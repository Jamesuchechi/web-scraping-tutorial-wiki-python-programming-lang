import requests
from bs4 import BeautifulSoup
import csv

url = "https://en.wikipedia.org/wiki/python_(programming_language)"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    soup = BeautifulSoup(response.text, "html.parser")

    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    for heading in headings:
        print(heading.get_text().strip())

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


with open("headings.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Heading", "Tag"])
    for heading in headings:
        writer.writerow([heading.get_text().strip(), heading.name])
    for heading in headings:
        writer.writerow([heading.get_text().strip()])

print("Headings have been written to headings.csv")