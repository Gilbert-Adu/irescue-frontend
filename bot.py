import torch # type: ignore
from transformers import BertTokenizer, BertModel # type: ignore
import boto3 # type: ignore
from sklearn.metrics.pairwise import cosine_similarity # type: ignore
import numpy as np
import time
from bs4 import BeautifulSoup # type: ignore
from csv import DictReader
from emailer import send_email
from requests.adapters import HTTPAdapter # type: ignore
import requests # type: ignore
from urllib3.util.retry import Retry # type: ignore



from selenium import webdriver  # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.common.keys import Keys # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.firefox.options import Options # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore

import platform
import os
from pathlib import Path
import requests # type: ignore

import schedule # type: ignore
import time






def message_clients():



    while True:
        try:
            url = "https://irescue-ngrok.ngrok.io/messaging_endpoint"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                print("running in background")
            else:
                print("error calling endpoint: ", str(response.status_code))
        
        except Exception as e:
            print("exception occurred: ", str(e))

        time.sleep(120) #in seconds
    """
        #call get_response here and send response to API
    url = "http://localhost:4000/messaging_endpoint"

    data = {}

    retry_strategy = Retry(
        total=10000,
        backoff_factor=0.5,
        status_forcelist=[404, 500, 502, 503, 504],
        allowed_methods=["HEAD", "GET", "POST", "OPTIONS"]

    )
    adapter = HTTPAdapter(max_retries=retry_strategy)

    session = requests.Session()
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    

    try:
        response = session.post(url, json=data)
        print("checking and sending messages")

        if response.status_code == 200:
            #table.put_item(Item={'title': title, 'description': desc_text, 'price': price, 'listing_url': listing_url,'task_url':taskUrl})
            print("response: ", response.json())
            print("successfully sending messages")

        else:
            print("Failed to call the endpoint")


    except requests.exceptions.RequestException as e:
        print("Error while calling the API: ", str(e))

