
from src.Extractor import ExtraerDatos   

def test_titulo():
    datos = ExtraerDatos("https://www.infobae.com/politica/2025/11/03/quien-asumira-como-diputado-en-lugar-de-diego-santilli-es-un-alfil-de-sebastian-pareja-que-suma-poder/")
    print(datos)
    assert datos["Titulo"] == "Quién asumirá como diputado en lugar de Diego Santilli: es un alfil de Sebastián Pareja, que suma poder" 
