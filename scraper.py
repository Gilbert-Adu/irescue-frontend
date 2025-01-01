from bs4 import BeautifulSoup # type: ignore
import time
from selenium import webdriver  # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.common.keys import Keys # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.firefox.options import Options # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
import asyncio
import boto3 # type: ignore
import platform
import os
from pathlib import Path
from csv import DictReader
import requests # type: ignore
from requests.adapters import HTTPAdapter # type: ignore
from urllib3.util.retry import Retry # type: ignore








dynamodb = boto3.resource('dynamodb',
                          region_name=os.getenv("REGION_NAME"),
                          aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
                          aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
                          )




table = dynamodb.Table('ListingsData')

def get_desktop_path():
    home = str(Path.home())

    if platform.system() == "Windows":
        desktop = os.path.join(home, "Desktop")
    elif platform.system() == "Darwin":
        desktop = os.path.join(home, "Desktop")
    else:
        desktop = os.path.join(home, "Desktop")
    return desktop

cookies_file = os.path.join(get_desktop_path(), "qkr.csv")


firefox_options = Options()
firefox_options.add_argument("--headless")


def match_criteria(title, query):

    if query.lower() in title.lower():
        return True
    return False
    

def scrape_listings(query, minPrice, maxPrice, taskUrl):
    
    url = "https://irescue-ngrok.ngrok.io/insert_listings"
    # new_correct_ngrok_url = https://9589-2603-7080-a400-2a00-c088-8851-d153-fdfe.ngrok-free.app/insert_listings

    data = {
        "query": query,
        "minPrice": minPrice,
        "maxPrice": maxPrice,
        "taskUrl": taskUrl
    }


    

    try:
        response = requests.post(url, json=data)

        if response.status_code == 200:
            #table.put_item(Item={'title': title, 'description': desc_text, 'price': price, 'listing_url': listing_url,'task_url':taskUrl})
            print("response: ", response.json())
            print("success confirmed from misc.py")

        else:
            print("Failed to call the endpoint")

    except requests.exceptions.RequestException as e:
        print("Error while calling the API: ", str(e))






                    

                


        


