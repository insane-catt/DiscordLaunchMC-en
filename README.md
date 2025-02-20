# DiscordLaunchMC-en

## Important Notice
**This is an older version of DiscordLaunchMC. DiscordLaunchMC can now be changed to English in the settings. Therefore, DiscordLaunchMC-en, which was provided as an English version, is no longer supported. [You can use DiscordLaunchMC from this link.](https://github.com/insane-catt/DiscordLaunchMC)**<br>

# README (conventional version)
JP: これは英語版DiscordLaunchMCです。日本語を使用したい場合は https://github.com/insane-catt/DiscordLaunchMC をご利用ください。<br>
EN: A Discord bot that can start a Minecraft server with custom settings.
This English text was translated using Bing Chat. We do our best to ensure the quality of the translation, but just in case, please watch out for translation errors.
## Overview
- I thought it would be tedious to have to connect via SSH and edit the server.properties file every time I wanted to create a new world with different settings or change the server settings, so I decided to add a feature to the Discord bot that allows me to edit the server.properties file by typing simple commands on Discord.
- Also, in the previous script ([the article I wrote on Qiita](https://qiita.com/insane_catt/items/f8cc4053a65334a8c9c4)), anyone could use the /start command even if they didn't have administrator privileges, so I improved it so that only people with administrator privileges could execute it.
- And, to make it easy for anyone who sees this article to run it, I decided to **distribute it on GitHub**.
## Execution environment
### My operating environment
- Operating computer: Raspberry Pi 4 Model B (RAM 8GB, SD card 64GB)
- Minecraft server software used: Paper 1.20.1 (with **DiscordSRV** and GeyserMC (with floodgate) plugins installed)

### Required environment setup
- **Python3**: It's a Python-based bot, so obviously it's necessary.
- **discord.py**: A library required to run a Discord bot. Don't confuse it with Pycord or something. Enter the following command in the terminal and install it.
```shell
python3 -m pip install -U discord.py
```
- **Paper**: A lightweight, Spigot-based Java edition Minecraft server software that allows you to install **plugins**. On top of this, you can install DiscordSRV and GeyserMC, which are optional but allow cross-play with the integrated version, which I will explain next.
- **DiscordSRV**: A plugin that allows you to display server join logs and Minecraft server console on Discord. I use this console, so I don't have a command to stop the Minecraft server in my custom Discord bot. So, if you don't install DiscordSRV or use the official Minecraft server software (heavy, no plugins), you have to go through the hassle of connecting to screen via SSH and typing the stop command. I won't explain how to use DiscordSRV because it's long, but it's useful and famous so you should install it.
![SRV_1.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3530195/462ce4eb-3ff2-20f7-7e28-6db318c84b4c.png)
Figure 1: In addition to join logs, you can also display achievements and death messages.
![SRV_2.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3530195/507aceb4-f63b-e836-8b02-fb24a64245cd.png)
Figure 2: A console screen that allows you to directly enter commands on the Minecraft server.
You can also use commands like seed normally.
PaperLaunchBot is the bot I made this time.

- **screen**: A software that allows you to run a Minecraft server in the background and connect and disconnect from it freely. You can install it by running the following command in the terminal.
```shell
sudo apt install screen -y
```
## How to use
**It is assumed that you have already set up a Minecraft server with Paper.** First, do that, and then follow these steps.
1. Download the package from the Releases on the right side of the screen.
1. Move `DiscordLaunchMC.py` and `config.py` from the package to the directory where the server executable file is located, and open `config.py` with an editor.
1. Either modify the settings section as desired or set the directory structure to `/home/pi/minecraft/java/paper` and make the `paper` directory the folder where the server executable file is located.
4. Go to https://discord.com/developers/applications, log in, and click the New Application button. Give it a name, check the box, and create it.
1. On the left side of the screen, click on "Bot", then click the "Reset Token" button, confirm by clicking "Yes, do it!", and finally click the "Copy" button. Replace the **TOKEN** in `config.py` with this copied token.
6. Turn on all the toggle switches in Privileged Gateway Intents and click the Save changes button that appears at the bottom.
7. Click OAuth2 → URL Generator on the left side of the screen and check bot and applications.commands from a large number of checkboxes. Then, from another large number of checkboxes that appear below, click Administrator (meaning administrator) because it's too much trouble. (You may need to set each one individually for security reasons, but I think it's fine to be an administrator if you don't worry about being attacked or something. It's your own bot and you just have to keep your token from being leaked or told to anyone.)
8. Copy the GENERATED URL that appears at the bottom and open it in your browser to invite the bot to your Discord server.
9. Run it with the following command.
```shell
python3 DiscordLaunchMC-en.py
```

## List of available commands
### Commands that can be used at any time
- **/hello**: Replies with "Hello, [user who executed the command]!" This command can be used by anyone to check if the bot is working properly.
### Commands that can only be used by Discord server administrators when the server is stopped
- **/start**: A command to start the server.
- /changeworld: Change the world you play in. You need to enter the world name as an argument. Entering a non-existent world name will generate a new world.
- /setseed: Specify a seed value. If no argument is specified, it will use a random seed value.
- /setdifficulty: Change the game difficulty with an argument.
- /setpvp: Specify whether to turn PVP on or off with an argument.
- /logout: Stop the bot.

For other things like game mode (survival or creative or something), please enter them on SRV or something console or something while the server is running. **I will add features if I feel like it or if there are requests. Please comment.**

## Contact information in case of trouble
Twitter (X lol)<br>
https://twitter.com/insane_catt

Please DM me

## Version history
- v1.0.7-en: Updated README and revised comments
- v1.0.6-en: Moved simple settings to config.py
- v1.0.5-en: Updated README and separated the English version
- v1.0.4: Updated README
- v1.0.3: Updated README
- v1.0.2: Implemented /logout command
- v1.0.1: Slightly changed message when starting server
- v1.0.0