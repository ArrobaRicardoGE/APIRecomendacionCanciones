from PIL import Image, ImageDraw, ImageFont
import textwrap


def create(name, artists, uuid):
    """Crea la imagen para mostrar la recomendación"""

    # Creamos una imagen para usar de fondo
    img = Image.new("RGB", (1280, 640), color="black")
    # Cargamos la tipografía a utilizar en nuestra imagen
    font = ImageFont.truetype("assets/Roboto-Bold.ttf", 70)
    # Creamos el objeto auxiliar que nos dejará escribir sobre nuestra imagen
    d = ImageDraw.Draw(img)

    # Partimos nuestro título en líneas para poder visualizarlo completo en
    # la imagen
    wp = textwrap.wrap(name, 16)
    current_h, pad = 100, 10
    # Escribimos el título línea por linea
    for line in wp:
        w, h = d.textsize(line, font=font)
        d.text((640 + (640 - w) / 2, current_h), line, font=font)
        current_h += h + pad

    # Volvemos a cargar la tipografía, con un tamaño menor
    font = ImageFont.truetype("assets/Roboto-Bold.ttf", 40)
    current_h += 80
    # Escribimos el nombre de cada artista
    for artist in artists:
        w, h = d.textsize(artist, font=font)
        d.text((640 + (640 - w) / 2, current_h), artist, font=font)
        current_h += h + pad

    # Incluimos la portada del album en la imagen
    cover = Image.open(f"covers/{uuid}.png")
    cover.resize((640, 640))
    img.paste(cover, (0, 0))

    # Guardamos la imagen en el disco
    img.save(f"results/{uuid}.png")
