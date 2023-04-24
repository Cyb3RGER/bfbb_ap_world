import typing
from BaseClasses import Location


class BfBBLocation(Location):
    game: str = "Battle for Bikini Bottom"


base_id = 149000

patrick_spat_location_table = {f"Hub: Return {(i + 1) * 10} Socks To Patrick": base_id + 84 + i for i in range(0, 8)}
krabs_spat_location_table = {
    f"Hub: Pay Mr. Krabs {30000 + i * 5000 + (5000 if i == 7 else 0)} Shiny Objects": base_id + 92 + i for i in
    range(0, 8)}
spat_location_table = {
    # Hub (0-7)
    "Hub1: On Top of the Pineapple": base_id + 0,
    "Hub2: On Top of Shady Shoals": base_id + 1,
    "Hub3: On Top of the Chum Bucket": base_id + 2,
    "Pineapple: SpongeBob's Closet": base_id + 3,
    "Squidward: Annoy Squidward": base_id + 4,
    "Tree Dome: Ambush at the Tree Dome": base_id + 5,
    "KK: Infestation at the Krusty Krab": base_id + 6,
    "CB: A Wall Jump in the Bucket": base_id + 7,
    # JF (8-15)
    "JF01: Top of the Hill": base_id + 8,
    "JF01: Cowa-Bungee!": base_id + 9,
    "JF02: Spelunking": base_id + 10,
    "JF02: Patrick's Dilemma": base_id + 11,
    "JF03: Navigate the Canyons and Mesas": base_id + 12,
    "JF03: Drain the Lake": base_id + 13,
    "JF04: Slide Leap": base_id + 14,
    "JF01: Defeat King Jellyfish": base_id + 15,
    # BB (16-23)
    "BB01: End of the Road": base_id + 16,
    "BB01: Learn Sandy's Moves": base_id + 17,
    "BB01: Tikis Go Boom": base_id + 18,
    "BB02: Across the Rooftops": base_id + 19,
    "BB02: Swingin' Sandy": base_id + 20,
    "BB03: Ambush in the Lighthouse": base_id + 21,
    "BB04: Extreme Bungee": base_id + 22,
    "BB04: Come Back With the Cruise Bubble": base_id + 23,
    # GL (24-31)
    "GL01: King of the Castle": base_id + 24,
    "GL01: Connect the Towers": base_id + 25,
    "GL01: Save the Children": base_id + 26,
    "GL01: Over the Moat": base_id + 27,
    "GL02: Through the Sea Caves": base_id + 28,
    "GL03: Clean out the Bumper Boats": base_id + 29,
    "GL03: Slip and Slide Under the Pier": base_id + 30,
    "GL03: Tower Bungee": base_id + 31,
    # Poseidome (32)
    "Poseidome: Defeat Robo-Sandy": base_id + 32,
    # RB (33-40)
    "RB01: Get to the Museum": base_id + 33,
    "RB01: Slip Sliding Away": base_id + 34,
    "RB01: Return the Museum's Art": base_id + 35,
    "RB01: Swingalong Spatula": base_id + 36,
    "RB02: Plundering Robots in the Museum": base_id + 37,
    "RB03: Across the Trench of Darkness": base_id + 38,
    "RB03: Lasers are Fun and Good for You": base_id + 39,
    "RB03: How in Tarnation Do You Get There?": base_id + 40,
    # Merm (41-48)
    "Merm01: Top of the Entrance Area": base_id + 41,
    "Merm02: Top of the Computer Area": base_id + 42,
    "Merm02: Shut Down the Security System": base_id + 43,
    "Merm02: The Funnel Machines": base_id + 44,
    "Merm02: The Spinning Towers of Power": base_id + 45,
    "Merm03: Top of the Security Tunnel": base_id + 46,
    "Merm04: Complete the Rolling Ball Room": base_id + 47,
    "Merm05: Defeat Prawn": base_id + 48,
    # SM (49-56)
    "SM01: Frosty Bungee": base_id + 49,
    "SM01: Top of the Lodge": base_id + 50,
    "SM02: Defeat Robots on Guppy Mound": base_id + 51,
    "SM02: Beat Mrs. Puff's Time": base_id + 52,
    "SM03: Defeat Robots on Flounder Hill": base_id + 53,
    "SM03: Beat Bubble Buddy's Time": base_id + 54,
    "SM04: Defeat Robots on Sand Mountain": base_id + 55,
    "SM04: Beat Larry's Time": base_id + 56,
    # IP (57)
    "IP: Defeat Robo-Patrick": base_id + 57,
    # KF (58-65)
    "KF01: Through the Woods": base_id + 58,
    "KF01: Find All the Lost Campers": base_id + 59,
    "KF02: Tiki Roundup": base_id + 60,
    "KF02: Down in the Swamp": base_id + 61,
    "KF04: Through the Kelp Caves": base_id + 62,
    "KF04: Power Crystal Crisis": base_id + 63,
    "KF05: Kelp Vine Slide": base_id + 64,
    "KF05: Beat Mermaid Man's Time": base_id + 65,
    # GY (66-73)
    "GY01: Top of the Entrance Area": base_id + 66,
    "GY01: A Path Through the Goo": base_id + 67,
    "GY01: Goo Tanker Ahoy!": base_id + 68,
    "GY02: Top of the Stack of Ships": base_id + 69,
    "GY02: Shipwreck Bungee": base_id + 70,
    "GY03: Destroy the Robot Ship": base_id + 71,
    "GY03: Get Aloft There, Matey!": base_id + 72,
    "GY04: Defeat the Flying Dutchman": base_id + 73,
    # Dream (74-81)
    "Dream01: Across the Dreamscape": base_id + 74,
    "Dream01: Follow the Bouncing Ball": base_id + 75,
    "Dream02: Slidin' Texas Style": base_id + 76,
    "Dream02: Swingers Ahoy": base_id + 77,
    "Dream03: Music is in the Ear of the Beholder": base_id + 78,
    "Dream04: Krabby Patty Platforms": base_id + 79,
    "Dream01: Super Bounce": base_id + 80,
    "Dream05: Here You Go": base_id + 81,
    # CB (82-83)
    "CB Lab: KAH - RAH - TAE!": base_id + 82,
    "CB Lab: The Small Shall Rule... Or No": base_id + 83,
    # Patrick (84-91)
    **patrick_spat_location_table,
    # Mr. Krabs (92-99)
    **krabs_spat_location_table,
}

