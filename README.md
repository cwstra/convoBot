# convoBot

## Intro
This bot is made to emulate text conversations, mostly for the sake of GMs and the like.

## Prerequisites
This bot requires:
* Python 3
* discord.py (rewrite)

Python 3 is best installed by Googling it

discord.py can be installed after Python 3 by the following command line command:

```bash
python3 -m pip install -U discord.py
```

## Installing and Set Up
1. Download the git file
2. Make a copy of `settings.default.json` and rename it `settings.json`
3. Put your Discord bot's token into the corresponding part of `settings.json`
4. Enter your character's names into the `names` list of `settings.json`
5. Use a hexadecimal color selector (such as [color-hex](http://www.color-hex.com/)) to select colors codes for your characters. They'll look like this: `#9bb1ff`
6. Use a hexadecimal to decimal converter (such as [this one](https://www.binaryhexconverter.com/hex-to-decimal-converter)) to change the base to what `settings.json` expects, and put them in the `colors` list in the same order as the characters they correspond to.
7. Get URLs for the thumbnails you want to use for your characters, and insert them into the `images` list of `settings.json`
8. Get the channel ids for the channels you want to type into (the sources), and put them into the `sources` list. No channel should appear here more than once. [Enabling Developer Mode will help get the ids.](https://discordia.me/developer-mode)
9. Get the channel ids for the channels you want to output to (the destinations), and put them into the `destinations` list, corresponding to their sources in the `sources` list.
10. Run bot.py using Python 3 
