# HyLink
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
