import pandas as pd
import json
import pickle


'''
Creates a user interface where user could input specified game info to predict
the game result as the game proceeds. The program supports functionality of 
prediction on the game result in one of the four following stages of a League 
of Legends game:

- pre-game: refers to when the game has not started yet while the ban-pick 
phase is complete. 

- early-game: generally refers to when first blood, first tower, first dragon 
and/or first rift herald has been taken, usually around 10 minutes of the game.

- mid-game: refers to when first baron and/or first inhibitor has been taken, 
usually around 25 minutes of the game. 

- post-game: after the game has ended. 
'''


def pre_game_predictor(champs, smn_spells):
    '''
    Implements the pregame classification model.
    Info needed: champion names and summoner spell names. 
    '''
    
    picks = {}
    bans = {}
    ss = {}
    for i in range(1, 3):
        for j in range(1, 6):
            while True:
                ban_name = input(f'Team {i} ban {j} name: ').strip().lower()
                if ban_name not in champs.index:
                    print('Invalid input. Please try again.')
                else:
                    break

            bans[f't{i}_ban{j}'] = champs[ban_name]

            while True:
                champ_name = input(f'Team {i} champion {j} name: ').strip().lower()
                if champ_name not in champs.index:
                    print('Invalid input. Please try again.')
                elif champs[champ_name] in picks.values():
                    print('Duplicated picks. Please try again.')
                elif champs[champ_name] in bans.values():
                    print('Pick not allowed. Please try again.')
                else:
                    break

            picks[f't{i}_champ{j}id'] = champs[champ_name]
            
            while True:
                ss1 = input(f'Team {i} champion {j} smn spell 1 (D): ').strip().lower()
                if ss1 not in smn_spells.index:
                    print('Invalid input. Please try again.')
                else:
                    break
                    
            while True:
                ss2 = input(f'Team {i} champion {j} smn spell 2 (F): ').strip().lower()
                if ss2 not in smn_spells.index:
                    print('Invalid input. Please try again.')
                else:
                    break
            
            ss[f't{i}_champ{j}_sum1'] = smn_spells[ss1]
            ss[f't{i}_champ{j}_sum2'] = smn_spells[ss2]
            
    data = pd.DataFrame()
    for attr, value in picks.items():
        data[attr] = [value]
    for attr, value in bans.items():
        data[attr] = [value]
    for attr, value in ss.items():
        data[attr] = [value]
    
    data = data[['t1_champ1id', 't1_champ1_sum1',
                't1_champ1_sum2', 't1_champ2id', 't1_champ2_sum1', 't1_champ2_sum2',
                't1_champ3id', 't1_champ3_sum1', 't1_champ3_sum2', 't1_champ4id',
                't1_champ4_sum1', 't1_champ4_sum2', 't1_champ5id', 't1_champ5_sum1',
                't1_champ5_sum2', 't1_ban1', 't1_ban2', 't1_ban3',
                't1_ban4', 't1_ban5', 't2_champ1id', 't2_champ1_sum1', 't2_champ1_sum2',
                't2_champ2id', 't2_champ2_sum1', 't2_champ2_sum2', 't2_champ3id',
                't2_champ3_sum1', 't2_champ3_sum2', 't2_champ4id', 't2_champ4_sum1',
                't2_champ4_sum2', 't2_champ5id', 't2_champ5_sum1', 't2_champ5_sum2',
                't2_ban1', 't2_ban2', 't2_ban3', 't2_ban4',
                't2_ban5']]
    
    # get the trained model
    with open('models/pre_game_model.pkl', 'rb') as file:
        model = pickle.load(file)
    
    # predict with probability
    return tuple(model.predict_proba(data)[0])


