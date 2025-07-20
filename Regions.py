from typing import List, Dict

from . import BfBBOptions
from .Locations import BfBBLocation, location_table, \
    sock_location_table, spat_location_table, level_item_location_table, golden_underwear_location_table, \
    skill_location_table, purple_so_location_table
from .constants import ConnectionNames, LevelNames, RegionNames, LocationNames

from BaseClasses import MultiWorld, Region, Entrance


def create_region(world: MultiWorld, player: int, name: str, locations=None, exits=None) -> Region:
    ret = Region(name, player, world)
    if locations:
        for location in locations:
            loc_id = location_table[location]
            location = BfBBLocation(player, location, loc_id, ret)
            ret.locations.append(location)
    if exits:
        for _exit in exits:
            ret.exits.append(Entrance(player, _exit, ret))
    return ret


def _get_locations_for_region(options: BfBBOptions, name: str) -> List[str]:
    result = [k for k in spat_location_table if f"{name}:" in k]
    if name == RegionNames.hub1:
        result += [k for k in spat_location_table if f"{LevelNames.hub}:" in k]
    if name == RegionNames.b3:
        result += [LocationNames.credits]
    if options.include_socks.value:
        result += [k for k in sock_location_table if f"{name}:" in k]
    if options.include_skills.value:
        result += [k for k in skill_location_table if f"{name}:" in k]
    if options.include_golden_underwear.value and "Hub" in name:
        result += [k for k in golden_underwear_location_table if f"{name}:" in k]
    if options.include_level_items.value:
        result += [k for k in level_item_location_table if f"{name}:" in k]
    if options.include_purple_so.value:
        result += [k for k in purple_so_location_table if f"{name}:" in k]
    return result


