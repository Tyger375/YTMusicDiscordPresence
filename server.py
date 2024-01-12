import nest_asyncio

nest_asyncio.apply()

import asyncio
from flask import Flask, request
from flask_cors import CORS, cross_origin
from ytmusicapi import YTMusic
from pypresence import Presence

client_id = ""
RPC = Presence(client_id=client_id)
RPC.connect()

ytmusic = YTMusic("headers_auth.json", user="")

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

stopped = True


async def nextSong():
    await asyncio.sleep(2.5)
    try:
        updatePresence()
    except Exception as e:
        print(e)


def updatePresence():
    global stopped
    stopped = False
    song = ytmusic.get_history()[0]
    img = song["thumbnails"][0]["url"]
    print(song)

    RPC.update(
        buttons=[{"label": "Listen", "url": f"https://youtube.com/watch?v={song['videoId']}"}],
        details=f"Listening to {song['title']}",
        state=f"by {', '.join([artist['name'] for artist in song['artists']])}",
        large_image=img
    )


@app.route("/", methods=["POST"])
@cross_origin()
def main():
    asyncio.run(nextSong())
    return "Presence updated"


@app.route("/pause", methods=["POST"])
@cross_origin()
def pause():
    global stopped
    stopped = True
    try:
        RPC.clear()
    except Exception as e:
        print(e)
    return "Presence updated"


@app.route("/resume", methods=["POST"])
@cross_origin()
def resume():
    updatePresence()
    return "Presence updated"


if __name__ == "__main__":
    app.run(debug=True)
