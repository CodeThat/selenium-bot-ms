# Lawyer Directory Scraper

This repository contains both Python and C# implementations of a web scraper that collects lawyer information from the Mississippi Bar Association's lawyer directory website.

## Prerequisites

### Python Version:
- Python 3
- Selenium library (`pip install selenium`)
- BeautifulSoup library (`pip install beautifulsoup4`)
- Pandas library (`pip install pandas`)
- Chrome WebDriver executable

### C# Version:
- .NET SDK (either .NET Core or .NET Framework)
- Selenium WebDriver for C# (`NuGet: Selenium.WebDriver`)
- Edge WebDriver (or Chrome WebDriver for Edge/Chrome automation)

## Installation

### Python Version:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/CodeThat/lawyer-directory-scraper.git
   ```

2. Navigate to the `python/` directory:

   ```bash
   cd python/
   ```

3. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. Download the appropriate Chrome WebDriver executable and place it in the project directory.

### C# Version:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/CodeThat/lawyer-directory-scraper.git
   ```

2. Navigate to the `csharp/` directory:

   ```bash
   cd csharp/
   ```

3. Install the required NuGet packages, including Selenium WebDriver:

   ```bash
   dotnet add package Selenium.WebDriver
   ```

4. Download the Edge WebDriver (or Chrome WebDriver) and place it in the project directory.

## Usage

### Python Version:

1. Open the `scraper.py` file in a text editor.

2. Set the proxy settings in the following variables:

   ```python
   proxy_host = "127.0.0.1"
   proxy_port = 1080
   ```

3. Customize any other settings in the script as needed.

4. Run the script:

   ```bash
   python scraper.py
   ```

   The script will navigate through the lawyer directory pages, scrape the data, and save it to a CSV file named `data.csv`.

5. After the script finishes running, you can find the scraped data in the `data.csv` file.

### C# Version:

1. Open the `Program.cs` file in a text editor or IDE.

2. Update the WebDriver settings if necessary, including the path to your Edge or Chrome WebDriver.

3. Run the program using the .NET CLI or your IDE:

   ```bash
   dotnet run
   ```

   The C# scraper will navigate through the lawyer directory pages and save the scraped data to a CSV file.

## Configuration

### Python Version:
- The script uses the Chrome browser. Make sure you have the appropriate Chrome WebDriver executable for your Chrome browser version.
- By default, the script operates in headless mode and accepts insecure SSL certificates. You can modify these settings in the `scraper.py` file if needed.

### C# Version:
- The program uses Edge WebDriver by default. Ensure you have the correct version of Edge WebDriver for your browser version.
- You can update browser preferences and WebDriver options in the `Program.cs` file.

## License

This project is licensed under the MIT License. Feel free to modify and distribute the code as needed.
