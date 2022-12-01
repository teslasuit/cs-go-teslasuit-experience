# CS:GO Teslasuit Experience
Application for real time generation of Teslasuit haptic feedback on Teslasuit for CS:GO game. Feedback generation is based on stream of collision events from special modified workshop maps from the game.
Feedback is implemented for bullet hit in different ares:
- body front/back and left/right parts
- each leg front/back parts
- each arm front/back parts
- fullbody and general damage
Feedback is implemented for recoil with unique haptic animations and touch parameters for each weapon.

## Setup Environment
1. Install Teslasuit Control Center - https://teslasuit.io/.
2. Install Python 3 x64 from https://www.python.org/downloads/.
3. Install Steam and CS:GO game from it - https://store.steampowered.com/.

## Configuration
1. Set launch option for CS:GO in game properties in steam: "-netconport 2121" to enable haptic event streaming from the game.
2. Subscribe to haptic maps from workshop. Try link or find for 'haptic' keyword in CS:GO steam workshop search https://steamcommunity.com/sharedfiles/filedetails/?id=2809580208.
3. Connect Teslasuit device to PC and calibrate it in Control Center.

## Running
1. Connect calibrated Teslasuit device to PC.
2. Run CS:GO game and select workshop map.
3. Run main.py - it will auto detect connected device, listen game telemetry and generate haptic feedback.
3. Close main.py terminal to stop feedback.
4. It can be run from terminal to check for errors in terminal window.

## Development

### Project structure
1. Project contains two main components - CS:GO game client and Teslasuit client.
2. CS:GO game client (cs_go_client.py) listen packages from the game and generates unified force feedback events (ff_event.py).
3. Teslasuit client (ts_client.py) detects attached suit, process feedback events into playback for haptic presets. TS client includes playlist object (playlist.py) to parse assets from disk, preload assets, control assets playback and modifiers.
4. Directory ts_assets contains haptic assets for different feedback events, Teslasuit Studio project that can be used to view or modify haptic assets, template haptic calibration file that can be used to start calibration with it.

### Links
https://wiki.alliedmods.net/Counter-Strike:_Global_Offensive_Weapons
