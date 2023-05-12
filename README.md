# BfBB AP world

Battle for Bikini Bottom [Archipelago](https://archipelago.gg/) world

## Running from source

Clone this repo with submodules into the worlds folder for your AP source.
Install py_dolphin_memory_engine and pythonnet via pip:
  - pip install dolphin-memory-engine
  - pip install pythonnet

## Installation

Place the .apworld in ``/lib/worlds/`` in your AP installation.
Place the .pyd files in ``/lib/`` in your AP installation.

## Usage

Use the included example yaml to configure your game.
Use the Archipelago Launcher to start the BfBB Client and use the BfBB Client to load your ``.apbfbb`` file.

## Known Issues

- Some spatulas do not unlock when the level's items were already received (e.g. JF01)
- Loading a non AP save file will lock the game in an infinite death loop and send all collected locations in that save file
