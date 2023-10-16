import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://cloud-api.yandex.net/"
TOKEN = os.getenv('TOKEN')


def header():
    yd_headers = {'Content-Type': 'application/json',
                  'Authorization': f'OAuth {TOKEN}'}
    return yd_headers


def create_folder(path):
    response = requests.put(f'{BASE_URL}v1/disk/resources?path={path}',
                            headers=header())
    return response.status_code


if __name__ == "__main__":
    create_folder('test')