def early_game_predictor(champs, smn_spells):
    '''
    Implements the early game classification model.
    Info needed: pre-game info plus first blood, first tower, 
    first dragon, and first rift herald. 
    '''
    
    picks = {}
    bans = {}
    ss = {}
    for i in range(1, 3):
        for j in range(1, 6):
            while True:
                ban_name = input(f'Team {i} ban {j} name: ').strip().lower()
                if ban_name not in champs.index:
                    print('Invalid input. Please try again.')
                else:
                    break

            bans[f't{i}_ban{j}'] = champs[ban_name]

            while True:
                champ_name = input(f'Team {i} champion {j} name: ').strip().lower()
                if champ_name not in champs.index:
                    print('Invalid input. Please try again.')
                elif champs[champ_name] in picks.values():
                    print('Duplicated picks. Please try again.')
                elif champs[champ_name] in bans.values():
                    print('Pick not allowed. Please try again.')
                else:
                    break

            picks[f't{i}_champ{j}id'] = champs[champ_name]
            
            while True:
                ss1 = input(f'Team {i} champion {j} smn spell 1 (D): ').strip().lower()
                if ss1 not in smn_spells.index:
                    print('Invalid input. Please try again.')
                else:
                    break
                    
            while True:
                ss2 = input(f'Team {i} champion {j} smn spell 2 (F): ').strip().lower()
                if ss2 not in smn_spells.index:
                    print('Invalid input. Please try again.')
                else:
                    break
            
            ss[f't{i}_champ{j}_sum1'] = smn_spells[ss1]
            ss[f't{i}_champ{j}_sum2'] = smn_spells[ss2]
            
    
    while True:
        first_blood = input('First blood (1 or 2, or 0 for not happened): ').strip()
        if first_blood not in {'0', '1', '2'}:
            print('Invalid input. Please try again.')
        else:
            first_blood = int(first_blood)
            break
            
    while True:
        first_tower = input('First tower (1 or 2, or 0 for not happened): ').strip()
        if first_tower not in {'0', '1', '2'}:
            print('Invalid input. Please try again.')
        else:
            first_tower = int(first_tower)
            break
            
    while True:
        first_dragon = input('First dragon (1 or 2, or 0 for not happened): ').strip()
        if first_dragon not in {'0', '1', '2'}:
            print('Invalid input. Please try again.')
        else:
            first_dragon = int(first_dragon)
            break
            
    while True:
        first_rh = input('First rift herald (1 or 2, or 0 for not happened): ').strip()
        if first_rh not in {'0', '1', '2'}:
            print('Invalid input. Please try again.')
        else:
            first_rh = int(first_rh)
            break
            
    data = pd.DataFrame()
    for attr, value in picks.items():
        data[attr] = [value]
    for attr, value in bans.items():
        data[attr] = [value]
    for attr, value in ss.items():
        data[attr] = [value]
    
    data['firstBlood'] = [first_blood]
    data['firstTower'] = [first_tower]
    data['firstDragon'] = [first_dragon]
    data['firstRiftHerald'] = [first_rh]
    
    data = data[['t1_champ1id', 't1_champ1_sum1',
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
                'firstDragon', 'firstRiftHerald']]
    
    # get the trained model
    with open('models/begin_game_model.pkl', 'rb') as file:
        model = pickle.load(file)
    
    # predict with probability
    return tuple(model.predict_proba(data)[0])


def mid_game_predictor(champs, smn_spells):
    '''
    Implements the mid game classification model.
    Info needed: early-game info plus first baron, first inhib, and number 
    of towers and dragons taken by each team. 
    '''
    
    picks = {}
    bans = {}
    ss = {}
    for i in range(1, 3):
        for j in range(1, 6):
            while True:
                ban_name = input(f'Team {i} ban {j} name: ').strip().lower()
                if ban_name not in champs.index:
                    print('Invalid input. Please try again.')
                else:
                    break

            bans[f't{i}_ban{j}'] = champs[ban_name]

            while True:
                champ_name = input(f'Team {i} champion {j} name: ').strip().lower()
                if champ_name not in champs.index:
                    print('Invalid input. Please try again.')
                elif champs[champ_name] in picks.values():
                    print('Duplicated picks. Please try again.')
                elif champs[champ_name] in bans.values():
                    print('Pick not allowed. Please try again.')
                else:
                    break

            picks[f't{i}_champ{j}id'] = champs[champ_name]
            
            while True:
                ss1 = input(f'Team {i} champion {j} smn spell 1 (D): ').strip().lower()
                if ss1 not in smn_spells.index:
                    print('Invalid input. Please try again.')
                else:
                    break
                    
            while True:
                ss2 = input(f'Team {i} champion {j} smn spell 2 (F): ').strip().lower()
                if ss2 not in smn_spells.index:
                    print('Invalid input. Please try again.')
                else:
                    break
            
            ss[f't{i}_champ{j}_sum1'] = smn_spells[ss1]
            ss[f't{i}_champ{j}_sum2'] = smn_spells[ss2]
            
    
    while True:
        first_blood = input('First blood (1 or 2, or 0 for not happened): ').strip()
        if first_blood not in {'0', '1', '2'}:
            print('Invalid input. Please try again.')
        else:
            first_blood = int(first_blood)
            break
            
    while True:
        first_tower = input('First tower (1 or 2, or 0 for not happened): ').strip()
        if first_tower not in {'0', '1', '2'}:
            print('Invalid input. Please try again.')
        else:
            first_tower = int(first_tower)
            break
            
    while True:
        first_dragon = input('First dragon (1 or 2, or 0 for not happened): ').strip()
        if first_dragon not in {'0', '1', '2'}:
            print('Invalid input. Please try again.')
        else:
            first_dragon = int(first_dragon)
            break
            
    while True:
        first_rh = input('First rift herald (1 or 2, or 0 for not happened): ').strip()
        if first_rh not in {'0', '1', '2'}:
            print('Invalid input. Please try again.')
        else:
            first_rh = int(first_rh)
            break
            
    while True:
        first_baron = input('First baron (1 or 2, or 0 for not happened): ').strip()
        if first_baron not in {'0', '1', '2'}:
            print('Invalid input. Please try again.')
        else:
            first_baron = int(first_baron)
            break
            
    while True:
        first_inhib = input('First inhibitor (1 or 2, or 0 for not happened): ').strip()
        if first_inhib not in {'0', '1', '2'}:
            print('Invalid input. Please try again.')
        else:
            first_inhib = int(first_inhib)
            break
            
    data = pd.DataFrame()
    for attr, value in picks.items():
        data[attr] = [value]
    for attr, value in bans.items():
        data[attr] = [value]
    for attr, value in ss.items():
        data[attr] = [value]
    
    data['firstBlood'] = [first_blood]
    data['firstTower'] = [first_tower]
    data['firstDragon'] = [first_dragon]
    data['firstRiftHerald'] = [first_rh]
    data['firstBaron'] = [first_baron]
    data['firstInhibitor'] = [first_inhib]
    
    for i in range(1, 3):
        while True:
            tower_kills = input(f'Team {i} tower kills: ').strip()
            if not tower_kills.isnumeric():
                print('Invalid input. Please try again.')
            else:
                data[f't{i}_towerKills'] = [int(tower_kills)]
                break
            
        while True:
            dragon_kills = input(f'Team {i} dragon kills: ').strip()
            if not dragon_kills.isnumeric():
                print('Invalid input. Please try again.')
            else:
                data[f't{i}_dragonKills'] = [int(dragon_kills)]
                break
                
        while True:
            rh_kills = input(f'Team {i} rift herald kills: ').strip()
            if not rh_kills.isnumeric():
                print('Invalid input. Please try again.')
            else:
                data[f't{i}_riftHeraldKills'] = [int(rh_kills)]
                break
    
    data = data[['t1_champ1id', 't1_champ1_sum1',
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
            't1_riftHeraldKills', 't2_towerKills', 't2_dragonKills','t2_riftHeraldKills']]
    
    # get the trained model
    with open('models/mid_game_model.pkl', 'rb') as file:
        model = pickle.load(file)
    
    # predict with probability
    return tuple(model.predict_proba(data)[0])
    
    
