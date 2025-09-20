import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def main():
    url = "https://gozambiajobs.co.zm/jobs-modern-list/?specialisms=accountancy"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    elements = soup.find_all('div', class_='jobs-content')
    keyWords = {'accountant' : 0, 'finance': 0, 'audit': 0, 'financial': 0, 'lusaka': 0}
    print(f"Found {len(elements)} job listings.")
    print(f"Scraping URL: {url}, \n\n\n --------------------------------------")

    for jl in elements:
        listing = jl.get_text(strip=True).lower()
        words = listing.split(" ")
        words = {word.strip(",.()[]{}<>!@#$%^&*;:'\"") for word in words}

        for kw in keyWords.keys():
            if kw in words:
                keyWords[kw] += 1
        
        #print("\n\n\n")
    #print(f"Response Status Code: {response.content}")
    print(keyWords)

    plt.bar(keyWords.keys(), keyWords.values())
    plt.xlabel('Keywords')
    plt.ylabel('Frequency')

if __name__ == "__main__":
    main()