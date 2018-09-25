import random
import urllib.request


# str functions converts other data types to string

def download(url):
    name = random.randrange(1, 1000)
    file_name = str(name) + ".png"
    urllib.request.urlretrieve(url, file_name)


download("URL HERE")
