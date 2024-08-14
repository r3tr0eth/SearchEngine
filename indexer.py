from collections import defaultdict
import re
import json

def create_index(crawled_data):
    index = defaultdict(list)
    
    for url, content in crawled_data.items():
        words = re.findall(r'\w+', content.lower())
        for word in words:
            index[word].append(url)
    
    return index

# Guardar el índice en un archivo JSON
def save_index(index, filepath='data/index.json'):
    with open(filepath, 'w') as f:
        json.dump(index, f, indent=4)
