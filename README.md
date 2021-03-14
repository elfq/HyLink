# HyLink
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
A Hypixel Verification bot.

### Usage

To use this bot, use the `verify` command in a channel, once you've entered it you should recieve a message from the bot
with instructions on how to link your Hypixel account with a discord server.

Once you're verified, you will be given a role called "Verified", and your server nickname will be changed to your Minecraft IGN.

# Installation

**`1)`**
Download the source code of this repository, and navigate to the `Hylink` folder and create a file called `.env`.

Inside this file make sure to add the following content:
```
TOKEN=
API_KEY=
```
For the `TOKEN=` part, you'll add your bot token.
For the `API_KEY=` part, you'll add your Hypixel API key. 
*to get your API Key, open up Hypixel, and type /api key in chat and copy & paste it*

Once you're done configuring .env, open the directory inside a command prompt, and enter the following commands.

```
pip install -r requirements.txt
```

```
python bot.py
```

Congratulations! You've successfully setup the bot.

**`2)`**
Once your bot is online, make sure to give it permissions to change nicknames, and add roles. After you've done that, create a role called `Verified`.

## Attributions
This bot is heavily inspired by the verification bot in SkyBlockZ
discord.gg/skyblock
