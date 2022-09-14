import pandas as pd
import json
import pickle
import sys


'''
This is essentially the same user interface implementation as what 
predictor_input.py did, except for the fact that predictor_input.py takes 
type-in input while predictor_csv.py takes a csv file as input info. This 
program also supports functionality of prediction on the game result in one 
of the four following stages of a League of Legends game:

- pre-game: refers to when the game has not started yet while the ban-pick 
phase is complete. 

- early-game: generally refers to when first blood, first tower, first dragon 
and/or first rift herald has been taken, usually around 10 minutes of the game.

- mid-game: refers to when first baron and/or first inhibitor has been taken, 
usually around 25 minutes of the game. 

- post-game: after the game has ended. 
'''


def pre_game_predictor(test_data):
    '''
    Uses pre-game classification model to predict game result.
    '''
    
    test_columns = set(test_data.columns)
    need_columns = {'t1_champ1id', 't1_champ1_sum1',
                't1_champ1_sum2', 't1_champ2id', 't1_champ2_sum1', 't1_champ2_sum2',
                't1_champ3id', 't1_champ3_sum1', 't1_champ3_sum2', 't1_champ4id',
                't1_champ4_sum1', 't1_champ4_sum2', 't1_champ5id', 't1_champ5_sum1',
                't1_champ5_sum2', 't1_ban1', 't1_ban2', 't1_ban3',
                't1_ban4', 't1_ban5', 't2_champ1id', 't2_champ1_sum1', 't2_champ1_sum2',
                't2_champ2id', 't2_champ2_sum1', 't2_champ2_sum2', 't2_champ3id',
                't2_champ3_sum1', 't2_champ3_sum2', 't2_champ4id', 't2_champ4_sum1',
                't2_champ4_sum2', 't2_champ5id', 't2_champ5_sum1', 't2_champ5_sum2',
                't2_ban1', 't2_ban2', 't2_ban3', 't2_ban4',
                't2_ban5'}
    
    if not need_columns.issubset(test_columns):
        print('Not enough information provided in input file. Check documentation for required information.')
        return
    
    data = test_data[['t1_champ1id', 't1_champ1_sum1',
                't1_champ1_sum2', 't1_champ2id', 't1_champ2_sum1', 't1_champ2_sum2',
                't1_champ3id', 't1_champ3_sum1', 't1_champ3_sum2', 't1_champ4id',
                't1_champ4_sum1', 't1_champ4_sum2', 't1_champ5id', 't1_champ5_sum1',
                't1_champ5_sum2', 't1_ban1', 't1_ban2', 't1_ban3',
                't1_ban4', 't1_ban5', 't2_champ1id', 't2_champ1_sum1', 't2_champ1_sum2',
                't2_champ2id', 't2_champ2_sum1', 't2_champ2_sum2', 't2_champ3id',
                't2_champ3_sum1', 't2_champ3_sum2', 't2_champ4id', 't2_champ4_sum1',
                't2_champ4_sum2', 't2_champ5id', 't2_champ5_sum1', 't2_champ5_sum2',
                't2_ban1', 't2_ban2', 't2_ban3', 't2_ban4',
                't2_ban5']].copy()
    
    # get the trained model
    with open('models/pre_game_model.pkl', 'rb') as file:
        model = pickle.load(file)
    
    # predict with probability
    return model.predict_proba(data)


