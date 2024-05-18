import pandas as pd

def readcsv(path):
    resultados = pd.read_csv(path)
    resultados_ord = resultados.iloc[::-1]
    results = resultados_ord.drop(['NPRODUCTO', 'CONCURSO', 'BOLSA', 'FECHA'], axis=1)
    return results
if __name__ == "__main__":

    df = readcsv('Melate.csv') 
    print(df)







