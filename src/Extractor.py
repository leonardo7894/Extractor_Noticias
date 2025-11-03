from newspaper import Article

def ExtraerDatos(url: str):
    print(f"Intentando extraer datos de: {url}")
    a = Article(url, language='es')
    a.download()
    a.parse()
    datos = {
        "Titulo": a.title,
        "Texto": a.text,
        "Autor": a.authors,
        "Publicacion": str(a.publish_date)
    }
    return datos