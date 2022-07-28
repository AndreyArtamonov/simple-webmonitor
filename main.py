import hashlib

import requests
from lxml import html
from fake_useragent import UserAgent
import sqlite3

headers = {'user-agent': UserAgent().chrome}
db = sqlite3.connect('database.sqlite3')


def getMD5onPage(url, xpath):
    page = html.fromstring(url.text).xpath(xpath)
    str = ''.join(page).encode()

    return hashlib.md5(str).hexdigest()


def updateMD5():
    if md5 != site[1]:
        try:
            db.execute("""UPDATE sites SET hash=? WHERE url=?""", (md5, site[0]))
            db.commit()

            print(f"[Обновлен] {site[0]} (new: {md5} | old: {site[1]})")
        except:
            print("Произошла ошибка при обновлении данных в БД")
    else:
        print(f"[Нет изменений] {site[0]} (hash: {md5})")


if __name__ == "__main__":
    sites = db.execute('SELECT * from sites').fetchall()

    for site in sites:
        url = requests.get(site[0], headers=headers)

        if url.status_code == 200:
            md5 = getMD5onPage(url, site[2])
            updateMD5()
