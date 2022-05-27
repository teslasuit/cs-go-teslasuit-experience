from ff_event import FeedbackEventWeaponType

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

WEAPON_FIRE_FEEDBACK = \
{
# Gear
"c4" : 0.2, "knife": 0.4, "knife_t": 0.4, "knife_gg": 0.4, "taser": 0.3, "shield": 0.5, "bumpmine": 0.2, "breachcharge": 0.2,
# Grenade
"decoy" : 0.4, "flashbang" : 0.4, "healthshot" : 0.8, "hegrenade" : 0.4, "incgrenade" : 0.4, "molotov" : 0.4, "smokegrenade" : 0.4, "tagrenade" : 0.4,
# Heavy
"m249" : 1, "mag7" : 0.8, "negev" : 1, "nova" : 0.85, "sawedoff" : 1, "xm1014" : 0.85,
# Pistol
"cz75a" : 0.35, "deagle" : 1, "elite" : 0.7, "fiveseven" : 0.6, "glock" : 0.4, "hkp2000" : 0.4, "p250" : 0.45, "revolver" : 0.8, "tec9" : 0.4, "usp_silencer" : 0.35, 
# Rifle
"ak47" : 0.75, "aug" : 0.65, "awp" : 1, "famas" : 0.55, "g3sg1" : 0.85, "galilar" : 0.55, "m4a1" : 0.55, "m4a1_silencer" : 0.5, "scar20" : 0.85, "sg556" : 0.65, "ssg08" : 0.7,
# SMG
"bizon" : 0.45, "mac10" : 0.45, "mp5sd" : 0.45, "mp7" : 0.45, "mp9" : 0.45, "p90" : 0.45, "ump45" : 0.45
}

WEAPON_TYPES = \
{
# Gear
"c4" : FeedbackEventWeaponType.Throwable, "knife": FeedbackEventWeaponType.Knife, "knife_t": FeedbackEventWeaponType.Knife, "knifegg": FeedbackEventWeaponType.Knife, "taser": FeedbackEventWeaponType.Pistol, "shield": FeedbackEventWeaponType.Throwable, "bumpmine": FeedbackEventWeaponType.Throwable, "breachcharge": FeedbackEventWeaponType.Throwable,
# Grenade
"decoy" : FeedbackEventWeaponType.Throwable, "flashbang" : FeedbackEventWeaponType.Throwable, "healthshot" : FeedbackEventWeaponType.Healthshot, "hegrenade" : FeedbackEventWeaponType.Throwable, "incgrenade" : FeedbackEventWeaponType.Throwable, "molotov" : FeedbackEventWeaponType.Throwable, "smokegrenade" : FeedbackEventWeaponType.Throwable, "tagrenade" : FeedbackEventWeaponType.Throwable,
# Heavy
"m249" : FeedbackEventWeaponType.Rifle, "mag7" : FeedbackEventWeaponType.Shotgun, "negev" : FeedbackEventWeaponType.Rifle, "nova" : FeedbackEventWeaponType.Shotgun, "sawedoff" : FeedbackEventWeaponType.Shotgun, "xm1014" : FeedbackEventWeaponType.Shotgun,
# Pistol
"cz75a" : FeedbackEventWeaponType.Pistol, "deagle" : FeedbackEventWeaponType.Pistol, "elite" : FeedbackEventWeaponType.Pistol, "fiveseven" : FeedbackEventWeaponType.Pistol, "glock" : FeedbackEventWeaponType.Pistol, "hkp2000" : FeedbackEventWeaponType.Pistol, "p250" : FeedbackEventWeaponType.Pistol, "revolver" : FeedbackEventWeaponType.Pistol, "tec9" : FeedbackEventWeaponType.Pistol, "usp_silencer" : FeedbackEventWeaponType.Pistol, 
# Rifle
"ak47" : FeedbackEventWeaponType.Rifle, "aug" : FeedbackEventWeaponType.Rifle, "awp" : FeedbackEventWeaponType.Sniper, "famas" : FeedbackEventWeaponType.Rifle, "g3sg1" : FeedbackEventWeaponType.Sniper, "galilar" : FeedbackEventWeaponType.Rifle, "m4a1" : FeedbackEventWeaponType.Rifle, "m4a1_silencer" : FeedbackEventWeaponType.Rifle, "scar20" : FeedbackEventWeaponType.Sniper, "sg556" : FeedbackEventWeaponType.Rifle, "ssg08" : FeedbackEventWeaponType.Sniper,
# SMG
"bizon" : FeedbackEventWeaponType.SMG, "mac10" : FeedbackEventWeaponType.SMG, "mp5sd" : FeedbackEventWeaponType.SMG, "mp7" : FeedbackEventWeaponType.SMG, "mp9" : FeedbackEventWeaponType.SMG, "p90" : FeedbackEventWeaponType.SMG, "ump45" : FeedbackEventWeaponType.SMG
}