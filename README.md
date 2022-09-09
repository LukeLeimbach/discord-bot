# discord-bot

This bot is created to have all my discord bots on a single bot.

## List of bots merged into this project:
    - Votekick Bot - Votekick's a user from the server.
        Utilizes these commands in a discord text channel:
            >>>votekick @<user>                     - opens a prompt to kick user
            >>>votetimelimit <number of minutes>    - sets the number of minutes until timeout
            >>>voteuserlimit <number of users>      - sets the number of users that are required to kick a user
            #NOT ADDED# >>>voteallowreconnect <True/False>      - determines if the user is sent an invite after being kicked
            #NOT ADDED# >>>voterestoreroles <True/False>        - determines if the user's roles are updated after being kicked
       
        Description:
            Upon completion of a vote, the user will be kicked and immediately sent an invitation
            to join the server again. Upon joining, the member will be given their roles back.
            If the user is not votekicked after the timeout period, nobody will be kicked.
            This is not meant for server moderation, just to mess with your friends.

        Bugs:
            - Only one member can be kicked at a time
            - If a user is kicked and another vote is started before they reconnect,
                the kicked user will recieve roles of the user currently being kicked.
            - If the bot is restarted while a user is being kicked, the kicked user's roles
                will not be updated.
            - Cannot kick users with roles higher than the bot's role.
    
    - #NOT MERGED# IntroBot - Plays a song when a user connects to to a voice channel
        Utilizes these commands in the #Song-Updating text channel:
            >>>intromute                            - toggles the bot's ability to connect to a vc
            >>>introtimelimit                       - sets the time limit on how long an intro can be

        Description:
            On connection to a new server, IntroBot creates a #Song-Updating text channel. In this channel, users can 
            upload sound clips that will automatically update their intro sound effect.

        Bugs:
            - We will see; I'm sure they are plentiful.
        
## Invite to your server

The bot currently only works on my server with my channels.

If you would like to optimize it for your own server or for servers in general, pull requests 
are welcome. I'll just make a new branch for the optimized version if I actually receive a 
request.

## Usage

If you want to modify the files locally and have this bot on your server,
you can clone this repository and push it to a Heroku server. Make sure to add your own
bot token.

## Creator

My name is Luke. I'm a Computer Science student at University of Montana. I like to make
these bots for fun, so don't take them seriously. 

## License

None. Go crazy and also go stupid.