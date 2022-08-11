import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import lxml

def get_data_with_selenium(url):
    options = webdriver.ChromeOptions()
    #options.set_preference("general.useragent.override","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36")

    try:
        driver = webdriver.Chrome(
        executable_path = "C:/Users/Kirill/PycharmProjects/Portfolio/Parser/chromedriver.exe",
        options=options
        )
        driver.get(url=f'https://www.dns-shop.ru/catalog/17a892f816404e77/noutbuki/?price=50001-70000,70001-100000&f[p3q]=b3cu&f[65c]=264d')
        time.sleep(3)

        with open(f"index_selenium.html","w",encoding='utf-8') as file:
            file.write(driver.page_source)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
    with open("index_selenium.html","r",encoding="utf-8") as file:
        src = file.read()
        soup = BeautifulSoup(src, "lxml")
        laptop_cards = soup.find_all("div", class_="catalog-product ui-button-widget")

    for laptop_url in laptop_cards:
        laptop_url = "https://www.dns-shop.ru/" + laptop_url.find("a").get("href")
        print(laptop_url)

# url = "https://www.dns-shop.ru/catalog/17a892f816404e77/noutbuki/?price=50001-70000,70001-100000&f[p3q]=b3cu&f[65c]=264d&p=1"

# headers = {
# "Accept":"*/*",
# "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
# }
# r = requests.get(url,headers=headers)
# src = r.text
#
#
#
# with open("index.html", "w",encoding='utf-8') as file:
# file.write(src)

def main():
    url = f'https://www.dns-shop.ru/catalog/17a892f816404e77/noutbuki/?price=50001-70000,70001-100000&f[p3q]=b3cu&f[65c]=264d'
    get_data_with_selenium(url)



if __name__ == '__main__':
    main()