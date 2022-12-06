import requests
from bs4 import BeautifulSoup
import os


def data_source():
    # Make a request to a web page
    page = requests.get(
        "https://www.census.gov/data/datasets/2021/econ/MHS/puf.html", timeout=5
    )
    # Create soup object
    soup = BeautifulSoup(page.content, "html.parser")
    # Get Download Links in a list
    links = []
    for url in soup.find_all(
        "a", class_="uscb-layout-align-start-start uscb-text-decoration-some", href=True
    ):
        links.append(url["href"])
    return links


def get_data():
    # Download data source and put into folder
    links = data_source()
    for i in range(len(data_source())):
        if i == 3:
            cmd = f"wget {links[i]} -P data_source/"
            os.system(cmd)
        else:
            cmd = f"wget https:{links[i]} -P data_source/"
            os.system(cmd)


if __name__ == "__main__":
    get_data()
