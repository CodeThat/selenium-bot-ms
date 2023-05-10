# Lawyer Directory Scraper

This is a Python script that scrapes lawyer information from the Mississippi Bar Association's lawyer directory website.

## Prerequisites

Before running the script, make sure you have the following prerequisites installed:

- Python 3
- Selenium library (`pip install selenium`)
- BeautifulSoup library (`pip install beautifulsoup4`)
- Pandas library (`pip install pandas`)
- Chrome WebDriver executable

## Installation

1. Clone the repository to your local machine:

 ```git clone https://github.com/CodeThat/lawyer-directory-scraper.git```

2. Install the required dependencies using pip:

 ```pip install -r requirements.txt```

3. Download the appropriate Chrome WebDriver executable and place it in the project directory.

Usage
 1. Open the scraper.py file in a text editor.

 2. Set the proxy settings in the following variables:

 ```
 proxy_host = "127.0.0.1
 proxy_port = 1080
 ```
 3. Customize any other settings in the script as needed.

 4.  Run the script:
 ```python scraper.py```
  The script will navigate through the lawyer directory pages, scrape the data, and save it to a CSV file named data.csv.

 5. After the script finishes running, you can find the scraped data in the data.csv file.

Configuration
* The script uses the Chrome browser. Make sure you have the appropriate Chrome WebDriver executable for your Chrome browser version.

* By default, the script operates in headless mode and accepts insecure SSL certificates. You can modify these settings in the scraper.py file if needed.

License
This project is licensed under the MIT License.
```
Feel free to customize the readme according to your preferences and add any additional information or sections as necessary.
```


   
   
   
 
