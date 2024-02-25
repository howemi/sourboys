#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all elements with the specified classes
        target_elements = soup.find_all(class_='grid__column grid__column--6 grid__column--4@md')

        for element in target_elements:
            # Find the value in the element with the classes "tile__heading hidden"
            heading_element = element.find(class_='tile__heading hidden')

            if heading_element:
                product_name = heading_element.get_text(strip=True)

                # Check if the element contains an image with alt attribute "soldout.png"
                image_tag = element.find('img', alt='soldout.png')

                # Check if the product name ends with "SourBoys"
                if image_tag and product_name.endswith("SourBoys"):
                    print(f"{product_name}: sold out")
                elif not image_tag and product_name.endswith("SourBoys"):
                    print(f"{product_name}: in stock")

    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)

# Replace 'your_website_url' with the actual URL of the webpage you want to scrape
website_url = 'https://sour.gg'
scrape_website(website_url)
