from enum import StrEnum

from settings import Group, UserFilePath, Bool
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

    class RomStart(Bool):
        """
        Set this to false to never open the patched rom automatically,
        set this to true to auto launch the patched rom using Dolphin.
        """

    class UseTracker(Bool):
        """
        Set this to true to display UT Tracker and Map Page in the BfBB Client (if UT is installed)
        """

    class TrackerVariant(StrEnum):
        """
        overview: the tracker will only use one map to display all locations
        detailed: the tracker will only use detailed maps for every level to display locations
        """
        OVERVIEW = 'overview'
        DETAILED = 'detailed'


    rom_file: RomFile = RomFile(RomFile.copy_to)
    dolphin_path: DolphinPath = DolphinPath(None)
    rom_start: RomStart | bool = True
    use_tracker: UseTracker | bool = True
    tracker_variant: TrackerVariant | None = 'detailed'