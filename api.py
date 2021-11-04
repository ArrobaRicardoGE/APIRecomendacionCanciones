from flask.helpers import send_from_directory
import image_creator, spotify_api, uuid
from flask import Flask

app = Flask(__name__)

BASE_URL = "http://127.0.0.1:5000"


@app.route("/v1/recommend")
def image():
    """Endpoint para acceder a las recomendaciones"""

    ruuid = uuid.uuid1()
    name, artists, img_url = spotify_api.get_track()
    spotify_api.download_image(img_url, ruuid)
    image_creator.create(name, artists, ruuid)
    return {"name": name, "artists": artists, "url": f"{BASE_URL}/results/{ruuid}.png"}


@app.route("/results/<filename>")
def result(filename):
    """Endpoint para visualizar la imagen resultante"""

    return send_from_directory("results", filename)


if __name__ == "__main__":
    app.run()
