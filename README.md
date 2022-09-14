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

t1_champ1id, t1_champ1_sum1, t1_champ1_sum2, t1_champ2id, t1_champ2_sum1, t1_champ2_sum2, t1_champ3id, t1_champ3_sum1, 
t1_champ3_sum2, t1_champ4id, t1_champ4_sum1, t1_champ4_sum2, t1_champ5id, t1_champ5_sum1, t1_champ5_sum2, 
t1_ban1, t1_ban2, t1_ban3, t1_ban4, t1_ban5, 
t2_champ1id, t2_champ1_sum1, t2_champ1_sum2, t2_champ2id, t2_champ2_sum1, t2_champ2_sum2, t2_champ3id, t2_champ3_sum1, 
t2_champ3_sum2, t2_champ4id, t2_champ4_sum1, t2_champ4_sum2, t2_champ5id, t2_champ5_sum1, t2_champ5_sum2,
t2_ban1, t2_ban2, t2_ban3, t2_ban4, t2_ban5

### early-game model:

t1_champ1id, t1_champ1_sum1, t1_champ1_sum2, t1_champ2id, t1_champ2_sum1, t1_champ2_sum2, t1_champ3id, t1_champ3_sum1, 
t1_champ3_sum2, t1_champ4id, t1_champ4_sum1, t1_champ4_sum2, t1_champ5id, t1_champ5_sum1, t1_champ5_sum2, 
t1_ban1, t1_ban2, t1_ban3, t1_ban4, t1_ban5, 
t2_champ1id, t2_champ1_sum1, t2_champ1_sum2, t2_champ2id, t2_champ2_sum1, t2_champ2_sum2, t2_champ3id, t2_champ3_sum1, 
t2_champ3_sum2, t2_champ4id, t2_champ4_sum1, t2_champ4_sum2, t2_champ5id, t2_champ5_sum1, t2_champ5_sum2,
t2_ban1, t2_ban2, t2_ban3, t2_ban4, t2_ban5

(new added) firstBlood, firstTower, firstDragon, firstRiftHerald

### mid-game model:

t1_champ1id, t1_champ1_sum1, t1_champ1_sum2, t1_champ2id, t1_champ2_sum1, t1_champ2_sum2, t1_champ3id, t1_champ3_sum1, 
t1_champ3_sum2, t1_champ4id, t1_champ4_sum1, t1_champ4_sum2, t1_champ5id, t1_champ5_sum1, t1_champ5_sum2, 
t1_ban1, t1_ban2, t1_ban3, t1_ban4, t1_ban5, 
t2_champ1id, t2_champ1_sum1, t2_champ1_sum2, t2_champ2id, t2_champ2_sum1, t2_champ2_sum2, t2_champ3id, t2_champ3_sum1, 
t2_champ3_sum2, t2_champ4id, t2_champ4_sum1, t2_champ4_sum2, t2_champ5id, t2_champ5_sum1, t2_champ5_sum2,
t2_ban1, t2_ban2, t2_ban3, t2_ban4, t2_ban5
firstBlood, firstTower, firstDragon, firstRiftHerald

(new added) firstInhibitor, firstBaron, t1_towerKills, t1_dragonKills, t1_riftHeraldKills, t2_towerKills, t2_dragonKills, t2_riftHeraldKills

### post-game model:

t1_champ1id, t1_champ1_sum1, t1_champ1_sum2, t1_champ2id, t1_champ2_sum1, t1_champ2_sum2, t1_champ3id, t1_champ3_sum1, 
t1_champ3_sum2, t1_champ4id, t1_champ4_sum1, t1_champ4_sum2, t1_champ5id, t1_champ5_sum1, t1_champ5_sum2, 
t1_ban1, t1_ban2, t1_ban3, t1_ban4, t1_ban5, 
t2_champ1id, t2_champ1_sum1, t2_champ1_sum2, t2_champ2id, t2_champ2_sum1, t2_champ2_sum2, t2_champ3id, t2_champ3_sum1, 
t2_champ3_sum2, t2_champ4id, t2_champ4_sum1, t2_champ4_sum2, t2_champ5id, t2_champ5_sum1, t2_champ5_sum2,
t2_ban1, t2_ban2, t2_ban3, t2_ban4, t2_ban5
firstBlood, firstTower, firstDragon, firstRiftHerald, firstInhibitor, firstBaron, 
t1_towerKills, t1_dragonKills, t1_riftHeraldKills, 
t2_towerKills, t2_dragonKills, t2_riftHeraldKills

(new added) t1_inhibitorKills, t1_baronKills, t2_inhibitorKills, t2_baronKills

Feel free to check out `t.csv` under `data` folder as an example template for an intended input csv file. It specifies what 
columns and column names should be included to successfully run the program. If the input csv file does not include all 
columns corresponding to the executed model, an error message will be printed and the program will be terminated. 

Alternatively, predictor_input.py is always available that guides the user to input desired information of the game and provides
predictions for that particular game.

This project uses Python to implement the user interaction program and jupyter notebook to train classification models. 
