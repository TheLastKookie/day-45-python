import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
empire_webpage = response.text
soup = BeautifulSoup(empire_webpage, "html.parser")


rankings = [rank.getText() for rank in soup.find_all(name="h3", class_="title")]
rankings = rankings[::-1]

with open(file="movies.txt", mode="w") as movie_file:
    for rank in rankings:
        movie_file.write(f"{rank}\n")
