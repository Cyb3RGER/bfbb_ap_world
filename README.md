# BfBB AP world

Battle for Bikini Bottom [Archipelago](https://archipelago.gg/) world.
More info [here](https://github.com/Cyb3RGER/bfbb_ap_world/blob/main/docs/en_Battle%20for%20Bikini%20Bottom.md).

## Installation & Usage

See the [setup guide](https://github.com/Cyb3RGER/bfbb_ap_world/blob/main/docs/setup_en.md).

## Running from source

- Clone this repo with submodules into the worlds folder for your AP source.
- Install py_dolphin_memory_engine and pythonnet via pip:
    - ``pip install dolphin-memory-engine``
    - ``pip install pythonnet``

## Known Issues

- Some spatulas do not unlock when the level's items were already received (e.g. JF01)
- Loading a non AP save file will lock the game in an infinite death loop and send all collected locations in that save
  file.
- Rarely items will be sent again when loading a save (because of a race condition). Just reloading the save should fix
  that.
- The BfBB Client becomes unresponsive when patching.
- Some Dependency creates ``laxtab.py`` and ``yacctab.py`` in the CWD. If you notice them you can just delete or ignore
  them.
