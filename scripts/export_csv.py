import csv
from app.fetcher import fetch_characters

def export_to_csv():
    print("📥 Fetching characters...")
    characters = fetch_characters()
    print(f"✅ Fetched {len(characters)} characters")

    print("💾 Writing CSV file...")
    with open("data/characters.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Name", "Location", "Image"])

        for character in characters:
            writer.writerow([
                character["name"],
                character["location"],
                character["image"],
            ])

    print("🎉 CSV file written successfully!")

if __name__ == "__main__":
    export_to_csv()

