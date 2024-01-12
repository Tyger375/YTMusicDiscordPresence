# YT Music Discord Presence

## Edge extension set up

First, add the extension folder to your browser's extensions.

## Server set up

Edit the `headers_auth.json` file and change the "cookie" value to your youtube music's cookies, you can get them from any request made by the website.
Edit the client_id variable in `server.py` and set it as your discord app's id

Download and run the `server.py` file <br>
<br>
packages required: <br>
- flask
- flask-cors
- ytmusicapi
- pypresence
- nest-asyncio
<br>
To show the discord presence, the server must be always on.
