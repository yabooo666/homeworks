import json
import os
import time
from concurrent.futures import ThreadPoolExecutor
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/photos"
session = requests.Session()


# ფუნქცია, რომელიც იღებს photo_id-ს და აბრუნებს მის JSON მონაცემს
def fetch_photo(photo_id):
    try:
        response = session.get(f"{BASE_URL}/{photo_id}", timeout=10)
        return response.json()
    except Exception as e:
        return {"id": photo_id, "error": str(e)}


def main():
    start_time = time.time()
    print("ფოტოების წამოღება მიმდინარეობს (5000 მოთხოვნა)...")

    # ThreadPoolExecutor ინარჩუნებს თანმიმდევრობას (1-დან 5000-მდე)
    with ThreadPoolExecutor(max_workers=50) as executor:
        photos = list(executor.map(fetch_photo, range(1, 5001)))

    output_path = os.path.join(os.path.dirname(__file__), "photos.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(photos, f, indent=4)

    total_time = time.time() - start_time
    print(f"წარმატებით ჩაიწერა {len(photos)} ფოტო photos.json-ში!")
    print(f"მთლიანი შესრულების დრო: {total_time:.2f} წამი")


if __name__ == "__main__":
    main()
