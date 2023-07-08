import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def download_assets(url, directory):
  # Create a directory based on the URL
  directory_name = urlparse(url).netloc
  os.makedirs(directory_name, exist_ok=True)

  # Send a GET request to the URL
  response = requests.get(url)
  if response.status_code != 200:
    print(f"Failed to retrieve {url}")
    return

  # Parse the HTML content
  soup = BeautifulSoup(response.content, "html.parser")

  # Download images
  images = soup.find_all("img")
  for img in images:
    img_url = urljoin(url, img["src"])
    save_image(img_url, directory_name)

  # Download other assets (videos, etc.)
  assets = soup.find_all("source")
  for asset in assets:
    asset_url = urljoin(url, asset["src"])
    save_asset(asset_url, directory_name)


def save_image(url, directory):
  response = requests.get(url)
  if response.status_code == 200:
    filename = os.path.join(directory, os.path.basename(url))
    with open(filename, "wb") as f:
      f.write(response.content)
      print(f"Image saved: {filename}")
  else:
    print(f"Failed to download image: {url}")


def save_asset(url, directory):
  response = requests.get(url)
  if response.status_code == 200:
    filename = os.path.join(directory, os.path.basename(url))
    with open(filename, "wb") as f:
      f.write(response.content)
      print(f"Asset saved: {filename}")
  else:
    print(f"Failed to download asset: {url}")


# change the website_url to download assets from a different website
website_url = "https://websitedemos.net/organic-shop-02/"
download_assets(website_url, directory=website_url)
