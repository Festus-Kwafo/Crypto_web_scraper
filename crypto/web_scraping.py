from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from time import sleep
from background_task import background
from crypto.models import Crypto, PercentageChange
from crypto.utils import format_market_cap, remove_percent_sign, format_circulating_supply


@background()
def scrap_data_2():
    driver = webdriver.Edge()
    driver.get("https://coinmarketcap.com/all/views/all/")
    index = 0
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        try:
            # scrap data with bs4 when we scroll to  the bottom of the page ensuring that all data is
            # accessing to be scrap
            for i in range(0, last_height, 200):
                driver.execute_script("window.scrollTo(0, {});".format(i))
                sleep(0.1)
            # Get current scroll position
            current_position = driver.execute_script("return window.pageYOffset;")

            # Get total scroll height
            total_height = driver.execute_script("return document.body.scrollHeight;")

            # Get the viewport height
            viewport_height = driver.execute_script("return window.innerHeight;")

            # Check if we are at the bottom of the page
            if current_position + viewport_height >= total_height:
                #Get the page HTML
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                #Find All table rows
                rows = soup.findAll('tr')
                rows = rows[2:]
                #
                for row in rows[index:]:
                    cols = row.find_all('td')
                    i = [ele.text.strip() for ele in cols]
                    if len(i) >= 1:
                        percent_change = PercentageChange(  change_1h=remove_percent_sign(i[7]),
                                                            change_24h=remove_percent_sign(i[8]),
                                                            change_7d=remove_percent_sign(i[9]))
                        percent_change.save()
                        crypto = Crypto(rank=i[0],
                                        name=i[1],
                                        symbol=i[2],
                                        market_cap=format_market_cap(i[3]),
                                        price=i[4],
                                        circulating_supply= format_circulating_supply(i[5]),
                                        volume=i[6],
                                        percent_change = percent_change
                                        )
                        crypto.save()
                index = len(rows)
                # Locate the load more button and click it
                loadMoreButton = driver.find_element(By.XPATH, value='//button[text()="Load More"]')
                loadMoreButton.click()
                sleep(3)
                last_height = driver.execute_script("return document.body.scrollHeight")
            else:
                last_height = driver.execute_script("return document.body.scrollHeight")
                for i in range(0, last_height, 200):
                    driver.execute_script("window.scrollTo(0, {});".format(i))
                    sleep(0.1)
        except Exception as e:
            print(e)
            break



