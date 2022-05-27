import sys
import ast
import re
import signal
import binascii
import telnetlib
import cs_go_weapons
from time import sleep
from enum import IntEnum, unique
from ff_event import FeedbackEvent, FeedbackEventType, FeedbackEventDirection, FeedbackEventLocation

# Config
TN_PORT = "2121"
TN_HOST = "127.0.0.1"

@unique
class HitGroup(IntEnum):
    Generic  = 0
    Head     = 1
    Chest    = 2
    Stomach  = 3
    LeftArm  = 4
    RightArm = 5
    LeftLeg  = 6
    RightLeg = 7
    Lethal   = 8

WEAPON_HAND = HitGroup.RightArm

class PlayerDamageEventParser:
    def __init__(self, damage_str: str):
        damage_dict = dict_from_ts_package(damage_str)
        self.health = int(damage_dict["health"])
        self.armor = int(damage_dict["armor"])
        self.weapon = str(damage_dict["weapon"])
        self.dmg_health = int(damage_dict["dmg_health"])
        self.dmg_armor = int(damage_dict["dmg_armor"])
        self.hit_group = HitGroup(int(damage_dict["hitgroup"]))

    def __str__(self):
        return "health: " + str(self.health) + ", armor: " + str(self.armor) + ", weapon: " + str(self.weapon) + \
            ", dmg_health: " + str(self.dmg_health) + ", dmg_armor: " + str(self.dmg_armor) + ", hit_group: " + str(self.hit_group)

    @staticmethod
    def get_keyword():
        return b"TsDamage"

class WeaponFireEventParser:
    def __init__(self, damage_str: str):
        fire_event_dict = dict_from_ts_package(damage_str)
        self.weapon = str(fire_event_dict["weapon"])
        self.is_silenced = bool(ast.literal_eval(fire_event_dict["is_silenced"].lower().capitalize()))

    def __str__(self):
        return "weapon: " + str(self.weapon) + ", is_silenced: " + str(self.is_silenced)

    @staticmethod
    def get_keyword():
        return b"TsWeaponFire"


class TsGoDamageListener:
    def __init__(self):
        self.host = TN_HOST
        self.port = TN_PORT

    def init(self):
        while True:
            if self.try_connect():
                print("CS:GO game connected.")
                break;
            else:
                print("Wait for connection to CS:GO game...")
                sleep(1)

    def set_event_callback(self, callback):
        self.event_callback = callback

    def read_handedness(self):
        cl_righthand = b"cl_righthand"
        handedness_str = self.get_var(cl_righthand)
        if handedness_str == None:
            return WEAPON_HAND
        handedness_val = int(handedness_str)
        if handedness_val > 0:
            return HitGroup.RightArm
        else:
            return HitGroup.LeftArm

    def get_var(self, command: bytes):
        command_unknown_str = ("Unknown command \"" + command.decode("utf-8") + "\"")
        cmd_unkn_str_b = command_unknown_str.encode("utf-8")
        self.tn.write(command + b"\n")
        line = b""
        response_received = False
        while not(response_received):
            line = self.tn.read_until(b"\n")
            if cmd_unkn_str_b in line:
                response_received = True
                return None
            if command in line:
                response_received = True
                expr = re.compile(b'"([^"]*)"')
                res = expr.findall(line)
                return res[1].decode("utf-8")
        return None


    def try_connect(self):
        try:
            self.tn = telnetlib.Telnet(self.host, self.port)
        except ConnectionRefusedError:
            print("Connection refused. Make sure you have the following launch option set in game launch arguments:")
            print("  -netconport " + str(self.port))
            return False
        self.tn.write(b"echo TS CS:GO Damage Handler Activated\n")
        WEAPON_HAND = self.read_handedness()
        return True

    def process(self):
        line = b""
        package_received = False
        haptic_event = None
        while not(package_received):
            line = self.tn.read_until(b"\n")
            if WeaponFireEventParser.get_keyword() in line:
                package_received = True
                fire_event = WeaponFireEventParser(line.decode("utf-8"))
                print(fire_event)
                haptic_event = self.convert_weapon_fire_to_haptic_event(fire_event)
            if PlayerDamageEventParser.get_keyword() in line:
                package_received = True
                damage_event = PlayerDamageEventParser(line.decode("utf-8"))
                print(damage_event)
                haptic_event = self.convert_damage_to_haptic_event(damage_event)

        if self.event_callback != None:
            self.event_callback({haptic_event})
        else:
            print("CS GO client: no client subscribed to events")

    def convert_damage_to_haptic_event(self, damage_event):
        dmg_percent = normalize(damage_event.dmg_health, float(0), float(100))
        return FeedbackEvent(type=FeedbackEventType.Hit,
            direction=FeedbackEventDirection.Front,
            location=FeedbackEventLocation(damage_event.hit_group.value + 1),
            intensity_percent=percent_to_intensity(dmg_percent, float(0.3), float(1)))

    def convert_weapon_fire_to_haptic_event(self, weapon_fire_event):
        dmg_percent = 0
        if weapon_fire_event.weapon in cs_go_weapons.WEAPON_FIRE_FEEDBACK:
            dmg_percent = cs_go_weapons.WEAPON_FIRE_FEEDBACK[weapon_fire_event.weapon]
        return FeedbackEvent(type=FeedbackEventType.Recoil,
            direction=FeedbackEventDirection.Front,
            location=FeedbackEventLocation(WEAPON_HAND.value + 1),
            intensity_percent=dmg_percent, float(0.3), float(1))

def normalize(value, min, max):
    if (value > max):
        return float(1)
    elif (value < min):
        return float(0)
    else:
        return float(value - min) / float(max - min)

def percent_to_intensity(value, min, max):
    if value == 0:
        return 0
    return float(max - min) * float(value) + float(min)

def dict_from_ts_package(ts_package_str: str):
    package_dict = {}
    ts_package_str = ts_package_str.strip().replace(" ", "")
    fields = ts_package_str[ts_package_str.find("{") + 1 : ts_package_str.find("}")].split(",")
    for row in fields:
        kv = row.split(":")
        package_dict[kv[0]] = kv[1]
    return package_dict
