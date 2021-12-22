from bs4 import BeautifulSoup
import requests

# example url: https://en.wikipedia.org/wiki/Monosodium_glutamate

#Tasks:
# TODO: Create a web scraper accepts a wikipedia url. It should be composed of two functions:
# TODO: Create a function that accepts a url and returns the number of citations needed.
# TODO: Create a function that accepts a wikipedia url and returns a string containing each entry on a new line, in the order found

URL = "https://en.wikipedia.org/wiki/Monosodium_glutamate"

def get_citations_needed_count(url):
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    
    citations = soup.findAll("a", string="citation needed")

    citation_num = len(citations)

    print("Number of citations needed:", citation_num)
    # for citation in citations:
    #     print(citation.find_parent("p").text)

    # print(citations.prettify())

    return citation_num
    

def get_citations_needed_report(url):
    pass


get_citations_needed_count(URL)

# get_citations_needed_report(URL)