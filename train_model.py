#Reading the csv
import pandas as pd
import numpy as np

def df_norm(df):
    return (df- df.min()) / (df.max() - df.min())


#Normalizing vectors

if __name__ == "__main__":

    df = pd.read_csv('data/melate_prep.csv') 
    #df1 = df.loc[:,1:]
    #print(df.columns)
    
    df_norm = df_norm(df[['R1','R2', 'R3', 'R4', 'R5', 'R6', 'R7']])
    #print(df_norm.head())

    print(df.shape)
    



                                #Windowing and sample generation

    window_length = 9
    window_y = window_length + 1
  
    #print(last_window)

    number_of_rows = df_norm.values.shape[0]
    print(number_of_rows)
    number_of_columns = df_norm.values.shape[1]
    print(number_of_columns)


    #filas= total de filas del df / window_y , columnas= numero de columnas
    X = np.empty([int(number_of_rows / window_y), window_length, number_of_columns], dtype=float)
    #y debe tener n filas (número de ventanas) y las 7 columnas
    #filas= total de filas del df / window_y , columnas= numero de columnas
    y = np.empty([int(number_of_rows / window_y), number_of_columns], dtype=float)


    for i in range(0, int(number_of_rows / window_y)):
        #print(df_norm.iloc[i * window_y : i * window_y + window_y -1, 0 : number_of_columns])
        #print(df_norm.iloc[(i+1) * window_y -1 , 0 : number_of_columns])
        X[i] = df_norm.iloc[i * window_y : i * window_y + window_y -1, 0 : number_of_columns]
        y[i] = df_norm.iloc[(i+1) * window_y -1 , 0 : number_of_columns]
        # print(i * window_y , i * window_y + window_y -2, 0 , number_of_columns)
        # print( (i+1) * window_y -1 , 0 , number_of_columns)
    
    

 





