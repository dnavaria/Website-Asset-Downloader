# Scrape Site Assets

## Description
- This script will scrape all assets from a site and download them to a local directory.
- The script will create a directory for each site and download the assets to that directory.
- The script will create a log file for each site and log the assets that were downloaded.


## Implementation Details
- The script will use the `aiohttp` library to make asynchronous HTTP requests.
- The script will use the `aiofiles` library to make asynchronous file writes.
- The script will use the `BeautifulSoup` library to parse the HTML.
- The script will use the `urlparse` library to parse the URL.
- The script will use the `os` library to create directories and files.
- The script will use the `asyncio` library to run the asynchronous tasks.
- The script will use the `logging` library to log the assets that were downloaded.

## Setup
- The script requires Python 3.7 or higher.
- Install the required libraries with the following command:
    - `pip3 install -r requirements.txt`

## Usage
- The script can be run with the following command:
    - `python3 main.py`
- Files will be downloaded to the `assets/<url>` directory.
- Logs will be written to the `assets/<url>/download.log` file.

