# JP: このファイルはDiscordLaunchMC-en（英語版）です。日本語を使用したい場合は、DiscordLaunchMCを使用してください。
# EN: This file is DiscordLaunchMC-en (English version). If you want to use Japanese, please use DiscordLaunchMC.
# DiscordLaunchMC: https://github.com/insane-catt/DiscordLaunchMC

# The settings section that was previously here has been moved to config.py.
from config import *


# Below is the code. Tweak it as needed.

import discord
from discord import app_commands
import subprocess
import sys

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@tree.command(name="hello", description="Hello, world!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f'Hello, {interaction.user.mention}!')


@tree.command(name="start", description="Start the server")
@app_commands.default_permissions(administrator=True)
async def start(interaction: discord.Interaction):
    if is_server_running():
        await interaction.response.send_message('Server is already up and running')
    else:
        start_server()
        await interaction.response.send_message('Starting the server. Please wait a moment')


@tree.command(name="setseed", description="Set the seed value of the world")
@app_commands.default_permissions(administrator=True)
@app_commands.describe(seed='seed value')
async def setseed(interaction: discord.Interaction, seed: str = None):
    if is_server_running():
        await interaction.response.send_message('The command cannot be executed because the server is running')
    else:
        search_text = "level-seed="
        replace_text = f"level-seed={seed}"
        if seed == None:
            replace_text = "level-seed="

        with open(f"{HOME_DIRECTORY}/{SERVER_PATH}/server.properties", 'r') as file:
            lines = file.readlines()

        with open(f"{HOME_DIRECTORY}/{SERVER_PATH}/server.properties", 'w') as file:
            for line in lines:
                if search_text in line:
                    line = replace_text + '\n'
                file.write(line)

        if seed == None:
            await interaction.response.send_message("Seed value changed to default (random)")
        else:
            await interaction.response.send_message(f"Seed value changed to [{seed}].")


@tree.command(name="setpvp", description="Change PVP settings")
@app_commands.default_permissions(administrator=True)
@app_commands.describe(on_or_off="ON or OFF")
@app_commands.choices(
    on_or_off=[
        discord.app_commands.Choice(name="ON",value="true"),
        discord.app_commands.Choice(name="OFF",value="false")
    ]
)
async def setpvp(interaction: discord.Interaction, on_or_off: str):
    if is_server_running():
        await interaction.response.send_message("The command cannot be executed because the server is running")
    else:
        search_text = "pvp="
        replace_text = f"pvp={on_or_off}"
        with open(f"{HOME_DIRECTORY}/{SERVER_PATH}/server.properties", 'r') as file:
            lines = file.readlines()

        with open(f"{HOME_DIRECTORY}/{SERVER_PATH}/server.properties", 'w') as file:
            for line in lines:
                if search_text in line:
                    line = replace_text + '\n'
                file.write(line)

        if on_or_off == "true":
            await interaction.response.send_message("PVP setting changed to **ON** .")
        else:
            await interaction.response.send_message("PVP setting changed to **OFF** .")



@tree.command(name="setdifficulty", description="Change game difficulty")
@app_commands.default_permissions(administrator=True)
@app_commands.describe(difficulty="difficulty")
@app_commands.choices(
    difficulty=[
        discord.app_commands.Choice(name="peaceful",value="peaceful"),
        discord.app_commands.Choice(name="easy",value="easy"),
        discord.app_commands.Choice(name="normal",value="normal"),
        discord.app_commands.Choice(name="hard",value="hard")
    ]
)
async def setdifficulty(interaction: discord.Interaction, difficulty: str):
    if is_server_running():
        await interaction.response.send_message("The command cannot be executed because the server is running")
    else:
        search_text = "difficulty="
        replace_text = f"difficulty={difficulty}"
        with open(f"{HOME_DIRECTORY}/{SERVER_PATH}/server.properties", 'r') as file:
            lines = file.readlines()

        with open(f"{HOME_DIRECTORY}/{SERVER_PATH}/server.properties", 'w') as file:
            for line in lines:
                if search_text in line:
                    line = replace_text + '\n'
                file.write(line)
        if difficulty == "peaceful":
            await interaction.response.send_message("Changed game difficulty to **peaceful** .")
        elif difficulty == "easy":
            await interaction.response.send_message("Changed game difficulty to **easy** .")
        elif difficulty == "normal":
            await interaction.response.send_message("Changed game difficulty to **normal** .")
        else:
            await interaction.response.send_message("Changed game difficulty to **hard** .")
        


@tree.command(
        name="changeworld", 
        description="Change the world to play in. A new world is created by entering a world name that does not exist."
        )
@app_commands.default_permissions(administrator=True)
@app_commands.describe(world='World Name')
async def changeworld(interaction: discord.Interaction, world: str):
    if is_server_running():
        await interaction.response.send_message('The command cannot be executed because the server is running')
    else:
        search_text = "level-name="
        replace_text = f"level-name={world}"

        with open(f"{HOME_DIRECTORY}/{SERVER_PATH}/server.properties", 'r') as file:
            lines = file.readlines()

        with open(f"{HOME_DIRECTORY}/{SERVER_PATH}/server.properties", 'w') as file:
            for line in lines:
                if search_text in line:
                    line = replace_text + '\n'
                file.write(line)

        await interaction.response.send_message(f"Changed world to **{world}** .")


@tree.command(name="logout", description="Log this bot out")
@app_commands.default_permissions(administrator=True)
async def exitbot(interaction: discord.Interaction):
    if is_server_running():
        await interaction.response.send_message('The server is running. To execute that command, please exit the server.')
    else:
        await interaction.response.send_message('Execute logout')
        print("The logout command has been executed.")
        sys.exit()


def is_server_running():
    process = subprocess.Popen(f"screen -ls {SCREEN_NAME}", stdout=subprocess.PIPE, shell=True)
    output, _ = process.communicate()
    return SCREEN_NAME in output.decode()

def start_server():
    subprocess.Popen(f"screen -dmS {SCREEN_NAME} java -Xmx{MAX_RAM}G -Xms{MIN_RAM}G -jar {JAR_FILE} nogui", shell=True)


@client.event
async def on_ready():
        await client.change_presence(activity=discord.Game(name="Minecraft"))
        await tree.sync()
        print("login complete")

client.run(TOKEN)