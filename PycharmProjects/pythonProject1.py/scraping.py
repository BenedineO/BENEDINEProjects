import requests
import Bs4 from BeautifulSoup
url = "https://www.techrevoluxe.com/"
response = requests.get(url)
if response.status_code ==200:
    print("Gotcha!")
else:
    print("Nope!")

print(response.links)

