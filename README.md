# Game Result Prediction

League of Legends is a worldwide famous MOBA game. Two teams of five players play against each other, aiming to destroy
the other team's Nexus before their own Nexus being destroyed. As players are interested in professional plays and their
own ranked games, it is meaningful for the players to utilize a tool that predicts the final result of a game for their 
own benefit. 

This project aims to predict the game result of a League of Legends game using the info from the game as it proceeds. It 
first trains four classification models to predict the result of a game at four stages of the game: 

- pre-game: refers to when the game has not started yet while the ban-pick 
phase is complete. 

- early-game: generally refers to when first blood, first tower, first dragon 
and/or first rift herald has been taken, usually around 10 minutes of the game.

- mid-game: refers to when first baron and/or first inhibitor has been taken, 
usually around 25 minutes of the game. 

- post-game: after the game has ended. 

As the game reaches the next stage, the user could switch to the model associated to that stage that analyzes more information 
from the game and provides more accurate prediction results. 

On the other hand, this project designs a program that allows user interaction. The program accepts game info as either 
standard system input or a csv file and produces predicted result. 

predictor_input.py is a program that is able to take standard system inputs and provide predictions for one game. 

predictor_csv.py is a program that takes a csv file as input, which is able to produce as many predictions as the number of games
included in the input file.
Please note that there are required columns for the model at each stage. The list of required columns are as follows:

### pre-game model:

't1_champ1id', 't1_champ1_sum1', 't1_champ1_sum2', 't1_champ2id', 't1_champ2_sum1', 't1_champ2_sum2', 't1_champ3id', 't1_champ3_sum1', 
't1_champ3_sum2', 't1_champ4id', 't1_champ4_sum1', 't1_champ4_sum2', 't1_champ5id', 't1_champ5_sum1', 't1_champ5_sum2', 
't1_ban1', 't1_ban2', 't1_ban3', 't1_ban4', 't1_ban5', 
't2_champ1id', 't2_champ1_sum1', 't2_champ1_sum2', 't2_champ2id', 't2_champ2_sum1', 't2_champ2_sum2', 't2_champ3id', 't2_champ3_sum1', 
't2_champ3_sum2', 't2_champ4id', 't2_champ4_sum1', 't2_champ4_sum2', 't2_champ5id', 't2_champ5_sum1', 't2_champ5_sum2',
't2_ban1', 't2_ban2', 't2_ban3', 't2_ban4', 't2_ban5'