def post_game_predictor(champs, smn_spells):
    '''
    Implements the post game classification model.
    Info needed: all info in the game.
    '''
    
    picks = {}
    bans = {}
    ss = {}
    for i in range(1, 3):
        for j in range(1, 6):
            while True:
                ban_name = input(f'Team {i} ban {j} name: ').strip().lower()
                if ban_name not in champs.index:
                    print('Invalid input. Please try again.')
                else:
                    break

            bans[f't{i}_ban{j}'] = champs[ban_name]

            while True:
                champ_name = input(f'Team {i} champion {j} name: ').strip().lower()
                if champ_name not in champs.index:
                    print('Invalid input. Please try again.')
                elif champs[champ_name] in picks.values():
                    print('Duplicated picks. Please try again.')
                elif champs[champ_name] in bans.values():
                    print('Pick not allowed. Please try again.')
                else:
                    break

            picks[f't{i}_champ{j}id'] = champs[champ_name]
            
            while True:
                ss1 = input(f'Team {i} champion {j} smn spell 1 (D): ').strip().lower()
                if ss1 not in smn_spells.index:
                    print('Invalid input. Please try again.')
                else:
                    break
                    
            while True:
                ss2 = input(f'Team {i} champion {j} smn spell 2 (F): ').strip().lower()
                if ss2 not in smn_spells.index:
                    print('Invalid input. Please try again.')
                else:
                    break
            
            ss[f't{i}_champ{j}_sum1'] = smn_spells[ss1]
            ss[f't{i}_champ{j}_sum2'] = smn_spells[ss2]
            
    
    while True:
        first_blood = input('First blood (1 or 2, or 0 for not happened): ').strip()
        if first_blood not in {'0', '1', '2'}:
            print('Invalid input. Please try again.')
        else:
            first_blood = int(first_blood)
            break
            
    while True:
        first_tower = input('First tower (1 or 2, or 0 for not happened): ').strip()
        if first_tower not in {'0', '1', '2'}:
            print('Invalid input. Please try again.')
        else:
            first_tower = int(first_tower)
            break
            
    while True:
        first_dragon = input('First dragon (1 or 2, or 0 for not happened): ').strip()
        if first_dragon not in {'0', '1', '2'}:
            print('Invalid input. Please try again.')
        else:
            first_dragon = int(first_dragon)
            break
            
    while True:
        first_rh = input('First rift herald (1 or 2, or 0 for not happened): ').strip()
        if first_rh not in {'0', '1', '2'}:
            print('Invalid input. Please try again.')
        else:
            first_rh = int(first_rh)
            break
            
    while True:
        first_baron = input('First baron (1 or 2, or 0 for not happened): ').strip()
        if first_baron not in {'0', '1', '2'}:
            print('Invalid input. Please try again.')
        else:
            first_baron = int(first_baron)
            break
            
    while True:
        first_inhib = input('First inhibitor (1 or 2, or 0 for not happened): ').strip()
        if first_inhib not in {'0', '1', '2'}:
            print('Invalid input. Please try again.')
        else:
            first_inhib = int(first_inhib)
            break
            
    data = pd.DataFrame()
    for attr, value in picks.items():
        data[attr] = [value]
    for attr, value in bans.items():
        data[attr] = [value]
    for attr, value in ss.items():
        data[attr] = [value]
    
    data['firstBlood'] = [first_blood]
    data['firstTower'] = [first_tower]
    data['firstDragon'] = [first_dragon]
    data['firstRiftHerald'] = [first_rh]
    data['firstBaron'] = [first_baron]
    data['firstInhibitor'] = [first_inhib]
    
    for i in range(1, 3):
        while True:
            tower_kills = input(f'Team {i} tower kills: ').strip()
            if not tower_kills.isnumeric():
                print('Invalid input. Please try again.')
            else:
                data[f't{i}_towerKills'] = [int(tower_kills)]
                break
            
        while True:
            dragon_kills = input(f'Team {i} dragon kills: ').strip()
            if not dragon_kills.isnumeric():
                print('Invalid input. Please try again.')
            else:
                data[f't{i}_dragonKills'] = [int(dragon_kills)]
                break
                
        while True:
            rh_kills = input(f'Team {i} rift herald kills: ').strip()
            if not rh_kills.isnumeric():
                print('Invalid input. Please try again.')
            else:
                data[f't{i}_riftHeraldKills'] = [int(rh_kills)]
                break
                
        while True:
            baron_kills = input(f'Team {i} baron kills: ').strip()
            if not baron_kills.isnumeric():
                print('Invalid input. Please try again.')
            else:
                data[f't{i}_baronKills'] = [int(baron_kills)]
                break
                
        while True:
            inhib_kills = input(f'Team {i} inhibitor kills: ').strip()
            if not inhib_kills.isnumeric():
                print('Invalid input. Please try again.')
            else:
                data[f't{i}_inhibitorKills'] = [int(inhib_kills)]
                break
        
    
    data = data[['firstBlood', 'firstTower', 'firstInhibitor', 'firstBaron',
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
       't2_ban5']]
    
    # get the trained model
    with open('models/post_game_model.pkl', 'rb') as file:
        model = pickle.load(file)
    
    # predict with probability
    return tuple(model.predict_proba(data)[0])
    

