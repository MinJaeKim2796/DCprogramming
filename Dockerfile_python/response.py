#response.py
import requests
from bs4 import BeautifulSoup

print("HTTP RESPONSE TEST")
while True:
    url = input("Input TEST URL : ")
    print("Go to", url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("RESPONSE OK!")
        else :
            print("RESPONSE FAILURE... Status Code is ", response.status_code)
    except requests.exceptions.MissingSchema as err:
        print("Error : Invalid URL")
    cont = input("Do you want to continue? [Y/n] : ")
    if cont == 'Y' or cont == 'y' :
        continue
    elif cont == 'N' or cont == 'n' :
        print("EXIT...")
        break
    else :
        print("Wrong Input! Program End.")
        break
