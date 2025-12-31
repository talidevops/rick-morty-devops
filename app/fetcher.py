import requests

BASE_URL = "https://rickandmortyapi.com/api/character"


def fetch_characters():
    characters = []
    url = BASE_URL

    while url:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        for character in data["results"]:
            if (
                character["species"] == "Human"
                and character["status"] == "Alive"
                and character["origin"]["name"].startswith("Earth")
            ):
                characters.append({
                    "name": character["name"],
                    "location": character["location"]["name"],
                    "image": character["image"],
                })

        url = data["info"]["next"]

    return characters
