import requests
from bs4 import BeautifulSoup

def scrape_daraz_phones(url):
    # Send an HTTP request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract information from the page
        phone_list = []

        # The product containers might have different classes, inspect the HTML
        product_containers = soup.find_all('div', class_='c2prKC')

        for container in product_containers:
            # Extract the name and price
            name = container.find('div', class_='c16H9d').text.strip()
            price = container.find('span', class_='c13VH6').text.strip()

            # Append the data to the phone_list
            phone_list.append({'name': name, 'price': price})

        return phone_list
    else:
        print(f"Error: Unable to fetch the page. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    daraz_url = "https://www.daraz.pk/smartphones/?spm=a2a0e.pdp.cate_7.1.648c6498u26rMd"
    phones = scrape_daraz_phones(daraz_url)

    if phones:
        # Print the collected data
        for i, phone in enumerate(phones, start=1):
            print(f"{i}. {phone['name']} - {phone['price']}")
    else:
        print("Scraping failed.")
