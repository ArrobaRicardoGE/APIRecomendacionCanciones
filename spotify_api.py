import requests, random

# Constantes
TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
BASE_URL = "https://api.spotify.com/v1/search"


def get_wildcard():
    """Produce un comodín válido para realizar una selección semialeatoria
    de una canción.
    """

    return random.choice(
        [
            "%25a%25",
            "a%25",
            "%25a",
            "%25e%25",
            "e%25",
            "%25e",
            "%25i%25",
            "i%25",
            "%25i",
            "%25o%25",
            "o%25",
            "%25o",
            "%25u%25",
            "u%25",
            "%25u",
        ]
    )


def get_track():
    """Selecciona una canción aleatoria y devuelve el título, nombre de los
    artistas y url de la imagen del álbum
    """

    r = requests.get(
        f"{BASE_URL}?q={get_wildcard()}&type=track&offset={random.randint(1, 1000)}&limit=1",
        headers={"Authorization": f"Bearer {TOKEN}"},
    )
    r_json = r.json()
    name = r_json["tracks"]["items"][0]["name"]
    img_url = r_json["tracks"]["items"][0]["album"]["images"][0]["url"]
    artists = [i["name"] for i in r_json["tracks"]["items"][0]["album"]["artists"]]
    return name, artists, img_url


def download_image(img_url, uuid):
    """Dada una url y el uuid, descarga la imagen y la guarda en disco"""

    data = requests.get(img_url).content
    with open(f"covers/{uuid}.png", "wb") as f:
        f.write(data)
