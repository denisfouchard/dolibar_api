from dotenv import load_dotenv
from os import getenv
load_dotenv()

API_KEY = getenv('API_KEY')

class Dolibar():
    def __init__(self, api_key):
        self.api_key = api_key

if __name__ == '__main__':
    dolibar = Dolibar(API_KEY)
    print(dolibar.api_key)