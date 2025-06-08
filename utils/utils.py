

def readcsv(path):
    resultados = pd.read_csv(path)
    resultados_ord = resultados.iloc[::-1]
    results = resultados_ord.drop(['NPRODUCTO', 'CONCURSO', 'BOLSA', 'FECHA'], axis=1)
    results = results.tail(3900)
    print (results.head())
    print(len(results))
    return results
if __name__ == "__main__":

    df = readcsv('data/Melate.csv') 
    df.to_csv('data/melate_prep.csv')