import requests
import sys
import random

def doRequest(url):
    try:
        response = requests.get(url)
        status_code = response.status_code
        text = response.text
        
        if 100 <= status_code < 400:
            print(f"URL: {url} | Статус: {status_code} | Ответ: {text}")
        else:
            print(f"URL: {url} | Ошибка: {status_code} | Ответ: {text}", file=sys.stderr)
            
        return response
    except requests.exceptions.RequestException as e:
        print(f"URL: {url} | Ошибка соединения: {str(e)}", file=sys.stderr)

def main():

    urls = [f"https://httpstat.us/{random.randint(100,599)}" for i in range(5)]
    
    for url in urls:
        doRequest(url)
        
if __name__ == "__main__":
    main()