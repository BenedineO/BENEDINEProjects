# SCRAPPING THE BOOKS TO SCRAPE WEBSITE
# This website list books along with the titles, prices and Ratings
# ------------------------------------------------------------------------------------------------------------------
# I aim to scrape the following data from each book: Title, price and Rating
# ------------------------------------------------------------------------------------------------------------------

# STEP 1:
import requests
# URL of the website to scrape
url = "https://exwhyzee.ng/"
# Send a GET request to fetch the HTML content of the page
response = requests.get(url)
if response.status_code == 200:
    print("Page successfully retrieved!")
else:
    print("Failed to retrieve page.")

# STEP 2:
from bs4 import BeautifulSoup

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Display the first 500 characters of the parsed HTML to see what we have
print(soup.prettify()[:500])
print(soup.title.text)

# STEP 3:
# Find all book containers on the page
book_containers = soup.find_all("article", class_="product_pod")
# Loop through each container and extract the relevant information
for book in book_containers:
    title = book.find("h3").find("a")["title"]
    price = book.find("p", class_="price_color").text
    rating = book.find("p", class_="star-rating"[1])
    print(f'Book Title: {title}')
    print(f'Book Price: {price}')
    print(f'Book Rating: {rating} stars')
    print("-" * 40)

# STEP 4:
import csv
# Open a csv file to store the data
with open("books.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Book Title", "Book Price", "Book Rating"])
# Loop through the book containers and write the data to the csv file
    for book in book_containers:
        title = book.find("h3").find("a")["title"]
        price = book.find("p", class_="price_color").text
        rating = book.find("p", class_="star-rating")["class"][1]
        writer.writerow([title, price, rating]) # write data for each book
print("Data successfully saved to books.csv!")




