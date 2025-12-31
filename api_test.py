import requests
import json
from datetime import datetime


def main():
    url = "http://localhost:8000/contacts"
    current_datetime = datetime.now().isoformat()
    body = {
        "id": 1,
        "name": "山田太郎",
        "email": "taro@example.com",
        "url": "http://example.com",
        "gender": 1,
        "massage": "こんにちは",
        "is_enabled": True,
        "created_at": current_datetime
    }

    res = requests.post(url, data=json.dumps(body))
    print(res.json())

# このファイルを直接実行した場合に main() を呼び出す
if __name__ == "__main__":
    main()