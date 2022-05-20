import sys
import signal
import binascii
import telnetlib
from time import sleep
from enum import IntEnum, unique
from ff_event import FeedbackEvent, FeedbackEventType, FeedbackEventDirection, FeedbackEventLocation

# Config
TN_PORT = "2121"
TN_HOST = "127.0.0.1"

# Weapon codes from https://wiki.alliedmods.net/Counter-Strike:_Global_Offensive_Weapons
WEAPON_CODES = \
{
# Gear
"c4", "knife", "taser", "shield", "bumpmine", "breachcharge",
# Grenade
"decoy", "flashbang", "healthshot", "hegrenade", "incgrenade", "molotov", "smokegrenade", "tagrenade",
# Heavy
"m249", "mag7", "negev", "nova", "sawedoff", "xm1014",
# Pistol
"cz75a", "deagle", "elite", "fiveseven", "glock", "hkp2000", "p250", "revolver", "tec9", "usp_silencer", 
# Rifle
"ak47", "aug", "awp", "famas", "g3sg1", "galilar", "m4a1", "m4a1_silencer", "scar20", "sg556", "ssg08",
# SMG
"bizon", "mac10", "mp5sd", "mp7", "mp9", "p90", "ump45"
}

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

class PlayerDamageEventParser:
    def __init__(self, damage_str: str):
        damage_dict = {}
        damage_str = damage_str.strip().replace(" ", "")
        fields = damage_str[damage_str.find("{") + 1 : damage_str.find("}")].split(",")
        for row in fields:
            kv = row.split(":")
            damage_dict[kv[0]] = kv[1]
        self.health = int(damage_dict["health"])
        self.armor = int(damage_dict["armor"])
        self.weapon = str(damage_dict["weapon"])
        self.dmg_health = int(damage_dict["dmg_health"])
        self.dmg_armor = int(damage_dict["dmg_armor"])
        self.hit_group = HitGroup(int(damage_dict["hitgroup"]))

    def __str__(self):
        return "health: " + str(self.health) + ", armor: " + str(self.armor) + ", weapon: " + str(self.weapon) + \
            ", dmg_health: " + str(self.dmg_health) + ", dmg_armor: " + str(self.dmg_armor) + ", hit_group: " + str(self.hit_group)

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

    def try_connect(self):
        try:
            self.tn = telnetlib.Telnet(self.host, self.port)
        except ConnectionRefusedError:
            print("Connection refused. Make sure you have the following launch option set in game launch arguments:")
            print("  -netconport " + str(self.port))
            return False
        self.tn.write(b"echo TS CS:GO Damage Handler Activated\n")
        return True

    def process(self):
        line = b""
        while not(b"TsDamage") in line:
            line = self.tn.read_until(b"\n")
        damage_event = PlayerDamageEventParser(line.decode("utf-8"))
        haptic_event = self.convert_damage_to_haptic_event(damage_event)
        if self.event_callback != None:
            print(damage_event)
            self.event_callback({haptic_event})
        else:
            print(damage_event)
            print("CS GO client: no client subscribed to events")

    def convert_damage_to_haptic_event(self, damage_event):
        dmg_percent = normalize(damage_event.dmg_health, float(0), float(100))
        return FeedbackEvent(type=FeedbackEventType.Hit,
            direction=FeedbackEventDirection.Front,
            location=FeedbackEventLocation(damage_event.hit_group.value + 1),
            intensity_percent=percent_to_intensity(dmg_percent, float(0.3), float(1)))

def normalize(value, min, max):
    if (value > max):
        return float(1)
    elif (value < min):
        return float(0)
    else:
        return float(value - min) / float(max - min)

def percent_to_intensity(value, min, max):
    return float(max - min) * float(value) + float(min)
