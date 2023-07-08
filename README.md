# Scrape Site Assets

## Description
- This Async program will scrape all assets from a site and download them to a local directory.
- It will create a directory for each site and download the assets to that directory along with a log file for each site, logging the assets that were downloaded.


## Implementation Details
- Libraries
    - `aiohttp` -> Asynchronous HTTP requests
    - `aiofiles` -> Asynchronous file writes
    - `BeautifulSoup` -> HTML parsing
    - `urlparse` -> URL parsing
    - `os` -> Directory and file creation
    - `asyncio` -> Asynchronous task execution
    - `logging` -> Logging

## Setup
- The script requires Python 3.7 or higher.
- Install the required libraries with the following command:
    - `pip3 install -r requirements.txt`

## Usage
- The script can be run with the following command:
    - `python3 main.py`
- Files will be downloaded to the `assets/<url>` directory.
- Logs will be written to the `assets/<url>/download.log` file.

