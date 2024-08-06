import json
import requests

url = "http://127.0.0.1:8001/api/v1/productlist_index/"  

response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # JSON

    # Сохранение в файл
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print("Данные успешно сохранены в файл data.json")
else:
    print("Ошибка при запросе к API")
