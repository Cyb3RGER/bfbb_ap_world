from settings import Group, UserFilePath
from worlds.bfbb import Rom


class BattleForBikiniBottomSettings(Group):
    class RomFile(UserFilePath):
        """File name of the US Battle For Bikini Bottom ISO"""
        description = "US Battle For Bikini Bottom ISO File"
        copy_to = "Nickelodeon SpongeBob SquarePants - Battle for Bikini Bottom (USA).iso"
        md5s = [
            Rom.BFBB_HASH
        ]

    class DolphinPath(UserFilePath):
        """
        The location of the Dolphin executable you want to auto launch patched ROMs with
        """
        is_exe = True
        description = "Dolphin Executable"

    class RomStart(str):
        """
        Set this to false to never open the patched rom automatically,
        set this to true to auto launch the patched rom using Dolphin.
        """

    rom_file: RomFile = RomFile(RomFile.copy_to)
    dolphin_path: DolphinPath = DolphinPath(None)
    rom_start: bool = True