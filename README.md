# TheBigBot
Experimental Beta v2.1

made by coolfav on Github

# Requirements if you want to use this source code for your own bot:

- Python 3.8 interpreter (could possibly work with 3.7 or below)

- PIP

- Discord.py[voice] (py -3 -m pip install -U discord.py[voice])

- Youtube-dl (pip install youtube-dl)

- Wikipedia ((pip install wikipedia)

- google (pip install google)

- google-images-search (pip install Google-Images-Search)

# Instructions:

1. Create a file called "token.txt" in the working/main directory (where mainbot.py is) containing ONLY the token of your discord bot (you can make one at https://discord.com/developers/applications)
2. Make a project at https://console.developers.google.com/apis/dashboard
3. Enable Custom Search API from https://console.developers.google.com/apis/library/customsearch.googleapis.com?q=search&id=4b0c5e50-0a7a-46cc-84f4-5aabeaebf6f2
4. Create an API Key from the credentials tab for your project. Create a "apikey.txt" file in the main/wokring directory containing ONLY the API key that you generated from your project.
5. Visit https://cse.google.com/cse/all and in the web form where you create/edit your custom search engine enable "Image search" option and for "Sites to search" option select "Search the entire web". Then copy the CX key after "https://cse.google.com/cse?cx=" in your custom search engine's public URL, and paste this into a new file "cx.txt" in the working/main directory.
6. Run mainbot.py
7. As long as your file is running, the bot should work as intended (as long as there aren't any bugs)

# Commands:

Voice:

/join - connects the bot to your voice channel

/leave - forces the bot to leave the channel it's in

/play /p - accepts a URL or keywords as an argument to search for a youtube video and to play it. Joins the voice channel if not already in it.

/pause - pauses or unpauses the current playing song

/queue /que /q - queues a song up that will automatically play after the current playing song is done, accepts same arguments as /play

/skip - skips the current song and jumps to the next in queue, or stops the song if there aren't any more songs in queue

/reset - stops the currently playing song and clears the queue

/volmue [1-100] - Sets the volume to a percentage out of 100

Google:

/wikipedialink /wikilink /wl /wikil /wikipedial /wlink [search terms] - provides a link to a wikipedia/fandom/etc. webpage that matches the search term

/googleimages /googleimage /googlei /gimages /gi [number of images] [search terms] - sends a number of the top images from Google images to the channel which the command was inputted in

Wikipedia:

/wikipedia /wiki /w [search terms] - provides a link and a 3 sentence description from the wikipedia/fandom/etc. webpage for the article that matches the search term

Miscellaneous:

/roll /r [ndn] - rolls a dice in the ndn format (e.g. 3d6, would roll 3 6-sided dice)

/math [add or +, subtract or -, multiply or * or x, divide or /] [numbers] - Does simple math using the 4 basic operators

# Known bugs:

- Sometimes a win-5 error will show up that doesn't allow the program to create the directory './Images' when using /googleimage. Just retry the commands and theoretically it should work. If the problem persists, restart the program. If everything else fails and you keep getting this error, please submit an issue request or contact me directly on discord, coolfav#3825.

- Sometimes the /wikipedia function provides a link that isn't from a wikipedia/fandom/etc page. I will probably fix this soon.

- When using /googleimage, the number of photos sent can differ from the number that has been inputted. I don't know why this occurs and it's strange. I hope to find a fix in the near future.

- With voice commands, sometimes the bot has trouble doing /play when it's already in a voice channel. Simply make it leave with /leave, then use /play again. It will automatically join and start playing the song once it's loaded.



This code is open source, anyone is free to modify and redistribute it, but it would be nice to be credited for it.
