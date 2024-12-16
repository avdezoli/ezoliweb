import requests # type: ignore
import re
import sys

url1 = sys.argv[1]

if sys.argv[2] == "1":
    url = "http://" + url1
if sys.argv[2] == "2":
    url = "https://" + url1

response = requests.get(url)

if response.status_code == 200:
    html_content = response.text

    input_elements = re.findall(r'<input[^>]*>', html_content)

    for input_tag in input_elements:
        print(input_tag)
else:
    print("Sayfa yüklenirken bir hata oluştu.")

