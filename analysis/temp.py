from selenium import webdriver
from bs4 import BeautifulSoup
from html_table_parser import parser_functions
from webdriver_manager.chrome import ChromeDriverManager

import time
import pandas as pd 
from selenium.webdriver.common.by import By

url = r"https://namu.wiki/w/%EA%B2%BD%EA%B8%B0%EB%8F%84"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)


import collections
if not hasattr(collections, 'Callable'):
    collections.Callable = collections.abc.Callable

def html_source():
    # 목적지 elemect
    element = driver.find_element(By.XPATH, '//*[@id="NATSIYlew"]/div[2]/div/div/div/div/div/div/div/div/div[1]/div[3]/div/div/div[5]/div/div/div/div/div/div/div/div[11]/div/div/div/div/div[1]/div/div[5]/table/tbody/tr[2]/td/div/div/dl')
    # 방법 1 
    # from selenium.webdriver.common.action_chains import ActionChains
    # action = ActionChains(driver)
    # action.move_to_element(element).perform()
    # """
    # 목적지 element 까지 이동 (방법2)
    element.location_once_scrolled_into_view

    element.click()
    
    return driver.page_source

# making table
def bs4_source():
    html = html_source()
    soup = BeautifulSoup(html, 'lxml')
    time.sleep(1)
    frame = []
    for data in soup.find_all("div", {"class": 'VSRmNdhS'}):
        for i in data.find_all('a', {"class": 'c-4yqZxu'}):
            for j in i.find_all('span', {"class": '_b32e38543948c43390b2efd7650c5027'}):
                frame.append(j.text)
    pd.DataFrame(frame).to_csv("test.csv", index=False, index_label=False)
bs4_source()