def early_game_predictor(test_data):
    '''
    Uses early-game classification model to predict game result.
    '''
    
    test_columns = set(test_data.columns)
    need_columns = {'t1_champ1id', 't1_champ1_sum1',
                't1_champ1_sum2', 't1_champ2id', 't1_champ2_sum1', 't1_champ2_sum2',
                't1_champ3id', 't1_champ3_sum1', 't1_champ3_sum2', 't1_champ4id',
                't1_champ4_sum1', 't1_champ4_sum2', 't1_champ5id', 't1_champ5_sum1',
                't1_champ5_sum2', 't1_ban1', 't1_ban2', 't1_ban3',
                't1_ban4', 't1_ban5', 't2_champ1id', 't2_champ1_sum1', 't2_champ1_sum2',
                't2_champ2id', 't2_champ2_sum1', 't2_champ2_sum2', 't2_champ3id',
                't2_champ3_sum1', 't2_champ3_sum2', 't2_champ4id', 't2_champ4_sum1',
                't2_champ4_sum2', 't2_champ5id', 't2_champ5_sum1', 't2_champ5_sum2',
                't2_ban1', 't2_ban2', 't2_ban3', 't2_ban4',
                't2_ban5', 'firstBlood', 'firstTower',
                'firstDragon', 'firstRiftHerald'}
    
    if not need_columns.issubset(test_columns):
        print('Not enough information provided in input file. Check documentation for required information.')
        return
    
    data = test_data[['t1_champ1id', 't1_champ1_sum1',
                't1_champ1_sum2', 't1_champ2id', 't1_champ2_sum1', 't1_champ2_sum2',
                't1_champ3id', 't1_champ3_sum1', 't1_champ3_sum2', 't1_champ4id',
                't1_champ4_sum1', 't1_champ4_sum2', 't1_champ5id', 't1_champ5_sum1',
                't1_champ5_sum2', 't1_ban1', 't1_ban2', 't1_ban3',
                't1_ban4', 't1_ban5', 't2_champ1id', 't2_champ1_sum1', 't2_champ1_sum2',
                't2_champ2id', 't2_champ2_sum1', 't2_champ2_sum2', 't2_champ3id',
                't2_champ3_sum1', 't2_champ3_sum2', 't2_champ4id', 't2_champ4_sum1',
                't2_champ4_sum2', 't2_champ5id', 't2_champ5_sum1', 't2_champ5_sum2',
                't2_ban1', 't2_ban2', 't2_ban3', 't2_ban4',
                't2_ban5', 'firstBlood', 'firstTower',
                'firstDragon', 'firstRiftHerald']].copy()
    
    # get the trained model
    with open('models/begin_game_model.pkl', 'rb') as file:
        model = pickle.load(file)
    
    # predict with probability
    return model.predict_proba(data)


def mid_game_predictor(test_data):
    '''
    Uses mid-game classification model to predict game result.
    '''
    
    test_columns = set(test_data.columns)
    need_columns = {'t1_champ1id', 't1_champ1_sum1',
            't1_champ1_sum2', 't1_champ2id', 't1_champ2_sum1', 't1_champ2_sum2',
            't1_champ3id', 't1_champ3_sum1', 't1_champ3_sum2', 't1_champ4id',
            't1_champ4_sum1', 't1_champ4_sum2', 't1_champ5id', 't1_champ5_sum1',
            't1_champ5_sum2', 't1_ban1', 't1_ban2', 't1_ban3',
            't1_ban4', 't1_ban5', 't2_champ1id', 't2_champ1_sum1', 't2_champ1_sum2',
            't2_champ2id', 't2_champ2_sum1', 't2_champ2_sum2', 't2_champ3id',
            't2_champ3_sum1', 't2_champ3_sum2', 't2_champ4id', 't2_champ4_sum1',
            't2_champ4_sum2', 't2_champ5id', 't2_champ5_sum1', 't2_champ5_sum2',
            't2_ban1', 't2_ban2', 't2_ban3', 't2_ban4',
            't2_ban5', 'firstBlood', 'firstTower', 'firstInhibitor', 'firstBaron',
            'firstDragon', 'firstRiftHerald', 't1_towerKills', 't1_dragonKills', 
            't1_riftHeraldKills', 't2_towerKills', 't2_dragonKills','t2_riftHeraldKills'}
    
    if not need_columns.issubset(test_columns):
        print('Not enough information provided in input file. Check documentation for required information.')
        return
    
    data = test_data[['t1_champ1id', 't1_champ1_sum1',
            't1_champ1_sum2', 't1_champ2id', 't1_champ2_sum1', 't1_champ2_sum2',
            't1_champ3id', 't1_champ3_sum1', 't1_champ3_sum2', 't1_champ4id',
            't1_champ4_sum1', 't1_champ4_sum2', 't1_champ5id', 't1_champ5_sum1',
            't1_champ5_sum2', 't1_ban1', 't1_ban2', 't1_ban3',
            't1_ban4', 't1_ban5', 't2_champ1id', 't2_champ1_sum1', 't2_champ1_sum2',
            't2_champ2id', 't2_champ2_sum1', 't2_champ2_sum2', 't2_champ3id',
            't2_champ3_sum1', 't2_champ3_sum2', 't2_champ4id', 't2_champ4_sum1',
            't2_champ4_sum2', 't2_champ5id', 't2_champ5_sum1', 't2_champ5_sum2',
            't2_ban1', 't2_ban2', 't2_ban3', 't2_ban4',
            't2_ban5', 'firstBlood', 'firstTower', 'firstInhibitor', 'firstBaron',
            'firstDragon', 'firstRiftHerald', 't1_towerKills', 't1_dragonKills', 
            't1_riftHeraldKills', 't2_towerKills', 't2_dragonKills','t2_riftHeraldKills']].copy()
    
    # get the trained model
    with open('models/mid_game_model.pkl', 'rb') as file:
        model = pickle.load(file)
    
    # predict with probability
    return model.predict_proba(data)


