from typing import Callable, Dict

from BaseClasses import MultiWorld, CollectionState
from worlds.bfbb.Locations import SOCK_NAME_TABLE, krabs_spat_location_table
from worlds.generic.Rules import set_rule, add_rule


# ToDo:
# double check access rules


def _get_sock_location_name(level: str, nr: int):
    name = SOCK_NAME_TABLE[level][nr]
    return f"{level}: Lost Sock #{nr + 1}{f' ({name})' if len(name) > 0 else ''}"

def _get_krabs_spat_name(i: int):
    return f"Hub: Pay Mr. Krabs {30000 + i * 5000 + (5000 if i == 7 else 0)} Shiny Objects"

def set_rules(world: MultiWorld, player: int):
    set_rule(world.get_entrance("Pineapple->HB1", player), lambda state: state.has("Golden Spatula", player, 1))
    set_rule(world.get_entrance("HB1->BB1", player), lambda state: state.has("Golden Spatula", player, 5))
    set_rule(world.get_entrance("HB1->GL1", player), lambda state: state.has("Golden Spatula", player, 10))
    set_rule(world.get_entrance("HB1->Poseidome", player), lambda state: state.has("Golden Spatula", player, 15))
    set_rule(world.get_entrance("HB2->RB1", player), lambda state: state.has("Golden Spatula", player, 25))
    set_rule(world.get_entrance("HB2->SM1", player), lambda state: state.has("Golden Spatula", player, 30))
    set_rule(world.get_entrance("HB2->IP", player), lambda state: state.has("Golden Spatula", player, 40) and state.has("Bubble Bowl", player))
    set_rule(world.get_entrance("HB3->KF1", player), lambda state: state.has("Golden Spatula", player, 50))
    set_rule(world.get_entrance("HB3->GY1", player), lambda state: state.has("Golden Spatula", player, 60))
    set_rule(world.get_entrance("CB->CBLab", player), lambda state: state.has("Golden Spatula", player, 75) and state.has("Bubble Bowl", player) and state.has("Cruise Bubble", player))
    set_rule(world.get_entrance("Merm1->Merm2", player), lambda state: state.has("Bubble Bowl", player))
    set_rule(world.get_entrance("Merm2->Merm3", player), lambda state: state.has("Bubble Bowl", player))
    set_rule(world.get_entrance("Merm2->Merm5", player), lambda state: state.has("Bubble Bowl", player))
    set_rule(world.get_entrance("KF4->KF5", player), lambda state: state.has("Cruise Bubble", player))
    set_rule(world.get_entrance("KF4->KF2", player), lambda state: state.has("Cruise Bubble", player))

    set_rule(world.get_location("Hub2: On Top of Shady Shoals", player), lambda state: state.has("Bubble Bowl", player) or state.has("Cruise Bubble", player))
    set_rule(world.get_location("Hub3: On Top of the Chum Bucket", player), lambda state: state.has("Cruise Bubble", player))
    set_rule(world.get_location("BB04: Come Back With the Cruise Bubble", player), lambda state: state.has("Cruise Bubble", player))
    # ToDo: test Cruise Bubble
    set_rule(world.get_location("Merm02: Shut Down the Security System", player), lambda state: state.has("Bubble Bowl", player))
    # ToDo: test Cruise Bubble
    set_rule(world.get_location("Merm04: Complete the Rolling Ball Room", player), lambda state: state.has("Bubble Bowl", player))
    # ToDo: test Cruise Bubble
    set_rule(world.get_location("Merm05: Defeat Prawn", player), lambda state: state.has("Bubble Bowl", player))
    set_rule(world.get_location("KF01: Find All the Lost Campers", player), lambda state: state.has("Cruise Bubble", player))
    set_rule(world.get_location("KF04: Through the Kelp Caves", player), lambda state: state.has("Cruise Bubble", player))
    set_rule(world.get_location("KF04: Power Crystal Crisis", player), lambda state: state.has("Cruise Bubble", player))
    set_rule(world.get_location("Dream01: Follow the Bouncing Ball", player), lambda state: state.has("Bubble Bowl", player))
    for i in range(0, 8):
        set_rule(world.get_location(_get_krabs_spat_name(i), player), lambda state: state.has("Golden Spatula", player, 5 + 5 * i))
    for i in range(1, 9):
        set_rule(world.get_location(f"Hub: Return {i * 10} Socks To Patrick", player), lambda state: state.has("Lost Sock", player, i * 10))
    set_rule(world.get_location(_get_sock_location_name("JF03", 1), player), lambda state: state.has("Cruise Bubble", player))
    set_rule(world.get_location(_get_sock_location_name("BB04", 0), player), lambda state: state.has("Cruise Bubble", player))
    set_rule(world.get_location(_get_sock_location_name("GL03", 1), player), lambda state: state.has("Bubble Bowl", player) or state.has("Cruise Bubble", player))
    set_rule(world.get_location(_get_sock_location_name("KF01", 2), player), lambda state: state.has("Bubble Bowl", player))
    set_rule(world.get_location(_get_sock_location_name("KF04", 0), player), lambda state: state.has("Cruise Bubble", player))

    world.completion_condition[player] = lambda state: state.has("Victory", player)
