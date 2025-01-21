# BfBB AP world ring link port

Battle for Bikini Bottom [Archipelago](https://archipelago.gg/) world.
More info [here](https://github.com/Cyb3RGER/bfbb_ap_world/blob/main/docs/en_bfbb.md).

## Installation & Usage

See the [setup guide](https://github.com/Cyb3RGER/bfbb_ap_world/blob/main/docs/setup_en.md).

## Running from source

- go to the main page for this.

## Known Issues

- Some spatulas do not unlock when the level's items were already received (e.g. JF01)
- Loading a non AP save file will lock the game in an infinite death loop and send all collected locations in that save
  file.
- Rarely items will be sent again when loading a save (because of a race condition). Just reloading the save should fix
  that.
- The BfBB Client becomes unresponsive when patching.
- Some Dependency creates ``laxtab.py`` and ``yacctab.py`` in the CWD. If you notice them you can just delete or ignore
  them.
