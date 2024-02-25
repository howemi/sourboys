# Web Scraping Script for SourGG Website

This simple Python script allows you to scrape information from
[sour.gg](https://sour.gg) to check the availability status of SourBoys. The
script looks for specific HTML elements on the page to determine if a product
is in stock or sold out.

## Prerequisites

Before using this script, ensure that you have Python installed on your system.
If you don't have Python installed, you can download it from the [official
Python website](https://www.python.org/downloads/).

## Installation

1. Clone or download the script files from this repository.

    ```bash
    git clone https://github.com/howemi/sourboys.git
    ```

2. Navigate to the project directory.

    ```bash
    cd sourboys
    ```

3. Install the required Python packages.

    ```bash
    pip install requests beautifulsoup4
    ```

## Usage

1. Open a terminal or command prompt and navigate to the project directory.

    ```bash
    cd path/to/sourboys
    ```

2. Run the script.

    ```bash
    python web_scraper.py
    ```

3. The script will output information about SourBoys on
   [sour.gg](https://sour.gg), indicating whether each product is in stock or
   sold out.

## Important Notes

- If the website structure changes, the script may break and you may need to
  pull the latest updates.
