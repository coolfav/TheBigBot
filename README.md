# TheBigBot

made by coolfav on Github

Requirements if you want to use this source code for your own bot:

-Any python IDE

-Discord.py[voice]

-Youtube-dl

Instructions:

1. Change all of the directory locations in the code to the directory where you placed the files you downloaded or equivalent (you will need to pay attention a little for this)
2. Replace the "token" at the bottom of mainbot.py with the token of your discord bot (you can make one at https://discord.com/developers/applications)
3. Run the python file
4. As long as your file is running, the bot should work as intended (as long as there aren't any bugs)

Commands:

/join - connects the bot to your voice channel

/leave - forces the bot to leave the channel it's in

/play /p - accepts a URL or keywords as an argument to search for a youtube video and to play it

/pause - pauses or unpauses the current playing song

/queue /que /q - queues a song up that will automatically play after the current playing song is done, accepts same arguments as /play

/skip - skips the current song and jumps to the next in queue, or stops the song if there aren't any more songs in queue

/reset - Stops the currently playing song and clears the queue

/volmue [1-100] - Sets the volume to a percentage out of 100