def post_game_predictor(test_data):
    '''
    Uses post-game classification model to predict game result.
    '''
    
    test_columns = set(test_data.columns)
    need_columns = {'firstBlood', 'firstTower', 'firstInhibitor', 'firstBaron',
           'firstDragon', 'firstRiftHerald', 't1_champ1id', 't1_champ1_sum1',
           't1_champ1_sum2', 't1_champ2id', 't1_champ2_sum1', 't1_champ2_sum2',
           't1_champ3id', 't1_champ3_sum1', 't1_champ3_sum2', 't1_champ4id',
           't1_champ4_sum1', 't1_champ4_sum2', 't1_champ5id', 't1_champ5_sum1',
           't1_champ5_sum2', 't1_towerKills', 't1_inhibitorKills', 't1_baronKills',
           't1_dragonKills', 't1_riftHeraldKills', 't1_ban1', 't1_ban2', 't1_ban3',
           't1_ban4', 't1_ban5', 't2_champ1id', 't2_champ1_sum1', 't2_champ1_sum2',
           't2_champ2id', 't2_champ2_sum1', 't2_champ2_sum2', 't2_champ3id',
           't2_champ3_sum1', 't2_champ3_sum2', 't2_champ4id', 't2_champ4_sum1',
           't2_champ4_sum2', 't2_champ5id', 't2_champ5_sum1', 't2_champ5_sum2',
           't2_towerKills', 't2_inhibitorKills', 't2_baronKills', 't2_dragonKills',
           't2_riftHeraldKills', 't2_ban1', 't2_ban2', 't2_ban3', 't2_ban4',
           't2_ban5'}
    
    if not need_columns.issubset(test_columns):
        print('Not enough information provided in input file. Check documentation for required information.')
        return
    
    data = test_data[['firstBlood', 'firstTower', 'firstInhibitor', 'firstBaron',
           'firstDragon', 'firstRiftHerald', 't1_champ1id', 't1_champ1_sum1',
           't1_champ1_sum2', 't1_champ2id', 't1_champ2_sum1', 't1_champ2_sum2',
           't1_champ3id', 't1_champ3_sum1', 't1_champ3_sum2', 't1_champ4id',
           't1_champ4_sum1', 't1_champ4_sum2', 't1_champ5id', 't1_champ5_sum1',
           't1_champ5_sum2', 't1_towerKills', 't1_inhibitorKills', 't1_baronKills',
           't1_dragonKills', 't1_riftHeraldKills', 't1_ban1', 't1_ban2', 't1_ban3',
           't1_ban4', 't1_ban5', 't2_champ1id', 't2_champ1_sum1', 't2_champ1_sum2',
           't2_champ2id', 't2_champ2_sum1', 't2_champ2_sum2', 't2_champ3id',
           't2_champ3_sum1', 't2_champ3_sum2', 't2_champ4id', 't2_champ4_sum1',
           't2_champ4_sum2', 't2_champ5id', 't2_champ5_sum1', 't2_champ5_sum2',
           't2_towerKills', 't2_inhibitorKills', 't2_baronKills', 't2_dragonKills',
           't2_riftHeraldKills', 't2_ban1', 't2_ban2', 't2_ban3', 't2_ban4',
           't2_ban5']].copy()
    
    # get the trained model
    with open('models/post_game_model.pkl', 'rb') as file:
        model = pickle.load(file)
    
    # predict with probability
    return model.predict_proba(data)


def main():
    # grab the input csv file name
    try: 
        file_name = sys.argv[1].strip()
    except IndexError:
        print('No file input. Please input a csv file.')
        return
    
    # edge case check
    if len(sys.argv) > 2:
        print('This program accepts only one input file.')
        return
    
    if file_name[-4:] != '.csv':
        print('Input file format is not valid. Please try again.')
        return
    
    test_data = pd.read_csv(file_name)
    
    # input game status, i.e. choose predictor
    while True:
        game_status = input('Enter game status. Options are pre-game, ' + 
                            'early-game, mid-game, post-game.\ngame status: ').strip().lower()
        if game_status not in {'pre-game', 'early-game', 'mid-game', 'post-game'}:
            print('Invalid input. Please try again.')
        else:
            break
    
    if game_status == 'pre-game':
        win_prob = pre_game_predictor(test_data)
    elif game_status == 'early-game':
        win_prob = early_game_predictor(test_data)
    elif game_status == 'mid-game':
        win_prob = mid_game_predictor(test_data)
    else:
        win_prob = post_game_predictor(test_data)
        
    print('')
    print('------------------')
    print('Prediction result:')
    for probs in win_prob:
        team1_win, team2_win = tuple(probs)
        print(f'team 1 wins: {round(team1_win * 100, 2)}%, team 2 wins: {round(team2_win * 100, 2)}%')
    

if __name__ == '__main__':
    main()
