from collections import defaultdict

def search_query(query, index):
    words = query.lower().split()
    results = defaultdict(int)
    
    for word in words:
        if word in index:
            for url in index[word]:
                results[url] += 1
    
    # Ordenar resultados por relevancia (número de coincidencias)
    sorted_results = sorted(results.items(), key=lambda item: item[1], reverse=True)
    
    return [url for url, count in sorted_results]
