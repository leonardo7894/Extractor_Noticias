from src.Extractor import ExtraerDatos  


def test_publicacion():
    datos = ExtraerDatos("https://www.infobae.com/politica/2025/11/03/quien-asumira-como-diputado-en-lugar-de-diego-santilli-es-un-alfil-de-sebastian-pareja-que-suma-poder/")
    datos["Publicacion"] == "2025-11-03 09:07:00"
    print(datos["Publicacion"])