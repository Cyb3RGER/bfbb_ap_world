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

- Place ``bfbb.apworld`` in ``custom_worlds`` of your AP installation.
- Place the included files from the ``lib/`` folder into ``lib/`` of your AP installation.

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

Start ``ArchipelagoLauncher.exe`` and choose ``Open Patch``, and select your ``.apbfbb`` patch file.

When opening a BfBB patch file for first time, you will also be prompted to select your BfBB ISO file. The patching process can take a while and the client may become unresponsive, so please be patient.

After patching is complete, if you are using autostart (which is enabled by default), you will also be prompted to select your Dolphin executable.

Alternatively, you can select the ``BfBB Client`` directly from the Launcher. This will ask for one of the following:
- An ``.apbfbb`` file to patch and run the game.
- An already-patched ``.gcm`` file to run the game directly.

You can also select ``Cancel`` to open the client by itself without patching or launching a game.

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

## Troubleshooting

The setup for this AP world is rather complex, so here are some common issues encountered during setup and how to fix
them.

### I don't see the BfBB Client in the Launcher.

Make sure you have installed the AP world. It should be in the `custom_worlds` folder within your AP directory.

### I see the BfBB Client, but it doesn't open.

This is most likely due to `dolphin_memory_engine` not loading correctly.

1. Ensure you have placed all files from the included `lib` folder into the `lib` folder in your AP directory.
2. Verify that you are using the correct version for your AP installation, as described on the release page.

If you are unsure which AP version you are using:

- Run `ArchipelagoLauncherDebug.exe`.
- In the console that opens, the first line will display the AP version and the Python version being used. It will look
  something like this:

    ```plaintext
    Archipelago (0.5.1) logging initialized on [...] running Python 3.12.6 (frozen)
    ```

In this example, the Python version is 3.12. This should match the end of the file name of the downloaded release (e.g.,
`bfbb_apworld-vX_X_X-win_amd64-py3_12.zip`).

If the issue persists, try the following:

- Delete your `lib` folder.
- Reinstall AP.
- Follow the setup instructions again.

### The BfBB Client opens, but it's just a black window.

This is normal. The client becomes unresponsive while patching, which can take a while, especially the first time.

### I get an error during patching...

#### Error: `No module named [...]`

This means the client is missing a required Python library. The most common cause is that the additional libraries were not installed correctly.  

Double-check that you copied **all** files from the included `lib\` folder in the download into your Archipelago `lib\` folder. If anything is missing, reinstall them and try again.

#### Error: `Failed to resolve Python.Runtime.Loader.Initialize from [...]\lib\pythonnet\runtime\Python.Runtime.dll`

Windows may block this DLL included in the download. To fix this:

1. Navigate to `\lib\pythonnet\runtime\` in your AP directory.
2. Right-click on `Python.Runtime.dll` and select **Properties**.
3. Near the bottom of the Properties window, check for an option to **Unblock** the file and apply the change.

#### Error: `Permission denied '[...].gcm'`

This usually occurs when the patched file is already open in Dolphin or another program. Close all programs that might access the file and try again.

#### Error: `No such file or directory: '[...]\Nickelodeon SpongeBob SquarePants - Battle for Bikini Bottom (USA).iso'`

Ensure that you have placed the vanilla USA ISO in your root AP directory with the exact name:

```plaintext
Nickelodeon SpongeBob SquarePants - Battle for Bikini Bottom (USA).iso
```

If file name extensions are hidden in Windows Explorer:

1. Enable them temporarily under View in the menu.
2. Ensure the file does not have a double extension (e.g., ``.iso.iso``).

#### Error: `Failed to create a default .NET runtime [...]`

Ensure that Microsoft .NET Framework 4.8 or higher is installed.

This error may also occur if the libraries were not installed correctly. To verify the installation, follow all the steps outlined [here](#i-see-the-bfbb-client-but-it-doesnt-open).

Additionally, ensure that none of the dlls in ``lib\clr_loader\ffi\dlls`` are blocked:

1. Right-click on the dll and select **Properties**.
2. Near the bottom of the Properties window, check for an option to **Unblock** the file and apply the change.

If the issue persists, consider uninstalling older versions of the .NET Framework. **NOTE**: Uninstalling older versions may prevent other programs that depend on them from working correctly.
