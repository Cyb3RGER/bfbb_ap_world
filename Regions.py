from .Locations import BfBBLocation, location_table, patrick_spat_location_table, krabs_spat_location_table, \
    sock_location_table, spat_location_table
from .Items import BfBBItem, item_table

from BaseClasses import MultiWorld, Region, Entrance, ItemClassification


def create_region(world: MultiWorld, player: int, name: str, locations=None, exits=None) -> Region:
    ret = Region(name, player, world)
    if locations:
        for location in locations:
            loc_id = location_table[location]
            location = BfBBLocation(player, location, loc_id, ret)
            ret.locations.append(location)
    if exits:
        for exit in exits:
            ret.exits.append(Entrance(player, exit, ret))
    return ret


""" 
Name Info:
HB = Hub
JF = Jellyfish Fields
BB = Downtown Bikini Bottom
GL = Goo Lagoon
RB = Rock Bottom
SM = Sand Mountain
IP = Industrial Park
KK = Krusty Krab
KF = Kelp Forest
GY = Graveyard
"""


class RegionData:
    def __init__(self, locations: list[str] = None, exits: list[str] = None):
        self.locations = locations
        self.exits = exits


def _get_locations_for_region(name: str) -> list[str]:
    return ([k for k in spat_location_table if f"{name}:" in k] +
            [k for k in sock_location_table if f"{name}:" in k]) + (
        [k for k in patrick_spat_location_table] + [k for k in krabs_spat_location_table] if name == "Hub1" else [])


