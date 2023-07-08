# Scrape Site Assets

## Description
- The Asset Downloader is a Python script that allows you to download images and other assets from a given website URL. It utilizes asynchronous programming with asyncio and aiohttp to efficiently download the assets concurrently. It also parses the HTML content of the website using BeautifulSoup to extract the URLs of the assets to be downloaded. The script logs the status and details of the downloaded assets to a log file.

## Features
- Downloads images and other assets (videos, etc.) from a website URL.
- Supports parsing HTML content using BeautifulSoup.
- Downloads assets concurrently using asyncio and aiohttp.
- Logs the status and details of downloaded assets to a log file.
- Exception handling to handle errors and continue with the remaining assets.

## Requirements
- The script requires Python 3.7 or higher.
- `aiohttp` -> Asynchronous HTTP requests
- `aiofiles` -> Asynchronous file writes
- `BeautifulSoup` -> HTML parsing
- `urlparse` -> URL parsing
- `os` -> Directory and file creation
- `asyncio` -> Asynchronous task execution
- `logging` -> Logging

## Setup
- Clone the repository or download the source code:
```bash
git clone https://github.com/dnavaria/scrape_site_assets.git
```
- Install the required libraries with the following command:
    - `pip3 install -r requirements.txt`

## Usage
- Open the asset_downloader.py file and locate the following line:
```python
website_url  = 'https://www.example.com'
```
- The script can be run with the following command:
    - `python3 main.py`
- Files will be downloaded to the `assets/<url>` directory.
- Logs will be written to the `assets/<url>/download.log` file.

## Contributing
- Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License
- This project is licensed under the MIT License.