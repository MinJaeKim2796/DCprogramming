#response.py
import requests
from bs4 import BeautifulSoup

url = "http://swcon.khu.ac.kr"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
item = soup.select_one("head > title").string
print("Go to", url)
print("Status Code :", response.status_code)
if response.status_code == 200:
    print("RESPONSE OK!")
    print("Department :", item)
else :
    print("RESPONSE FAILURE...")
