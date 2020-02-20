from bs4 import BeautifulSoup
import json

f = open("app_ranking_list.json", "r")

soup = json.load(f)

f.close()

print(soup)