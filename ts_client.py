from teslasuit_sdk import ts_api
from teslasuit_sdk.subsystems import ts_haptic
from teslasuit_sdk.ts_mapper import TsBone2dIndex

import ts_playlist
from ff_event import FeedbackEvent, FeedbackEventType, FeedbackEventDirection, FeedbackEventLocation

class TsClient:
    def init(self, lib_path=None):
        print("Connecting teslasuit device...")
        api = ts_api.TsApi(lib_path)
        device = api.get_device_manager().get_or_wait_last_device_attached()
        self.player = device.haptic
        self.bones = api.mapper.get_layout_bones(api.mapper.get_haptic_electric_channel_layout(device.get_mapping()))
        print("Device connected.")
        print("Loading TS assets...")
        self.playlist = ts_playlist.TsPlaylist(api, device, "ts_assets")
        print("TS assets loaded.")

    def play_touch(self, params, channels, duration_ms):
        playable_id = player.create_touch(params, channels, duration_ms)
        self.player.play_playable(playable_id)

    def test_haptic(self):
        params = player.create_touch_parameters(100, 40, 150)
        bones = mapper.get_bone_contents(self.bones[TsBone2dIndex.RightUpperArm.value])
        duration_ms = 1000
        self.play_touch(params, bones, duration_ms)
        time.sleep(duration_ms / 1000)

    def process_ff_events(self, events):
        asset = None
        for event in events:
            asset_name = self.get_asset_name(event)
            if asset_name == None:
                continue
            if event.is_enable:
                self.playlist.play(asset_name, event.is_continue, event.intensity_percent, event.frequency_percent)
            else:
                self.playlist.stop(asset_name)

    def get_asset_name(self, event):
        if event.type == FeedbackEventType.Hit:
            if event.location == FeedbackEventLocation.Generic or event.location == FeedbackEventLocation.Head  or event.location == FeedbackEventLocation.Lethal:
                return "_full_body_hit.ts_asset"
            elif event.location == FeedbackEventLocation.Chest or event.location == FeedbackEventLocation.Stomach:
                if event.direction == FeedbackEventDirection.Front:
                    return "_body_front_hit.ts_asset"
                elif event.direction == FeedbackEventDirection.Back:
                    return "_body_back_hit.ts_asset"
                elif event.direction == FeedbackEventDirection.FrontLeft:
                    return "_body_front_left_hit.ts_asset"
                elif event.direction == FeedbackEventDirection.FrontRight:
                    return "_body_front_right_hit.ts_asset"
                elif event.direction == FeedbackEventDirection.BackLeft:
                    return "_body_back_left_hit.ts_asset"
                elif event.direction == FeedbackEventDirection.BackRight:
                    return "_body_back_right_hit.ts_asset"
                else:
                    return "_body_hit.ts_asset"
            elif event.location == FeedbackEventLocation.LeftArm:
                return "_left_hand_hit.ts_asset"
            elif event.location == FeedbackEventLocation.RightArm:
                return "_right_hand_hit.ts_asset"
            elif event.location == FeedbackEventLocation.LeftLeg:
                return "_left_leg_hit.ts_asset"
            elif event.location == FeedbackEventLocation.RightLeg:
                return "_right_leg_hit.ts_asset"
        elif event.type == FeedbackEventType.Recoil:
            if event.weapon_type == FeedbackEventWeaponType.Pistol:
                return "_recoil_pistol_l.ts_asset" if event.direction == FeedbackEventDirection.Left else "_recoil_pistol_r.ts_asset"
            elif event.weapon_type == FeedbackEventWeaponType.SMG:
                return "_recoil_smg_l.ts_asset" if event.direction == FeedbackEventDirection.Left else "_recoil_smg_r.ts_asset"
            elif event.weapon_type == FeedbackEventWeaponType.Rifle:
                return "_recoil_rifle_l.ts_asset" if event.direction == FeedbackEventDirection.Left else "_recoil_rifle_r.ts_asset"
            elif event.weapon_type == FeedbackEventWeaponType.Sniper:
                return "_recoil_sniper_l.ts_asset" if event.direction == FeedbackEventDirection.Left else "_recoil_sniper_r.ts_asset"
            elif event.weapon_type == FeedbackEventWeaponType.Shotgun:
                return "_recoil_shotgun_l.ts_asset" if event.direction == FeedbackEventDirection.Left else "_recoil_shotgun_r.ts_asset"
            elif event.weapon_type == FeedbackEventWeaponType.Knife:
                return "_recoil_knife_l.ts_asset" if event.direction == FeedbackEventDirection.Left else "_recoil_knife_r.ts_asset"
            elif event.weapon_type == FeedbackEventWeaponType.Healthshot:
                return "_recoil_healthshot_l.ts_asset" if event.direction == FeedbackEventDirection.Left else "_recoil_healthshot_r.ts_asset"
            elif event.weapon_type == FeedbackEventWeaponType.Throwable:
                return "_recoil_throwable_l.ts_asset" if event.direction == FeedbackEventDirection.Left else "_recoil_throwable_r.ts_asset"
        return None
