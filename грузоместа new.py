import pandas as pd
import requests

# чтение Excel
# создание ГМ
# сбор id созданных ГМ по 10 адресам доставки
# финальная статистика
# Можно брать и запускать, меняя только путь, URL и токен.


EXCEL_PATH = r"C:\Users\user\Desktop\список грузомест.xlsx"
API_URL = "https://api.vezubr.com/v1/api/cargo-place/update"

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3NzAyMTc4NzEsImV4cCI6MTc3MzgxNzg3MSwidXNlcm5hbWUiOiI3MDlkNzE3NDk2YmJjZWRiMDZmMGRiNmM2MmRhN2M4NmMzNTBlNzM3MjBiMjZlNzgzNTQ1ZTdiYzRhZGY2YTcxIiwiY29udHJhY3RvcklkIjozODQwLCJjb250cmFjdG9yS2V5IjoiOTFhNzU3ZWMiLCJpZCI6MTI2MDAsInVzZXJJZCI6MTMxNTcsInVzZXJLZXkiOiJkOWUyOWMyMCIsImNlbnRyaWZ1Z29Ub2tlbiI6ImV5SjBlWEFpT2lKS1YxUWlMQ0poYkdjaU9pSklVekkxTmlKOS5leUp6ZFdJaU9pSXhNall3TUNJc0ltVjRjQ0k2TVRjM01ETXdOREkzTVN3aWFXNW1ieUk2ZXlKMWMyVnlibUZ0WlNJNmJuVnNiSDE5LjRGUlpSMEpBbUtiUkpORnRXSnY1QmZZQi1jTERWZ0lnc05JY09HVGFBTzgiLCJoZWxwRGVza0VkZHlUb2tlbiI6ImV5SjBlWEFpT2lKS1YxUWlMQ0poYkdjaU9pSklVekkxTmlKOS5leUpwWVhRaU9qRTNOekF5TVRjNE56RXNJbXAwYVNJNklqUTFORE13WldFM0xUSXpNRFV0TkRBM05TMWhOR0l5TFdNeFpqZzVPR05sTURSa09DSXNJbVZ0WVdsc0lqb2liMjl0YjI1bGRHdGhRSFpwY21kcGJHbGhiaTVqYjIwaUxDSnVZVzFsSWpvaVhIVXdORFF5WEhVd05ETTFYSFV3TkRReFhIVXdORFF5WEhVd05ETmxYSFV3TkRNeVhIVXdORFJpWEhVd05ETTVJRngxTURReFpWeDFNRFF4WlZ4MU1EUXhaU0JjZFRBME1XTmNkVEEwTVdWY2RUQTBNV1JjZFRBME1UVmNkVEEwTWpKY2RUQTBNV0ZjZFRBME1UQWlMQ0p2Y21kaGJtbDZZWFJwYjI0aU9pSmNkVEEwTVdWY2RUQTBNV1ZjZFRBME1XVWdYQ0pjZFRBME1XTmNkVEEwTVdWY2RUQTBNV1JjZFRBME1UVmNkVEEwTWpKY2RUQTBNV0ZjZFRBME1UQmNJaUlzSW5Cb2IyNWxJanB1ZFd4c2ZRLmxrMENTR1Z1UHdydHl1Si13ajJPM2RFMUNYUjFiTlExeFBuX0Y3c2N3dEkiLCJlbXBsb3llZVJvbGVzIjpbMTMsMV19.nB1YIjG1CWmm7mSb4crxp3YVCDkTCQgUee5ryVos0P1bYou_H7sF8i8Begi2puaiPLpcOK7GPVx6ivufLX2frMnOMfkg3Nq53ngG0SCTkJb11RXljMdfHKlUFoIJt2prPaJ1p1Rjpk4nkE9EWAb3jfMcf1VCdq4UkdwNrvXIvMG6jUiDwdUMkK-KowwSsWQYf5DfIr1tRV0iJuOgO1YkAe3fMEJiwnCxJGeESmXglvgAwqly119dFZt5guOH1tk1jnb20b71XVsKqn98fXWzcha34u8hOAhyMZFuLVYZZ4WHn5ud_UR7fYOvZfxvlt2l0WzO73IgdV62af6f1aQ7hL98Lp9spTr35uniRmTAu0kv5y5e_dbUrgZjh96V6xANk3N9fUoEDZ4jtnjF5msYyE6d-6mgqr7ekvBLSxLX9g4F_5wv-EbxKVFG7ZBuijtX6jyrCBGnFEEYSjRitzzwYCECkLzu7udZNP4AXOOU_hbUzlw8pEngvRQqht9QyrYd9WMCRYBMit9eJe2AIxzEM-teEy5NDBqN6R7rUuGD6iMVY5ErTXJgr1LhbKsgwBVObYnPdKREK8MsKvN-AtgdafwQL03K64cD59LmctfqOLn7DCVGL96gDETNajOfQRoqVFr0uT0_hdinNw_wSVOMnGjMSt2-Jwwt36E-luscnT8"
}

DELIVERY_ADDRESSES = [
    28325,
    28326,
    28327,
    28328,
    28329,
    28330,
    28331,
    28332,
    28333,
    28334,
]

# считываем excel
df = pd.read_excel(EXCEL_PATH)

# хранилище id
created_ids_by_address = {
    address: [] for address in DELIVERY_ADDRESSES
}

# идём по строкам
for index, row in df.iterrows():

    delivery_address = int(row["№ адреса доставки п/п"])

    payload = {
        "barCode": str(row["Баркод"]),
        "title": str(row["Название груза"]),
        "weight": int(row["Вес,кг"]),
        "volume": int(row["Объем,м3"]),

        "departureAddress": 28336,
        "deliveryAddress": delivery_address,

        "feacnCode": str(row["ID товароносителя"]),
        "invoiceNumber": str(row["№ ГМ п/п"]),

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
            cargo_place_id = response.json().get("id")

            if cargo_place_id:
                created_ids_by_address[delivery_address].append(cargo_place_id)
                print(
                    f"✅ ГМ создано | id={cargo_place_id} "
                    f"| deliveryAddress={delivery_address}"
                )
            else:
                print(
                    f"⚠️ Успех без id | barcode={row['Баркод']} "
                    f"| ответ={response.json()}"
                )
        else:
            print(
                f"❌ Ошибка создания ГМ | barcode={row['Баркод']} "
                f"| {response.status_code} {response.text}"
            )

    except Exception as e:
        print(
            f"💥 Исключение | barcode={row['Баркод']} | {e}"
        )


print("\n========== ИТОГ ==========")

total_created = 0

for address, ids in created_ids_by_address.items():
    print(f"Адрес доставки {address}: {len(ids)} ГМ")
    total_created += len(ids)

print(f"\nВсего создано ГМ: {total_created}")
print("\nID по адресам:")
print(created_ids_by_address)



