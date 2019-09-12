import urllib.request
from bs4 import BeautifulSoup

base_url = "https://www.oakhouse.jp/house/970"

req = urllib.request.Request(base_url)
with urllib.request.urlopen(req) as res:
    body = res.read()
    sorp = BeautifulSoup(body, "html.parser")

    # これが空室
    # tab_room_all > div:nth-child(1) > div.bukkeninfo_box03.bukken_heightlines > table > tbody > tr:nth-child(1) > td
    # これが満室
    # tab_room_enp > div:nth-child(1) > div.bukkeninfo_box03.bukken_heightlines > table > tbody > tr:nth-child(1) > td

    tab_room_all = sorp.find(id="tab_room_all")
    bukken_heightlines = tab_room_all.find_all("div", attrs={"class", "bukkeninfo_box03"})
    for line in bukken_heightlines:
        num = line.select("table > tr:nth-of-type(1) > td")
        print(num)
