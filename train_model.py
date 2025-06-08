#Reading the csv
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense, Bidirectional, Dropout, Activation
from tensorflow import keras
from tensorflow.keras.optimizers import Adam
from keras import activations

def df_norm(df):
    scaler = StandardScaler()
    norm_df = scaler.fit_transform(df.values)
    return scaler, pd.DataFrame(df.values, index=df.index)


#Normalizing vectors

if __name__ == "__main__":

    df = pd.read_csv('data/melate_prep.csv') 
    
    scaler, df_norm = df_norm(df[['R1','R2', 'R3', 'R4', 'R5', 'R6', 'R7']])
    
    #Windowing and sample generation

    window_length = 9
    window_y = window_length + 1

    number_of_rows = df_norm.values.shape[0]
    print(number_of_rows)
    number_of_columns = df_norm.values.shape[1]
    print(number_of_columns)

    X = np.empty([int(number_of_rows / window_y), window_length, number_of_columns], dtype=float)
    y = np.empty([int(number_of_rows / window_y), number_of_columns], dtype=float)

    rows_for_prediction = df_norm.tail(window_length)
    df_norm = df_norm.head(number_of_rows - window_y)


    for i in range(0, int(number_of_rows / window_y) - 1):

        X[i] = df_norm.iloc[i * window_y : i * window_y + window_y - 1, 0 : number_of_columns]
        y[i] = df_norm.iloc[(i+1) * window_y -1 , 0 : number_of_columns]

    #Initialize the model
    model = Sequential()
    
    #Add layers to the model
    model.add(Bidirectional(LSTM(140, input_shape = (window_length, number_of_columns), return_sequences=True)))
    #Dropout is a regularizatin technique to prevent overfitting. 
    #Randomly selected neurons are ignored during training.
    model.add(Dropout(0.2))
    model.add(Bidirectional(LSTM(240, return_sequences=True)))
    model.add(Dropout(0.2))
    model.add(Bidirectional(LSTM(140, return_sequences=True)))
    model.add(Bidirectional(LSTM(70, return_sequences=False)))
    #Dense layer applies activation function 
    model.add(Dense(units=35))
 #, kernel_initializer="he_normal"))

    model.add(Dense(units=7, activation='linear'))
  
    
    model.compile(optimizer=Adam(learning_rate=0.001), loss='mean_squared_error', metrics=['mae']) 
    
    reduce_lr = keras.callbacks.ReduceLROnPlateau(monitor='accuracy', factor=0.5, patience=3, min_lr=0.001)
    early_stopping = keras.callbacks.EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
    model.fit(x=X, y=y, batch_size=32, epochs=100, verbose=2, callbacks=[reduce_lr, early_stopping], validation_split=0.2)
    
    to_predict = np.zeros((1, window_length, number_of_columns))
    to_predict[0,:,:] = rows_for_prediction
    
    next_game_prediction = model.predict(to_predict)

    print(next_game_prediction[0])
    final_pred = scaler.inverse_transform(next_game_prediction)
    rounded_pred = np.round(final_pred)
    print('The predicted numbers for the next game are: ',  rounded_pred)
    
    

 





