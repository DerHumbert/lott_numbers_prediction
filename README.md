# lott_numbers_prediction
Exploring different techniques and algorithms using lottery numbers as input

This project explored a few concepts in order to build a lottery number predictor. In order to achieve that, data is taken from
https://www.loterianacional.gob.mx/Melate/Resultados. Melate is a Mexican lottery game which takes in account six balls and an
"additional". 

Of course, the idea of a lottery game is that there is no model that can fit the sequence in which the balls are extracted,
being a complete random event. However, different test have shown that this code is able to, from time to time, correctly 
predict around 2 numbers.

The first concept involved is web scraping. The function get_data applies web scrapping techniques to automatically download
the most recent file containing the results of all available games. This file contains historical data starting in 1984. 
This is the data that will be used to train the model.

For this particular project, LSTM was selected. LSTM's architecture is a RNN commonly used in forecasting problems. Thus, the
idea to apply this architecture in this use case. 