def main():
    # parse json file of champion info
    with open('data/champion_info_2.json', 'r') as f:
        data = json.loads(f.read())

    data['data'] = list(data['data'].values())
    champs = pd.json_normalize(data, record_path=['data'])
    champs['name'] = champs['name'].str.lower()
    champs = champs.set_index('name').sort_values('id')['id']
    
    # parse json file of summoner spell info
    with open('data/summoner_spell_info.json', 'r') as f:
        data = json.loads(f.read())

    data['data'] = list(data['data'].values())
    smn_spells = pd.json_normalize(data, record_path=['data'])
    smn_spells['name'] = smn_spells['name'].str.lower()
    smn_spells = smn_spells.set_index('name').sort_values('id')['id']
    
    # create a user interface for the predictor
    
    # input game status, i.e. choose predictor
    while True:
        game_status = input('Enter game status. Options are pre-game, ' + 
                            'early-game, mid-game, post-game.\ngame status: ').strip().lower()
        if game_status not in {'pre-game', 'early-game', 'mid-game', 'post-game'}:
            print('Invalid input. Please try again.')
        else:
            break
    
    if game_status == 'pre-game':
        team1_win, team2_win = pre_game_predictor(champs, smn_spells)
    elif game_status == 'early-game':
        team1_win, team2_win = early_game_predictor(champs, smn_spells)
    elif game_status == 'mid-game':
        team1_win, team2_win = mid_game_predictor(champs, smn_spells)
    else:
        team1_win, team2_win = post_game_predictor(champs, smn_spells)
        
    print('')
    print('------------------')
    print('Prediction result:')
    print(f'team 1 wins: {round(team1_win * 100, 2)}%')
    print(f'team 2 wins: {round(team2_win * 100, 2)}%')
    
if __name__ == '__main__':
    main()
