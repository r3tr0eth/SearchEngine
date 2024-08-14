import requests
from bs4 import BeautifulSoup

def simple_crawler(start_url, max_pages=10):
    visited = set()
    to_visit = [start_url]
    crawled_data = {}
    pages_crawled = 0
    
    while to_visit and pages_crawled < max_pages:
        url = to_visit.pop(0)
        if url in visited:
            continue
        
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extraer texto
        text = soup.get_text()
        crawled_data[url] = text
        
        visited.add(url)
        pages_crawled += 1
        
        # Encontrar nuevos enlaces
        for link in soup.find_all('a', href=True):
            full_url = requests.compat.urljoin(url, link['href'])
            if full_url not in visited:
                to_visit.append(full_url)

    return crawled_data
