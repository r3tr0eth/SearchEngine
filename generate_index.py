from app.crawler import simple_crawler
from app.indexer import create_index, save_index

# Rastrear algunas páginas (puedes cambiar la URL y el número de páginas)
crawled_data = simple_crawler('https://www.xataka.com/', max_pages=10)

# Crear el índice
index = create_index(crawled_data)

# Guardar el índice
save_index(index)

print("Index generated and saved successfully.")