SOCK_NAME_TABLE = {
    "Hub3": [
        "Behind KK under trash",
    ],
    "Hub2": [
        "Fountain",
    ],
    "Hub1": [
        "Patrick",
    ],
    "Pineapple": [
        "Library",
    ],
    "Squidward": [
        "Destroy all furniture",
    ],
    "Patrick": [
        "Destroy all furniture"
    ],
    "Shoals": [
        "Shoals",
    ],
    "KK": [
        "",
    ],
    "JF01": [
        "On JF rock",
        "Bungee",
        "On island",
        "Fountain",
        "On goo",
        "Bowling minigame",
    ],
    "JF02": [
        "On slide",
        "After slide",
        "In cave near slide",
        "On goo in cave",
    ],
    "JF03": [
        "On Cliff near Clamp",
        "Tiki Minigame",
        "Near wall jumps",
    ],
    "JF04": [
        "On Slide after JFK",
    ],
    "BB01": [
        "On broken house",
        "In broken house",
        "On floating platform",
        "On copper house",
    ],
    "BB02": [
        "On windmill",
        "Under slide",
        "Behind lighthouse"
    ],
    "BB03": [
        "On top"
    ],
    "BB04": [
        "South side"
    ],
    "GL01": [
        "On watchtower",
        "In sand castle",
        "On juice bar",
        "On top of sand castle",
        "Sand castle entrance gate"
    ],
    "GL02": [
        "Under ledge near entrance",
        "On goo",
        "On side ledge"
    ],
    "GL03": [
        "Tiki minigame",
        "Sliding minigame",
        "On booth"
    ],
    "RB01": [
        "On roof near elevator",
        "On rock",
        "Near slide end"
    ],
    "RB02": [
        "Ledge near exit",
        "Midway right ledge",
        "On entrance"
    ],
    "RB03": [
        "Bungee",
        "Near Duplicatotron",
        "At button under laser"
    ],
    "Merm01": [
        "Bungee"
    ],
    "Merm02": [
        "On light"
    ],
    "Merm03": [
        "Conveyor clamp"
    ],
    "Merm04": [
        "Behind tilting platform near end"
    ],
    "SM01": [
        "Below bridge",
        "Snowman",
    ],
    "SM02": [
        "Ledge near start",
        "Underpass",
        "Ledge near end"
    ],
    "SM03": [
        "At end",
        "On last tunnel near end"
    ],
    "SM04": [
        "Top ledge near start",
        "In hidden cave",
        "On ice platforms"
    ],
    "KF01": [
        "On high platform near Ms. Puff",
        "At waterfall",
        "Tiki bowling"
    ],
    "KF02": [
        "On ledge",
        "On tiki stack"
    ],
    "KF04": [
        "On ledge near entrance"
    ],
    "KF05": [
        "On slide"
    ],
    "GY01": [
        "On mast platform in goo"
    ],
    "GY02": [
        "In shipwreck"
    ],
    "GY03": [
        "On rope on robot ship"
    ],
    "Dream02": [
        "On top slide near skull",
        "Oil tower",
        "Behind house on Swingers platform"
    ],
    "Dream03": [
        "In air near trampoline"
    ],
    "Dream04": [
        "Behind grill"
    ]

}

sock_location_table = {
}
j = 0
for k, v in SOCK_NAME_TABLE.items():
    for i in range(0, len(v)):
        sock_location_table[f"{k}: Lost Sock #{i + 1}{f' ({v[i]})' if len(v[i]) > 0 else ''}"] = base_id + 100 + j
        j += 1

location_table = {
    **spat_location_table,
    **sock_location_table,
    "Bubble Bowl": base_id + 202,
    "Cruise Bubble": base_id + 203,
    "Robo-Sandy": None,
    "Robo-Patrick": None,
    "Credits": None
}

lookup_id_to_name: typing.Dict[int, str] = {id: name for name, id in location_table.items()}
