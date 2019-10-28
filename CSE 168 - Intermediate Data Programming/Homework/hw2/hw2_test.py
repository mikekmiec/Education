from cse163_utils import assert_equals
# Don't worry about this import syntax, we will talk about it later

import hw2_manual
import hw2_pandas


# This file is left blank for you to fill in with your tests!
DATA = hw2_pandas.parse('pokemon_test.csv')
DATA2 = hw2_pandas.parse('pokemon_jay.csv')

NUMERICAL_COLS = ['id', 'level', 'atk', 'def', 'hp', 'stage']

parsed_data = hw2_manual.parse('pokemon_test.csv', NUMERICAL_COLS)
parsed_data2 = hw2_manual.parse('pokemon_jay.csv', NUMERICAL_COLS)


def test_species_count():
    '''
    Test spcies_count funciton.
    '''
    print("test_species_count")
    print('Part0')
    assert_equals(3, hw2_manual.species_count(parsed_data))
    assert_equals(74, hw2_manual.species_count(parsed_data2))
    print('Part1')
    assert_equals(3, hw2_pandas.species_count(DATA))
    assert_equals(74, hw2_pandas.species_count(DATA2))


def test_max_level():
    '''
    Test max_level funciton.
    '''
    print("test_max_level")
    print('Part0')
    assert_equals(('Lapras', 72), hw2_manual.max_level(parsed_data))
    assert_equals(('Victreebel', 100), hw2_manual.max_level(parsed_data2))
    print('Part1')
    assert_equals(('Lapras', 72), hw2_pandas.max_level(DATA))
    assert_equals(('Victreebel', 100), hw2_pandas.max_level(DATA2))
    
    
def test_filter_range():
    '''
    Test filter_range funciton.
    '''
    print("test_filter_range")
    print('Part0')
    assert_equals(['Arcanine', 'Arcanine', 'Starmie'],
                  hw2_manual.filter_range(parsed_data, 30, 70))
    assert_equals(['Seaking', 'Vaporeon', 'Spearow', 'Rapidash', 'Lickitung',
                  'Vaporeon', 'Doduo', 'Clefairy', 'Starmie', 'Moltres'],
                  hw2_manual.filter_range(parsed_data2, 60, 70))
    print('Part1')
    assert_equals(['Arcanine', 'Arcanine', 'Starmie'],
                  hw2_pandas.filter_range(DATA, 30, 70))
    assert_equals(['Seaking', 'Vaporeon', 'Spearow', 'Rapidash', 'Lickitung',
                  'Vaporeon', 'Doduo', 'Clefairy', 'Starmie', 'Moltres'],
                  hw2_pandas.filter_range(DATA2, 60, 70))


def test_mean_attack_for_type():
    '''
    Test mean_attack_for_type funciton.
    '''
    print("test_mean_attack_for_type")
    print('Part0')
    assert_equals(47.5, hw2_manual.mean_attack_for_type(parsed_data, 'fire'))
    assert_equals(101.8,
                  hw2_manual.mean_attack_for_type(parsed_data2, 'water'))
    print('Part1')
    assert_equals(47.5, hw2_pandas.mean_attack_for_type(DATA, 'fire'))
    assert_equals(101.8, hw2_pandas.mean_attack_for_type(DATA2, 'water'))


def test_count_types():
    '''
    Test count_types function.
    '''
    print("test_count_types")
    print('Part0')
    assert_equals({'water': 2, 'fire': 2},
                  hw2_manual.count_types(parsed_data))
    assert_equals({'bug': 3, 'electric': 1, 'fairy': 3, 'fighting': 3,
                  'fire': 13, 'flying': 6, 'ghost': 3, 'grass': 15,
                   'ground': 4, 'normal': 8, 'poison': 10, 'psychic': 4,
                   'rock': 6, 'water': 20},
                  hw2_manual.count_types(parsed_data2))
    print('Part1')
    assert_equals({'water': 2, 'fire': 2},
                  hw2_pandas.count_types(DATA))
    assert_equals({'bug': 3, 'electric': 1, 'fairy': 3, 'fighting': 3,
                  'fire': 13, 'flying': 6, 'ghost': 3, 'grass': 15,
                   'ground': 4, 'normal': 8, 'poison': 10, 'psychic': 4,
                   'rock': 6, 'water': 20}, hw2_pandas.count_types(DATA2))


def test_highest_stage_per_type():
    '''
    Test highest_stage_per_type funciton.
    '''
    print("test_highest_stage_per_type")
    print('Part0')
    assert_equals({'water': 2, 'fire': 2},
                  hw2_manual.highest_stage_per_type(parsed_data))
    assert_equals({'bug': 3, 'electric': 1, 'fairy': 1, 'fighting': 2,
                  'fire': 3, 'flying': 3, 'ghost': 3, 'grass': 3,
                   'ground': 2, 'normal': 2, 'poison': 3, 'psychic': 2,
                   'rock': 2, 'water': 2},
                  hw2_manual.highest_stage_per_type(parsed_data2))
    print('Part1')
    assert_equals({'water': 2, 'fire': 2},
                  hw2_pandas.highest_stage_per_type(DATA))
    assert_equals({'bug': 3, 'electric': 1, 'fairy': 1, 'fighting': 2,
                  'fire': 3, 'flying': 3, 'ghost': 3, 'grass': 3,
                   'ground': 2, 'normal': 2, 'poison': 3, 'psychic': 2,
                   'rock': 2, 'water': 2},
                  hw2_pandas.highest_stage_per_type(DATA2))


def test_mean_attack_per_type():
    '''
    Test mean_attack_per_type funciton.
    '''
    print("test_mean_attack_per_type")
    print('Part0')
    assert_equals({'water': 140.5, 'fire': 47.5},
                  hw2_manual.mean_attack_per_type(parsed_data))
    assert_equals({'bug': 25.0, 'electric': 64.0, 'fairy': 76.33,
                   'fighting': 99.67, 'fire': 99.31, 'flying': 110.83,
                   'ghost': 88.0, 'grass': 97.0, 'ground': 110.25,
                   'normal': 119.88, 'poison': 123.7, 'psychic': 127.75,
                   'rock': 88.17, 'water': 101.8},
                  hw2_manual.mean_attack_per_type(parsed_data2))
    print('Part1')
    assert_equals({'water': 140.5, 'fire': 47.5},
                  hw2_pandas.mean_attack_per_type(DATA))
    assert_equals({'bug': 25.0, 'electric': 64.0, 'fairy': 76.33,
                   'fighting': 99.67, 'fire': 99.31, 'flying': 110.83,
                   'ghost': 88.0, 'grass': 97.0, 'ground': 110.25,
                   'normal': 119.88, 'poison': 123.7, 'psychic': 127.75,
                   'rock': 88.17, 'water': 101.8},
                  hw2_pandas.mean_attack_per_type(DATA2))


def main():
    test_species_count()
    test_max_level()
    test_filter_range()
    test_highest_stage_per_type()
    test_mean_attack_for_type()
    test_mean_attack_per_type()




if __name__ == '__main__':
    main()