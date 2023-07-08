import os
import asyncio
import aiohttp
import logging
import aiofiles
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


async def download_assets(url, directory):
    # Create a directory based on the URL
    directory_name = urlparse(url).netloc
    os.makedirs(directory_name, exist_ok=True)

    # Set up logging
    log_filename = os.path.join(directory_name, "download.log")
    logging.basicConfig(
        filename=log_filename,
        level=logging.INFO,
        format="%(asctime)s - %(message)s"
    )

    # Send a GET request to the URL
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if not (200 <= response.status < 300):
                    logging.error(f"Failed to retrieve {url} (status code: {response.status})")
                    return

                # Parse the HTML content
                content = await response.text()
                soup = BeautifulSoup(content, "html.parser")

                # Download images
                images = soup.find_all("img")
                image_tasks = []
                for img in images:
                    img_url = urljoin(url, img["src"])
                    image_tasks.append(download_image(img_url, directory_name, session))

                # Download other assets (videos, etc.)
                assets = soup.find_all("source")
                asset_tasks = []
                for asset in assets:
                    asset_url = urljoin(url, asset["src"])
                    asset_tasks.append(download_asset(asset_url, directory_name, session))

                await asyncio.gather(*image_tasks, *asset_tasks)

    except Exception as e:
        logging.error(f"Error occurred while downloading assets: {str(e)}")


async def download_image(url, directory, session):
    try:
        async with session.get(url) as response:
            if 200 <= response.status < 300:
                filename = os.path.join(directory, os.path.basename(url))
                async with aiofiles.open(filename, "wb") as f:
                    await f.write(await response.content.read())
                logging.info(f"Image saved: {filename}")
            else:
                logging.error(f"Failed to download image: {url} (status code: {response.status})")

    except Exception as e:
        logging.error(f"Error occurred while downloading image {url}: {str(e)}")


async def download_asset(url, directory, session):
    try:
        async with session.get(url) as response:
            if 200 <= response.status < 300:
                filename = os.path.join(directory, os.path.basename(url))
                async with aiofiles.open(filename, "wb") as f:
                    await f.write(await response.content.read())
                logging.info(f"Asset saved: {filename}")
            else:
                logging.error(f"Failed to download asset: {url} (status code: {response.status})")

    except Exception as e:
        logging.error(f"Error occurred while downloading asset {url}: {str(e)}")


# change the website_url to download assets from a different website
website_url = "https://websitedemos.net/organic-shop-02/"

asyncio.run(download_assets(website_url, directory=website_url))
