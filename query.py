import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys
import re

class Fetcher:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.PhantomJS()
        self.driver.wait = WebDriverWait(self.driver, 5)
    def lookup(self):
        self.driver.get(self.url)
        try:
            ip = self.driver.wait.until(EC.presence_of_element_located(By.CLASS_NAME, "gsfi"))
        except:
            print("failed to search")

        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        #finds the information from google search using st class in html
        tag = soup.select(".st")[0]
        contents = tag.contents
        answer = ""
        for line in contents: 
            if str(type(line)) == "<class 'bs4.element.Tag'>":
                if len(line.contents) > 0:
                    answer += line.contents[0]
            else:
                answer += line
            
            answer += " "
        self.driver.quit()
        return str(answer)
