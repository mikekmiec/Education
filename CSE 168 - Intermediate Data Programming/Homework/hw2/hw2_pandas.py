
import pandas as pd


# Write your functions here!


def parse(file_name):
    """
    This functin converts CSV file, returning a Pandas dataframe.
    """
    
    return pd.read_csv(file_name, header=0)


def species_count(data):
    """
    This function returns the number of unique species of Pokemon,
    using the name attribute (column).
    """
    return len(pd.unique(data.loc[:, 'name']))


def max_level(data):
    """
    This function returns the Pokemon with the highest level.
    """
    result = data[data['level'] == max(data['level'])].iloc[0, :]
    return (result['name'], result['level'])


def filter_range(data,low,high):
    '''
    This function returns all Pokemon whose level
    is within the selected range (inclusive).
    '''
    
    return data[(data['level'] >= low) & (data['level'] <= high)]['name'].tolist()

def mean_attack_for_type(data,type):
    '''
    This function takes a Pokemon type as an argument and returns
    the average attack stat for all the Pokemon in the dataset
    with that type.
    '''
    atk = data[data['type'] == type]['atk']
    return atk.mean()

def count_types(data):
    '''
    This function returns a dictionary with keys that are Pokemon types
    and values that are the number of times that type
    appears in the dataset.
    '''
    type_data = data.groupby(by='type').apply(len)
    result = {}
    for type, num in type_data.items():
        result[type] = num
    return result
    

def highest_stage_per_type(data):
    '''
    This function calculates the largest stage reached for each type of
    Pokemon in the dataset.
    ''' 
    stage_data = data.groupby('type')['stage'].max()
    result = {}
    for type, stage in stage_data.items():
        result[type] = stage
    return result


def mean_attack_per_type(data):
    '''
    This function calculates the average attack for every type of Pokemon
    in the dataset, returning a dictionary that has keys that are the
    Pokemon types and values that are the average attack for that
    Pokemon type.
    '''
    attack_data = data.groupby('type')['atk'].mean()
    result = {}
    for name, attack in attack_data.items():
        result[name] = round(attack,2)
    return result
    
    
    

    
    