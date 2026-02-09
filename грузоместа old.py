import pandas as pd
import requests

EXCEL_PATH = r"C:\Users\user\Desktop\список грузомест.xlsx"
API_URL = "https://your-host/v1/api/cargo-place/update"

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_TOKEN"
}

# считываем excel
df = pd.read_excel(EXCEL_PATH)

created_id = [] # сюда сложим id созданных ГМ

# идём по строкам
for index, row in df.iterrows():
    payload = {
        "barCode": str(row["Баркод"]),
        "title": str(row["Название груза"]),
        "weight": float(row["Вес,кг"]),
        "volume": float(row["Объем,м3"]),

        "departureAddress": 28336,
        "deliveryAddress": int(row["№ адреса доставки п/п"]),

        "feacnCode": int(row["ID товароносителя"]),
        "invoiceNumber": int(row["№ ГМ п/п"]),

        "comment": None,

        "category": None,
        "quantity": None,
        "length": None,
        "width": None,
        "height": None,
        "cost": None,
        "totalCost": None,
        "type": "box",
        "status": "new"
    }

    try:
        response = requests.post(API_URL, json=payload, headers=HEADERS)

        if response.status_code == 200:
            response_json = response.json()
            cargo_place_id = response_json.get("id")

            if cargo_place_id:
                created_id.append(cargo_place_id)
                print(f"✅ ГМ создано, id = {cargo_place_id}")
            else:
                print(f"⚠️ Успех, но id не найден в ответе: {response_json}")

        else:
            print(
                f"❌ Ошибка создания ГМ (barcode={row['Баркод']}): "
                f"{response.status_code} {response.text}"
            )

    except Exception as e:
        print(f"💥 Исключение при создании ГМ (barcode={row['Баркод']}): {e}")

# --------------- финальный отчёт ---------------
print("\n====== РЕЗУЛЬТАТ ======")
print(f"Создано грузомест: {len(created_id)}")
print(f"Список id: {created_id}")
