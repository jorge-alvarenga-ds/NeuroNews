import feedparser

# URL do feed RSS que queremos verificar
# (Este é um feed real do portal G1)
url_do_feed = "https://simonwillison.net/atom/everything/"

# A função parse faz o download e a análise do feed
feed = feedparser.parse(url_do_feed)

# --- Exibindo informações gerais do Feed ---
print("--- Informações do Canal ---")
print(f"Título do Feed: {feed.feed.title}")
print(f"Link do Feed: {feed.feed.link}")
print("-" * 30)
print("\n--- Últimas Notícias ---")

# --- Iterando sobre as entradas (notícias) do Feed ---
# feed.entries é uma lista onde cada item é uma notícia/post
for i, entry in enumerate(feed.entries):
    # Vamos limitar a exibição às 5 primeiras notícias
    if i >= 5:
        break
    
    print(f"\nNotícia #{i+1}")
    print(f"  Título: {entry.title}")
    print(f"  Link: {entry.link}")
    print(f" Conteudo: {entry.summary}")
    
    # Nem todo feed tem a data de publicação, então é bom verificar
    if 'published' in entry:
        print(f"  Publicado em: {entry.published}")