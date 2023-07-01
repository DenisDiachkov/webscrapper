# Webscrapper.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import bs4
from pyvirtualdisplay import Display 
import time
import traceback
import asyncio


class Webscrapper:
    @staticmethod
    def __get_chrome_driver():
        options = Options()
        options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(options=options)
        
        return driver

    @staticmethod
    async def scrape(url, retries, wait_time, load_page_wait_time=3):
        while retries > 0:
            try:
                display = Display(visible=0, size=(1920, 1280))
                display.start()
                driver = Webscrapper.__get_chrome_driver()
                driver.get(url)
                # Wait for page to load
                time.sleep(load_page_wait_time)
                soup = bs4.BeautifulSoup(driver.page_source, features="html.parser")
                driver.quit()
                display.stop()
                print (f"Scraped {url}")
                break
            except Exception as e:
                print (f"Error while scraping {url}\n{e}\nRetrying...")
                # Traceback
                print (traceback.format_exc())  
                time.sleep(wait_time)
                retries -= 1
        return soup
    
    @staticmethod
    def get_or_create_eventloop():
        try:
            return asyncio.get_event_loop()
        except RuntimeError as ex:
            if "There is no current event loop" in str(ex):
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                return asyncio.get_event_loop()

    @staticmethod
    def scrape_elements(url, name, attrs, except_retries, none_retries, wait_time):
        loop = Webscrapper.get_or_create_eventloop()
        while none_retries > 0:
            soup = loop.run_until_complete(Webscrapper.scrape(url, except_retries, wait_time))
            elems = soup.find_all(name, attrs)
            if len(elems) > 0:
                return elems
            time.sleep(wait_time)
            none_retries -= 1
            print(f"None returned, Retrying {url}")
        return None
    
    @staticmethod
    def scrape_whole_page(url, retries, wait_time):
        loop = Webscrapper.get_or_create_eventloop()
        try:
            soup = loop.run_until_complete(Webscrapper.scrape(url, retries, wait_time))
        finally:
            loop.close()
        return soup
