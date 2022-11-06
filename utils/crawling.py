from bs4 import BeautifulSoup
import requests

page = requests.get("https://listofdeaths.fandom.com/wiki/Main_characters")
soup = BeautifulSoup(page.text, "html.parser")

elements = soup.select("h2")

print ("deadList={")
for element in elements:
    if element.text in ["Contents",'Superstore', "Kindergarten:", "Star Wars"]:
        continue

    if len(element.text.strip()) == 0:
        continue

    h2Tag = soup.find("h2", text=element.text)
    try:
        ulTag = h2Tag.find_next("ul")
    except AttributeError:
        continue



    print(f"\"{element.text}\": [")


    for child in ulTag.findChildren('li'):
        name = child.text.split('-')[0].strip().replace('"', R'\"')

        print(f"\"{name}\",")

    print("],")


print("}")