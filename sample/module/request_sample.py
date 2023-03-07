import json
import os

import requests


nasa_api_key = os.environ.get("API_KEY")
api_url = "https://api.nasa.gov/planetary/apod?api_key={}".format(nasa_api_key)


def request_get(api_url=api_url):
    try:
        response = requests.get(api_url)
        # これで200以外の場合はエラーに出来る
        response.raise_for_status()
        print(response)
        json_response = json.loads(response.text)
        print(json_response)
    except requests.exceptions.RequestException as e:
        print("Error occured!!", e)
