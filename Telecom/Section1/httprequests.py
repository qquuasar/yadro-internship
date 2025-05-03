import requests
import sys
import random


def doRequest(url):
    try:
        response = requests.get(url)
        status_code = response.status_code
        text = response.text
        if (status_code>=100) and (status_code < 400):
            
            print(f"Статус код: {status_code}, Тело ответа: {text}")

        elif (status_code>=400) and (status_code<600):
            if status_code==500: text = "Null code text"
            raise Exception(f"Ошибка, статус код ошибки: {status_code}, Тело ответа: {text}")

        return response 
    except requests.exceptions.RequestException as exc:
        raise Exception(f"Ошибка запроса: {str(exc)}")
    

def main():
    urls = []
    for i in range(5):
        appendCode = random.randint(100,599)
        urls.append(f"https://httpstat.us/{appendCode}")

    for url in urls:
        try:
            print(f"Запрос: {url}")
            doRequest(url)
        except Exception as exc:
            print(exc, file=sys.stderr)

if __name__ == "__main__":
    main()