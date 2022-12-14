from enum import IntEnum, unique

@unique
class FeedbackEventType(IntEnum):
    Undefined = 0
    Hit = 1
    Recoil = 2

@unique
class FeedbackEventWeaponType(IntEnum):
    Undefined = 0
    Pistol = 1
    SMG = 2
    Rifle = 3
    Sniper = 4
    Shotgun = 5
    Knife = 6
    Healthshot = 7
    Throwable = 8

@unique
class FeedbackEventDirection(IntEnum):
    Undefined = 0
    Front = 1
    Back = 2
    Left = 3
    Right = 4
    Up = 5
    Down = 6
    FrontLeft = 7
    FrontRight = 8
    BackLeft = 9
    BackRight = 10

@unique
class FeedbackEventLocation(IntEnum):
    Undefined = 0
    Generic  = 1
    Head     = 2
    Chest    = 3
    Stomach  = 4
    LeftArm  = 5
    RightArm = 6
    LeftLeg  = 7
    RightLeg = 8
    Lethal   = 9

class FeedbackEvent:
    def __init__(self, is_enable=True, is_continue=True, type=FeedbackEventType.Undefined, weapon_type=FeedbackEventWeaponType.Undefined, direction=FeedbackEventDirection.Undefined, location=FeedbackEventLocation.Undefined, intensity_percent=float(0), frequency_percent=float(0)):
        self.is_enable = is_enable
        self.is_continue = is_continue
        self.type = type
        self.weapon_type = weapon_type
        self.direction = direction
        self.location = location
        self.intensity_percent = intensity_percent
        self.frequency_percent = frequency_percent

    def is_same(self, event):
        return self.type == event.type and self.direction == event.direction and self.location == event.location
