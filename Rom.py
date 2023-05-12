import hashlib
import json
import os
import sys
import tempfile
import zipfile
from enum import Enum
from typing import Any

import Utils
from worlds.Files import AutoPatchRegister, APContainer
from . import Patches
from .inc.wwrando.wwlib.gcm import GCM

BFBB_HASH = "9e18f9a0032c4f3092945dc38a6517d3"


class BfBBDeltaPatch(APContainer, metaclass=AutoPatchRegister):
    hash = BFBB_HASH
    game = "Battle for Bikini Bottom"
    patch_file_ending: str = ".apbfbb"
    result_file_ending: str = ".gcm"
    zip_version: int = 1

    def __init__(self, *args: Any, **kwargs: Any):
        self.include_socks: int = kwargs['include_socks']
        self.include_skills: int = kwargs['include_skills']
        self.include_golden_underwear: int = kwargs['include_golden_underwear']
        self.include_level_items: int = kwargs['include_level_items']
        self.include_purple_so: int = kwargs['include_purple_so']
        self.seed: bytes = kwargs['seed']
        del kwargs['include_socks']
        del kwargs['include_skills']
        del kwargs['include_golden_underwear']
        del kwargs['include_level_items']
        del kwargs['include_purple_so']
        del kwargs['seed']
        super(BfBBDeltaPatch, self).__init__(*args, **kwargs)

    def write_contents(self, opened_zipfile: zipfile.ZipFile):
        super(BfBBDeltaPatch, self).write_contents(opened_zipfile)
        opened_zipfile.writestr("zip_version",
                                self.zip_version.to_bytes(1, "little"),
                                compress_type=zipfile.ZIP_STORED)
        opened_zipfile.writestr("include_socks",
                                self.include_socks.to_bytes(1, "little"),
                                compress_type=zipfile.ZIP_STORED)
        opened_zipfile.writestr("include_skills",
                                self.include_skills.to_bytes(1, "little"),
                                compress_type=zipfile.ZIP_STORED)
        opened_zipfile.writestr("include_golden_underwear",
                                self.include_golden_underwear.to_bytes(1, "little"),
                                compress_type=zipfile.ZIP_STORED)
        opened_zipfile.writestr("include_level_items",
                                self.include_level_items.to_bytes(1, "little"),
                                compress_type=zipfile.ZIP_STORED)
        opened_zipfile.writestr("include_purple_so",
                                self.include_purple_so.to_bytes(1, "little"),
                                compress_type=zipfile.ZIP_STORED)
        m = hashlib.md5()
        m.update(self.seed)
        opened_zipfile.writestr("seed",
                                m.digest(),
                                compress_type=zipfile.ZIP_STORED)

    def read_contents(self, opened_zipfile: zipfile.ZipFile) -> None:
        super(BfBBDeltaPatch, self).read_contents(opened_zipfile)

    @classmethod
    def get_bool(cls, opened_zipfile: zipfile.ZipFile, name: str):
        return bool.from_bytes(opened_zipfile.read(name), "little")

    @classmethod
    def get_manifest_json(cls, opened_zipfile: zipfile.ZipFile):
        with opened_zipfile.open("archipelago.json", "r") as f:
            manifest = json.load(f)
        return manifest

    @classmethod
    def get_seed_hash(cls, opened_zipfile: zipfile.ZipFile):
        return opened_zipfile.read("seed")

    @classmethod
    async def apply_hiphop_changes(cls, opened_zipfile: zipfile.ZipFile, source_iso, dest_iso):
        include_skills = BfBBDeltaPatch.get_bool(opened_zipfile, "include_skills")
        include_level_items = BfBBDeltaPatch.get_bool(opened_zipfile, "include_level_items")
        if not include_skills and not include_level_items:
            return
        # extract dependencies need to patch with IP
        world_path = os.path.join(__file__[:__file__.find('worlds') + len('worlds')], 'bfbb.apworld')
        is_ap_world = os.path.exists(world_path)
        lib_path = os.path.abspath(os.path.dirname(__file__) + '/inc/')
        if is_ap_world:
            lib_path = os.path.expandvars('%APPDATA%/bfbb_ap/')
            with zipfile.ZipFile(world_path) as world_zip:
                for file in world_zip.namelist():
                    if file.startswith('bfbb/inc/packages') or file.startswith('bfbb/inc/IP'):
                        try:
                            world_zip.extract(file, lib_path)
                        except:
                            print(f"warning: couldn't overwrite dependency: {file}")
            lib_path = lib_path + 'bfbb/inc/'
        if not lib_path in sys.path:
            sys.path.append(lib_path)
        # print(sys.path)
        # setup pythonnet
        from packages.pythonnet import load
        load()
        import clr
        # extract ISO content
        extraction_temp_dir = tempfile.TemporaryDirectory()
        extraction_path = extraction_temp_dir.name
        gcm = GCM(source_iso)
        gcm.read_entire_disc()
        generator = gcm.export_disc_to_folder_with_changed_files(output_folder_path=extraction_path,
                                                                 only_changed_files=False)
        print('--extracting--')
        while True:
            file_path, files_done = next(generator)
            print(file_path, files_done)
            if files_done == -1:
                break
        print('--extraction done--')
        print('--making changes--')
        # load and setup IP libs
        clr.AddReference(os.path.abspath(lib_path + '/IP/IndustrialPark.exe'))
        clr.AddReference(os.path.abspath(lib_path + '/IP/HipHopFile.dll'))
        from HipHopFile import Platform, Game
        from IndustrialPark import ArchiveEditorFunctions, Link, HexUIntTypeConverter
        class EventIDs(Enum):
            Increment = 0x000B
            Decrement = 0x000C
            GivePowerUp = 0x0101
            GiveCollectables = 0x01C2

        class LinkData:
            event = 0
            target = 0

            def __init__(self, event: EventIDs, target):
                self.event = event.value
                self.target = target

            def compare(self, link: Link):
                return link.EventSendID == self.event and link.TargetAsset.op_Implicit(link.TargetAsset) == self.target

        files_to_check_lvl_items = {
            'jf04': {
                # CUTSCENE_KJ_END
                0xbd99ade0: [
                    LinkData(EventIDs.GiveCollectables, 0xBD7097e3)
                ]
            },
            'gl01': {
                # BALLOON_A_PLAT
                0x3db4fe59: [
                    LinkData(EventIDs.GiveCollectables, 0xBD7097e3),
                    LinkData(EventIDs.Decrement, 0xa6662680),
                ],
                # BALLOON_B_PLAT
                0x393949cc: [
                    LinkData(EventIDs.GiveCollectables, 0xBD7097e3),
                    LinkData(EventIDs.Decrement, 0xa6662680),
                ],
                # BALLOON_C_PLAT
                0x34bd953f: [
                    LinkData(EventIDs.GiveCollectables, 0xBD7097e3),
                    LinkData(EventIDs.Decrement, 0xa6662680),
                ],
                # BALLOON_D_PLAT
                0x3041e0b2: [
                    LinkData(EventIDs.GiveCollectables, 0xBD7097e3),
                    LinkData(EventIDs.Decrement, 0xa6662680),
                ],
                # BALLOON_E_PLAT
                0x2bc62c25: [
                    LinkData(EventIDs.GiveCollectables, 0xBD7097e3),
                    LinkData(EventIDs.Decrement, 0xa6662680),
                ],
                # BALLOON_A_COUNT_DISP
                0x078dc464: [
                    LinkData(EventIDs.Decrement, 0xa6662680),
                ],
                # BALLOON_B_COUNT_DISP
                0xa65659df: [
                    LinkData(EventIDs.Decrement, 0xa6662680),
                ],
                # BALLOON_C_COUNT_DISP
                0x451eef5a: [
                    LinkData(EventIDs.Decrement, 0xa6662680),
                ],
                # BALLOON_D_COUNT_DISP
                0xe3e784d5: [
                    LinkData(EventIDs.Decrement, 0xa6662680),
                ],
                # BALLOON_E_COUNT_DISP
                0x82b01a50: [
                    LinkData(EventIDs.Decrement, 0xa6662680),
                ],
            },
            'bc02': {
                0x5e64831b: [
                    LinkData(EventIDs.GiveCollectables, 0xBD7097e3)
                ],
                0x5e64831c: [
                    LinkData(EventIDs.GiveCollectables, 0xBD7097e3)
                ]
            },
            'bc03': {
                0x91f2a6cf: [
                    LinkData(EventIDs.GiveCollectables, 0xBD7097e3)
                ],
            },
            'bc04': {
                0xc1841225: [
                    LinkData(EventIDs.GiveCollectables, 0xBD7097e3)
                ],
            },
            'sm03': {
                0xd4d3bec2: [
                    LinkData(EventIDs.Decrement, 0xc4e703d6)
                ],
                0xd4d3bec3: [
                    LinkData(EventIDs.Decrement, 0xc4e703d6)
                ],
                0xd4d3bec4: [
                    LinkData(EventIDs.Decrement, 0xc4e703d6)
                ],
                0xd4d3bec5: [
                    LinkData(EventIDs.Decrement, 0xc4e703d6)
                ],
                0xd4d3bec6: [
                    LinkData(EventIDs.Decrement, 0xc4e703d6)
                ],
                0xd4d3bec7: [
                    LinkData(EventIDs.Decrement, 0xc4e703d6)
                ],
                0xd4d3bec8: [
                    LinkData(EventIDs.Decrement, 0xc4e703d6)
                ],
                0xd4d3bec9: [
                    LinkData(EventIDs.Decrement, 0xc4e703d6)
                ],
            },
            'kf01': {
                0x153CCF73: [
                    LinkData(EventIDs.GiveCollectables, 0xBD7097e3),
                ],
                0x153CCF74: [
                    LinkData(EventIDs.GiveCollectables, 0xBD7097e3),
                ],
                0x153CCF75: [
                    LinkData(EventIDs.GiveCollectables, 0xBD7097e3),
                ],
            },
            'kf02': {
                0x9c2d8bb3: [
                    LinkData(EventIDs.GiveCollectables, 0xBD7097e3),
                ],
                0x9c2d8bb4: [
                    LinkData(EventIDs.GiveCollectables, 0xBD7097e3),
                ],
            },
            'kf04': {
                0x609203fd: [
                    LinkData(EventIDs.GiveCollectables, 0xBD7097e3),
                ],
                0x96017696: [
                    LinkData(EventIDs.Increment, 0xed81694f)
                ],
                0x96017697: [
                    LinkData(EventIDs.Increment, 0xed81694f)
                ],
                0x96017698: [
                    LinkData(EventIDs.Increment, 0xed81694f)
                ],
                0x96017699: [
                    LinkData(EventIDs.Increment, 0xed81694f)
                ],
                0x9601769a: [
                    LinkData(EventIDs.Increment, 0xed81694f)
                ],
                0x9601769b: [
                    LinkData(EventIDs.Increment, 0xed81694f)
                ],
            },
            'gy03': {
                0x1344a38c: [
                    LinkData(EventIDs.GiveCollectables, 0xBD7097e3),
                    LinkData(EventIDs.Decrement, 0x9a101de7),
                ],
                0x1344a38d: [
                    LinkData(EventIDs.GiveCollectables, 0xBD7097e3),
                    LinkData(EventIDs.Decrement, 0x9a101de7),
                ],
                0x1344a38e: [
                    LinkData(EventIDs.GiveCollectables, 0xBD7097e3),
                    LinkData(EventIDs.Decrement, 0x9a101de7),
                ],
                0x1344a38f: [
                    LinkData(EventIDs.GiveCollectables, 0xBD7097e3),
                    LinkData(EventIDs.Decrement, 0x9a101de7),
                ],
                0x46d4fa25: [
                    LinkData(EventIDs.Decrement, 0x9a101de7),
                ],
                0x46d4fa26: [
                    LinkData(EventIDs.Decrement, 0x9a101de7),
                ],
                0x46d4fa27: [
                    LinkData(EventIDs.Decrement, 0x9a101de7),
                ],
                0x46d4fa28: [
                    LinkData(EventIDs.Decrement, 0x9a101de7),
                ],
            },
        }
        files_to_check_skills = {
            'b101': {
                0xcc4ea457: [
                    LinkData(EventIDs.GivePowerUp, 0xBD7097e3)
                ]
            },
            'b201': {
                0xeb3aada0: [
                    LinkData(EventIDs.GivePowerUp, 0x00002abb)
                ]
            },
        }
        files_to_check: dict[str, dict[int, list[LinkData]]] = {}
        if include_skills:
            files_to_check.update(files_to_check_skills)
        if include_level_items:
            files_to_check.update(files_to_check_lvl_items)
        HexUIntTypeConverter.Legacy = True
        editor_funcs = ArchiveEditorFunctions()
        editor_funcs.SkipTextureDisplay = True
        editor_funcs.Platform = Platform.GameCube
        editor_funcs.Game = Game.BFBB
        editor_funcs.standalone = True
        # make changes with IP
        for name, assets_to_check in files_to_check.items():
            editor_funcs.OpenFile(extraction_path + f'/files/{name[:-2]}/{name}.HIP', False, Platform.Unknown)
            for id, links_to_check in assets_to_check.items():
                assert id in editor_funcs.assetDictionary, f"{id} is not a valid id in {name}.HIP"
                links = editor_funcs.assetDictionary[id].Links
                links_to_remove = []
                for data in links_to_check:
                    found = False
                    for link in links:
                        if data.compare(link):
                            print(f"removing link {link.ToString()} from 0x{id:x} in {name}.HIP")
                            links_to_remove.append(link)
                            found = True
                    if not found:
                        assert False, f"link not found {data.event} => 0x{data.target:x} on 0x{id:x} in {name}.HIP"
                editor_funcs.assetDictionary[id].Links = [link for link in links if link not in links_to_remove]
            editor_funcs.Save()
        print('--done making changes--')
        # repack ISO (as gcm for better distinction)
        print('--repacking--')
        num = gcm.import_all_files_from_disk(input_directory=extraction_path)
        generator = gcm.export_disc_to_iso_with_changed_files(dest_iso)
        while True:
            file_path, files_done = next(generator)
            print(file_path, files_done)
            if files_done == -1:
                break
        print('--repacking done--')
        # clean up
        extraction_temp_dir.cleanup()

    @classmethod
    async def apply_binary_changes(cls, opened_zipfile: zipfile.ZipFile, iso):
        print('--binary patching--')
        # get slot name and seed hash
        manifest = BfBBDeltaPatch.get_manifest_json(opened_zipfile)
        slot_name = manifest["player_name"]
        slot_name_bytes = slot_name.encode('utf-8')
        slot_name_offset = 0x2AB980
        seed_hash = BfBBDeltaPatch.get_seed_hash(opened_zipfile)
        seed_hash_offset = slot_name_offset + 0x40
        # always apply these patches
        patches = [Patches.AP_SAVE_LOAD, Patches.SPATS_REWARD_FIX]
        # conditional patches
        include_socks = BfBBDeltaPatch.get_bool(opened_zipfile, "include_socks")
        include_golden_underwear = BfBBDeltaPatch.get_bool(opened_zipfile, "include_golden_underwear")
        include_level_items = BfBBDeltaPatch.get_bool(opened_zipfile, "include_level_items")
        if include_socks:
            patches += [Patches.SOCKS_REWARD_FIX]
        if include_golden_underwear:
            patches += [Patches.GOLDEN_UNDERWEAR_REWARD_FIX]
        if include_level_items:
            patches += [Patches.LVL_ITEM_REWARD_FIX]
        with open(iso, "rb+") as stream:
            # write patches
            for patch in patches:
                print(f"applying patch {patches.index(patch) + 1}/{len(patches)}")
                for addr, val in patch.items():
                    stream.seek(addr, 0)
                    if type(val) == bytes:
                        stream.write(val)
                    else:
                        stream.write(val.to_bytes(0x4, "big"))
            # write slot name
            print(f"writing slot_name {slot_name} to 0x{slot_name_offset:x} ({slot_name_bytes})")
            stream.seek(slot_name_offset, 0)
            stream.write(slot_name_bytes)
            print(f"writing seed_hash {seed_hash} to 0x{seed_hash_offset:x}")
            stream.seek(seed_hash_offset, 0)
            stream.write(seed_hash)
        print('--binary patching done--')

    @classmethod
    def get_rom_path(cls) -> str:
        return get_base_rom_path()

    @classmethod
    def get_source_data(cls) -> bytes:
        return get_base_rom_bytes()

    @classmethod
    def check_version(cls, opened_zipfile: zipfile.ZipFile) -> bool:
        version_bytes = opened_zipfile.read("zip_version")
        version = 0
        if version_bytes is not None:
            version = int.from_bytes(version_bytes, "little")
        if version != cls.zip_version:
            return False
        return True


def get_base_rom_path(file_name: str = "") -> str:
    options: Utils.OptionsType = Utils.get_options()
    if not file_name:
        # file_name = options["bfbb_options"]["rom_file"]
        file_name = "Nickelodeon SpongeBob SquarePants - Battle for Bikini Bottom (USA).iso"
    if not os.path.exists(file_name):
        file_name = Utils.user_path(file_name)
    return file_name


def get_base_rom_bytes(file_name: str = ""):
    file_name = get_base_rom_path(file_name)
    with open(file_name, "rb") as file:
        base_rom_bytes = bytes(file.read())
    basemd5 = hashlib.md5()
    basemd5.update(base_rom_bytes)
    if BFBB_HASH != basemd5.hexdigest():
        raise Exception(f"Supplied Base Rom does not match known MD5 for BfBB (US). "
                        "Get the correct game and version.")
    return base_rom_bytes
