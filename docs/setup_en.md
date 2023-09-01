# Battle for Bikini Bottom Setup Guide

## Required Software

- [Archipelago](https://github.com/ArchipelagoMW/Archipelago/releases) v0.4.1 or higher. Make sure to install the
  Generator.
- [This AP world](https://github.com/Cyb3RGER/bfbb_ap_world/releases)
- Microsoft .NET Framework 4.8 or higher
- [Dolphin](https://dolphin-emu.org/download/)
- Your US Version of Battle for Bikini Bottom, probably
  named ``Nickelodeon SpongeBob SquarePants - Battle for Bikini Bottom (USA).iso``.

## Installation Procedures

- Place ``bfbb.apworld`` in ``lib/worlds/`` of your AP installation.
- Place the included ``.pyd`` files and the ``dolphin_memory_engine`` folder into ``lib/`` of your AP installation.
- Place the ISO in the root folder of your AP installation and make sure it's
  named ``Nickelodeon SpongeBob SquarePants - Battle for Bikini Bottom (USA).iso``.

For more information about .apworlds
see [here](https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/apworld%20specification.md)

## Create a Config (.yaml) File

### What is a config file and why do I need one?

See the guide on setting up a basic YAML at the Archipelago setup
guide: [Basic Multiworld Setup Guide](https://archipelago.gg/tutorial/Archipelago/setup/en)

### Where do I get a config file?

A default yaml is included in the download. Alternative you can use the Web Host when running from source.

### Verifying your config file

If you would like to validate your config file to make sure it works, you may do so on the YAML Validator page. YAML
validator page: [YAML Validation page](https://archipelago.gg/mysterycheck)

## Joining a MultiWorld Game

Start ``ArchipelagoLauncher.exe`` and choose ``BfBB Client``. You will be asked to provide a ``.apbfbb`` patch file so
choose your patch file. The client will then open, patch and attempt to open the resulting ``.gcm`` ISO file. Patching
can take a while and the client will become unresponsive while patching. You can also select a ``.gcm`` directly to just
open it without patching or just click cancel, if you don't want to patch or open any ISO.

### Connect to the Client

#### With Dolphin

The Client will automatically try to connect to Dolphin every 5 seconds and will do so if BfBB is running. If this
doesn't work try restarting Dolphin and make sure you only have one instance running of Dolphin. If you still get the
invalid game error message when using the US Version make sure that ``Emulated Memory Size Override`` (
under ``Settings`` > ``Advanced``) is disabled.

### Connect to the Archipelago Server

If the client window shows "Server Status: Not Connected", simply ask the host for the address of the server, and
copy/paste it into the "Server" input field then press enter.

The client will attempt to reconnect to the new server address, and should momentarily show "Server Status: Connected".

## Hosting a MultiWorld game

The recommended way to host a game is to use the Archipelago hosting service. The process is relatively simple:

1. Collect config files from your players.
2. Place the config files in the ``Players`` folder in your Archipelago install
3. Run ``ArchipelagoGenerate.exe`` and location the resulting zip in the ``output`` folder
4. Upload that zip file to the Host Game page.
    - Generate page: [WebHost Host Game Page](https://archipelago.gg/uploads)
5. Click "Create New Room". This will take you to the server page. Provide the link to this page to your players, so
   they may download their patch files from there.
6. Note that a link to a MultiWorld Tracker is at the top of the room page. The tracker shows the progress of all
   players in the game. Any observers may also be given the link to this page.
7. Once all players have joined, you may begin playing.
