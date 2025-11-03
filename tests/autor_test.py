
from src.Extractor import ExtraerDatos  

def test_autor():
    datos = ExtraerDatos("https://www.infobae.com/politica/2025/11/03/quien-asumira-como-diputado-en-lugar-de-diego-santilli-es-un-alfil-de-sebastian-pareja-que-suma-poder/")
    print(datos)
    assert "Facundo Chaves" in datos["Autor"] #assert verifica que una porcion de codigo funcione
