from bs4 import BeautifulSoup
import requests

# example url: https://en.wikipedia.org/wiki/Monosodium_glutamate

#Tasks:
# DONE: Create a web scraper accepts a wikipedia url. It should be composed of two functions:
# DONE: Create a function that accepts a url and returns the number of citations needed.
# DONE: Create a function that accepts a wikipedia url and returns a string containing each entry on a new line, in the order found

URL = "https://en.wikipedia.org/wiki/Monosodium_glutamate"

prompt = """
Check for citations needed on a wikipedia article.
Please provide a wikipedia url:
>"""

URL = input(prompt)

def get_citations_needed_count(url):
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    
    citations = soup.findAll("a", string="citation needed")

    citation_num = len(citations)

    print("Number of citations needed:", citation_num)

    return citation_num
    

def get_citations_needed_report(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    
    citations = soup.findAll("a", string="citation needed")

    citation_list = [citation.find_parent("p").text for citation in citations]

    #handle duplicate parent elements
    citation_list = list(set(citation_list))

    citations_string = ""

    #extract passages requiring citation
    for p in citation_list:

        s = p.split("]")
        s = filter(lambda txt: "[citation needed" in txt, s)
        for txt in s:
            citations_string += ("\n" + txt + "]\n")

    print(citations_string)

    return citations_string


get_citations_needed_count(URL)
get_citations_needed_report(URL)