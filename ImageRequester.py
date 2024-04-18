import requests
from bs4 import BeautifulSoup

def search_images(query):
    url = f"https://www.google.com/search?q={query}&tbm=isch"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    image_links = []
    for img in soup.find_all('img'):
        image_links.append(img.get('src'))

    return image_links

if __name__ == "__main__":
    query = input("Enter your search query: ")
    image_links = search_images(query)
    
    for link in image_links:
        print(link)
