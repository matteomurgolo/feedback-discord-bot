import os
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from datetime import datetime, timedelta
import textwrap

def generate_message_image(message):
    # Couleurs Twitter mode sombre
    background_color = (21, 32, 43)  # Bleu foncé
    text_color = (255, 255, 255)  # Blanc
    secondary_color = (136, 153, 166)  # Gris clair

    # Dimensions de l'image
    width = 600
    min_height = 200
    padding = 20
    avatar_size = 60

    # Chargement des polices
    font_path = os.path.join('assets', 'fonts', 'arial.ttf')
    name_font = ImageFont.truetype(font_path, 20)
    username_font = ImageFont.truetype(font_path, 16)
    content_font = ImageFont.truetype(font_path, 18)
    date_font = ImageFont.truetype(font_path, 14)

    # Calcul de la largeur maximale pour le contenu
    max_content_width = width - (2 * padding)

    # Fonction pour wrapper le texte manuellement
    def wrap_text(text, font, max_width):
        words = text.split()
        lines = []
        current_line = []
        current_width = 0
        for word in words:
            word_width = font.getlength(word)
            if current_width + word_width <= max_width:
                current_line.append(word)
                current_width += word_width + font.getlength(' ')
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
                current_width = word_width
        lines.append(' '.join(current_line))
        return lines

    # Wrapping du texte
    wrapped_text = wrap_text(message.content, content_font, max_content_width)
    content_height = len(wrapped_text) * content_font.getbbox('A')[3]
    
    # Ajout d'un espace pour la date
    date_height = date_font.getbbox('A')[3]
    extra_space = 20  # Espace supplémentaire entre le contenu et la date

    # Calcul de la hauteur totale de l'image
    height = max(min_height, 130 + content_height + date_height + extra_space + padding * 2)

    # Création de l'image
    img = Image.new('RGB', (width, height), color=background_color)
    d = ImageDraw.Draw(img)

    # Avatar
    avatar_url = message.author.display_avatar.url if message.author.avatar else message.author.default_avatar.url
    response = requests.get(avatar_url)
    avatar = Image.open(BytesIO(response.content))
    avatar = avatar.resize((avatar_size, avatar_size))
    avatar_mask = Image.new("L", avatar.size, 0)
    draw = ImageDraw.Draw(avatar_mask)
    draw.ellipse((0, 0, avatar_size, avatar_size), fill=255)
    img.paste(avatar, (padding, padding), avatar_mask)

    # Calcul de la position verticale centrée pour le nom et le @
    name_height = name_font.getbbox(message.author.name)[3]
    username_height = username_font.getbbox(f"@{message.author.name}")[3]
    total_text_height = name_height + username_height
    text_start_y = padding + (avatar_size - total_text_height) // 2

    # Nom d'utilisateur et @
    d.text((padding + avatar_size + 10, text_start_y), message.author.name, fill=text_color, font=name_font)
    d.text((padding + avatar_size + 10, text_start_y + name_height), f"@{message.author.name}", fill=secondary_color, font=username_font)

    # Contenu du message
    y_text = padding + avatar_size + 20
    for line in wrapped_text:
        d.text((padding, y_text), line, fill=text_color, font=content_font)
        y_text += content_font.getbbox(line)[3]

    # Date
    timestamp = message.created_at + timedelta(hours=2)  # Ajout de 2 heures
    date_str = timestamp.strftime("%H:%M · %d %b. %Y")
    d.text((padding, height - padding - date_height), date_str, fill=secondary_color, font=date_font)

    output_path = 'discord_message.png'
    img.save(output_path)
    return output_path