regions: dict[str, RegionData] = {
    "Menu": RegionData([], ["StartGame"]),
    "Pineapple": RegionData(_get_locations_for_region("Pineapple"),
                            ["Pineapple->HB1"]),
    "HB1": RegionData(_get_locations_for_region("Hub1"),
                      ["HB1->Pineapple", "HB1->Squid", "HB1->Pat", "HB1->JF1", "HB1->BB1",
                       "HB1->GL1", "HB1->Poseidome"]),
    "Squid": RegionData(_get_locations_for_region("Squidward"),
                        ["Squid->HB1"]),
    "Pat": RegionData(_get_locations_for_region("Patrick"),
                      ["Pat->HB1"]),
    "JF1": RegionData(_get_locations_for_region("JF01"),
                      ["JF1->HB1", "JF1->JF2"]),
    "JF2": RegionData(_get_locations_for_region("JF02"),
                      ["JF2->JF1", "JF2->JF3"]),
    "JF3": RegionData(_get_locations_for_region("JF03"),
                      ["JF3->JF2", "JF3->JF4"]),
    "JF4": RegionData(_get_locations_for_region("JF04"),
                      ["JF4->JF3", "JF4->JF1"]),
    "BB1": RegionData(_get_locations_for_region("BB01"),
                      ["BB1->HB1", "BB1->BB2", "BB1->BB4"]),
    "BB2": RegionData(_get_locations_for_region("BB02"),
                      ["BB2->BB1", "BB2->BB3"]),
    "BB3": RegionData(_get_locations_for_region("BB03"),
                      ["BB3->BB2", "BB3->BB1"]),
    "BB4": RegionData(_get_locations_for_region("BB04"),
                      ["BB4->BB1"]),
    "GL1": RegionData(_get_locations_for_region("GL01"),
                      ["GL1->HB1", "GL1->GL2"]),
    "GL2": RegionData(_get_locations_for_region("GL02"),
                      ["GL2->GL1", "GL2->GL3"]),
    "GL3": RegionData(_get_locations_for_region("GL03"),
                      ["GL3->GL2", "GL3->GL1"]),
    "Poseidome": RegionData(_get_locations_for_region("Poseidome") + ["Bubble Bowl", "Robo-Sandy"],
                            ["Poseidome->HB1", "Poseidome->HB2"]),
    "HB2": RegionData(_get_locations_for_region("Hub2"),
                      ["HB2->HB1", "HB2->IP", "HB2->Tree Dome", "HB2->Shoals", "HB2->Police", "HB2->RB1", "HB2->SM1"]),
    "Tree Dome": RegionData(_get_locations_for_region("Tree Dome"),
                            ["Tree Dome->HB2"]),
    "Shoals": RegionData(_get_locations_for_region("Shoals"),
                         ["Shoals->HB2", "Shoals->Merm1"]),
    "Police": RegionData(_get_locations_for_region("Police"),
                         ["Police->HB2"]),
    "RB1": RegionData(_get_locations_for_region("RB01"),
                      ["RB1->HB2", "RB1->RB2", "RB1->RB3"]),
    "RB2": RegionData(_get_locations_for_region("RB02"),
                      ["RB2->RB1", "RB2->RB3"]),
    "RB3": RegionData(_get_locations_for_region("RB03"),
                      ["RB3->RB1"]),
    "Merm1": RegionData(_get_locations_for_region("Merm01"),
                        ["Merm1->Shoals", "Merm1->Merm2"]),
    "Merm2": RegionData(_get_locations_for_region("Merm02"),
                        ["Merm2->Merm1", "Merm2->Merm3", "Merm2->Merm5"]),
    "Merm3": RegionData(_get_locations_for_region("Merm03"),
                        ["Merm3->Merm2", "Merm3->Merm4"]),
    "Merm4": RegionData(_get_locations_for_region("Merm04"),
                        ["Merm4->Merm3", "Merm4->Merm2"]),
    "Merm5": RegionData(_get_locations_for_region("Merm05"),
                        ["Merm5->Merm2"]),
    "SM1": RegionData(_get_locations_for_region("SM01"),
                      ["SM1->HB2", "SM1->SM2", "SM1->SM3", "SM1->SM4"]),
    "SM2": RegionData(_get_locations_for_region("SM02"),
                      ["SM2->SM1"]),
    "SM3": RegionData(_get_locations_for_region("SM03"),
                      ["SM3->SM1"]),
    "SM4": RegionData(_get_locations_for_region("SM04"),
                      ["SM4->SM1"]),
    "IP": RegionData(_get_locations_for_region("IP") + ["Cruise Bubble", "Robo-Patrick"],
                     ["IP->HB2", "IP->HB3"]),
    "HB3": RegionData(_get_locations_for_region("Hub3"),
                      ["HB3->HB2", "HB3->CB", "HB3->KK", "HB3->KF1", "HB3->GY1", "HB3->Dream1"]),
    "KK": RegionData(_get_locations_for_region("KK"),
                     ["KK->HB3"]),
    "CB": RegionData(_get_locations_for_region("CB"),
                     ["CB->HB3", "CB->CBLab"]),
    "KF1": RegionData(_get_locations_for_region("KF01"),
                      ["KF1->HB3", "KF1->KF2", "KF1->KF5"]),
    "KF2": RegionData(_get_locations_for_region("KF02"),
                      ["KF2->KF1", "KF2->KF4"]),
    "KF4": RegionData(_get_locations_for_region("KF04"),
                      ["KF4->KF2", "KF4->KF5"]),
    "KF5": RegionData(_get_locations_for_region("KF05"),
                      ["KF5->KF4", "KF5->KF1"]),
    "GY1": RegionData(_get_locations_for_region("GY01"),
                      ["GY1->HB3", "GY1->GY2"]),
    "GY2": RegionData(_get_locations_for_region("GY02"),
                      ["GY2->GY1", "GY2->GY3"]),
    "GY3": RegionData(_get_locations_for_region("GY03"),
                      ["GY3->GY2", "GY3->GY4"]),
    "GY4": RegionData(_get_locations_for_region("GY04"),
                      ["GY4->GY3", "GY4->GY1"]),
    "Dream1": RegionData(_get_locations_for_region("Dream01"),
                         ["Dream1->HB3", "Dream1->Dream2", "Dream1->Dream3", "Dream1->Dream4", "Dream1->Dream5"]),
    "Dream2": RegionData(_get_locations_for_region("Dream02"),
                         ["Dream2->Dream1"]),
    "Dream3": RegionData(_get_locations_for_region("Dream03"),
                         ["Dream3->Dream1"]),
    "Dream4": RegionData(_get_locations_for_region("Dream04"),
                         ["Dream4->Dream1"]),
    "Dream5": RegionData(_get_locations_for_region("Dream05"),
                         ["Dream5->Dream1"]),
    "CBLab": RegionData(_get_locations_for_region("CB Lab") + ["Credits"],
                        ["CBLab->CB"])
}


def create_regions(world, player: int):
    # create regions
    world.regions = [
        create_region(world, player, k, v.locations, v.exits) for k, v in regions.items()
    ]

    # connect regions
    world.get_entrance("StartGame", player).connect(world.get_region("Pineapple", player))
    for k, v in regions.items():
        if k == "Menu":
            continue
        for exit in v.exits:
            exit_regions = exit.split('->')
            assert len(exit_regions) == 2
            # ToDo: warp rando
            target = world.get_region(exit_regions[1], player)
            world.get_entrance(exit, player).connect(target)


def test_regions(world):
    for reg in world.regions:
        print(reg.name)
        print("", "entrances")
        for ent in reg.entrances:
            print("", "", ent.name, ent.parent_region.name, ent.connected_region.name)
        print("", "exits")
        for ent in reg.exits:
            print("", "", ent.name, ent.parent_region.name, ent.connected_region.name)