exit_table: Dict[str, List[str]] = {
    RegionNames.menu: [ConnectionNames.start_game],
    RegionNames.pineapple: [ConnectionNames.pineapple_hub1],
    RegionNames.hub1: [ConnectionNames.hub1_pineapple, ConnectionNames.hub1_squid, ConnectionNames.hub1_pat,
                       ConnectionNames.hub1_jf01, ConnectionNames.hub1_bb01, ConnectionNames.hub1_gl01,
                       ConnectionNames.hub1_b1],
    RegionNames.squid: [ConnectionNames.squid_hub1],
    RegionNames.pat: [ConnectionNames.pat_hub1],
    RegionNames.jf01: [ConnectionNames.jf01_hub1, ConnectionNames.jf01_jf02],
    RegionNames.jf02: [ConnectionNames.jf02_jf01, ConnectionNames.jf02_jf03],
    RegionNames.jf03: [ConnectionNames.jf03_jf02, ConnectionNames.jf03_jf04],
    RegionNames.jf04: [ConnectionNames.jf04_jf03, ConnectionNames.jf04_jf01],
    RegionNames.bb01: [ConnectionNames.bb01_hub1, ConnectionNames.bb01_bb02, ConnectionNames.bb01_bb04],
    RegionNames.bb02: [ConnectionNames.bb02_bb01, ConnectionNames.bb02_bb03],
    RegionNames.bb03: [ConnectionNames.bb03_bb02, ConnectionNames.bb03_bb01],
    RegionNames.bb04: [ConnectionNames.bb04_bb01],
    RegionNames.gl01: [ConnectionNames.gl01_hub1, ConnectionNames.gl01_gl02],
    RegionNames.gl02: [ConnectionNames.gl02_gl01, ConnectionNames.gl02_gl03],
    RegionNames.gl03: [ConnectionNames.gl03_gl02, ConnectionNames.gl03_gl01],
    RegionNames.b1: [ConnectionNames.b1_hub1, ConnectionNames.b1_hub2],
    RegionNames.hub2: [ConnectionNames.hub2_hub1, ConnectionNames.hub2_tree, ConnectionNames.hub2_shoals,
                       ConnectionNames.hub2_police, ConnectionNames.hub2_rb01, ConnectionNames.hub2_sm01,
                       ConnectionNames.hub2_b2],
    RegionNames.tree: [ConnectionNames.tree_hub2],
    RegionNames.shoals: [ConnectionNames.shoals_hub2, ConnectionNames.shoals_bc01],
    RegionNames.police: [ConnectionNames.police_hub2],
    RegionNames.rb01: [ConnectionNames.rb01_hub2, ConnectionNames.rb01_rb02, ConnectionNames.rb01_rb03],
    RegionNames.rb02: [ConnectionNames.rb02_rb01, ConnectionNames.rb02_rb03],
    RegionNames.rb03: [ConnectionNames.rb03_rb01],
    RegionNames.bc01: [ConnectionNames.bc01_shoals, ConnectionNames.bc01_bc02],
    RegionNames.bc02: [ConnectionNames.bc02_bc01, ConnectionNames.bc02_bc03, ConnectionNames.bc02_bc05],
    RegionNames.bc03: [ConnectionNames.bc03_bc02, ConnectionNames.bc03_bc04],
    RegionNames.bc04: [ConnectionNames.bc04_bc03, ConnectionNames.bc04_bc02],
    RegionNames.bc05: [ConnectionNames.bc05_bc02],
    RegionNames.sm01: [ConnectionNames.sm01_hub2, ConnectionNames.sm01_sm02, ConnectionNames.sm01_sm03,
                       ConnectionNames.sm01_sm04],
    RegionNames.sm02: [ConnectionNames.sm02_sm01],
    RegionNames.sm03: [ConnectionNames.sm03_sm01],
    RegionNames.sm04: [ConnectionNames.sm04_sm01],
    RegionNames.b2: [ConnectionNames.b2_hub2, ConnectionNames.b2_hub3],
    RegionNames.hub3: [ConnectionNames.hub3_hub2, ConnectionNames.hub3_kk, ConnectionNames.hub3_cb,
                       ConnectionNames.hub3_kf01, ConnectionNames.hub3_gy01, ConnectionNames.hub3_db01],
    RegionNames.kk: [ConnectionNames.kk_hub3],
    RegionNames.cb: [ConnectionNames.cb_hub3, ConnectionNames.cb_b3],
    RegionNames.kf01: [ConnectionNames.kf01_hub3, ConnectionNames.kf01_kf02, ConnectionNames.kf01_kf05],
    RegionNames.kf02: [ConnectionNames.kf02_kf01, ConnectionNames.kf02_kf04],
    RegionNames.kf04: [ConnectionNames.kf04_kf02, ConnectionNames.kf04_kf05],
    RegionNames.kf05: [ConnectionNames.kf05_kf04, ConnectionNames.kf05_kf01],
    RegionNames.gy01: [ConnectionNames.gy01_hub3, ConnectionNames.gy01_gy02],
    RegionNames.gy02: [ConnectionNames.gy02_gy01, ConnectionNames.gy02_gy03],
    RegionNames.gy03: [ConnectionNames.gy03_gy02, ConnectionNames.gy03_gy04],
    RegionNames.gy04: [ConnectionNames.gy04_gy03, ConnectionNames.gy04_gy01],
    RegionNames.db01: [ConnectionNames.db01_hub3, ConnectionNames.db01_db02, ConnectionNames.db01_db03,
                       ConnectionNames.db01_db04, ConnectionNames.db01_db05],
    RegionNames.db02: [ConnectionNames.db02_db01],
    RegionNames.db03: [ConnectionNames.db03_db01],
    RegionNames.db04: [ConnectionNames.db04_db01],
    RegionNames.db05: [ConnectionNames.db05_db01],
    RegionNames.b3: [ConnectionNames.b3_cb]
}


def create_regions(world: MultiWorld, options: BfBBOptions, player: int):
    # create regions
    world.regions += [
        create_region(world, player, k, _get_locations_for_region(options, k), v) for k, v in exit_table.items()
    ]

    # connect regions
    world.get_entrance(ConnectionNames.start_game, player).connect(world.get_region(RegionNames.pineapple, player))
    for k, v in exit_table.items():
        if k == RegionNames.menu:
            continue
        for _exit in v:
            exit_regions = _exit.split('->')
            assert len(exit_regions) == 2
            # ToDo: warp rando
            target = world.get_region(exit_regions[1], player)
            world.get_entrance(_exit, player).connect(target)
