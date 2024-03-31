from thefuzz import fuzz
from thefuzz import process


if __name__ == '__main__':
    print('fuzz.ratio')
    ratio_strs = (
        'ontem fui a escola',
        'Ontem fui a escola',
        'Ontem fui à escola',
        'Ontem fui à escola.',
    )
    ratio_str_origin = 'Ontem fui à escola.'
    for ratio_str in ratio_strs:
        ratio = fuzz.ratio(ratio_str, ratio_str_origin)
        print(f'\'{ratio_str}\' -> \'{ratio_str_origin}\': {ratio}')
    print('fuzz.partial_ratio')
    for ratio_str in ratio_strs:
        ratio = fuzz.partial_ratio(ratio_str, ratio_str_origin)
        print(f'\'{ratio_str}\' -> \'{ratio_str_origin}\': {ratio}')
    print('fuzz.token_sort_ratio')
    a = 'Parece que está um pouco bagunçado isso daqui'
    b = 'que Parece está daqui isso bagunçado pouco um'
    ratio = fuzz.token_sort_ratio(a, b)
    print(f'\'{a}\' -> \'{b}\': {ratio}')
    print('fuzz.token_set_ratio')
    a = 'Caramba esse menino é chato dimais caramba menino chato'
    b = 'Esse menino é chato dimais caramba'
    ratio = fuzz.token_set_ratio(a, b)
    print(f'\'{a}\' -> \'{b}\': {ratio}')
    print('fuzz.partial_token_sort_ratio')
    a = 'Parece que está um pouco bagunçado isso daqui zé'
    b = 'que Parece está daqui isso bagunçado pouco um'
    ratio = fuzz.partial_token_sort_ratio(a, b)
    print(f'\'{a}\' -> \'{b}\': {ratio}')
    print('fuzz.partial_token_set_ratio')
    a = 'Caramba esse menino é chato dimais caramba menino chato, para de fazer isso!'
    b = 'Esse menino é chato dimais caramba'
    ratio = fuzz.partial_token_set_ratio(a, b)
    print(f'\'{a}\' -> \'{b}\': {ratio}')
    print('fuzz.WRatio')
    for ratio_str in ratio_strs:
        ratio = fuzz.WRatio(ratio_str, ratio_str_origin)
        print(f'\'{ratio_str}\' -> \'{ratio_str_origin}\': {ratio}')
    print('process.extract')
    sentences = [
        'Lamborguini Aventador is one of the fastest cars even made.',
        'What about watching a movie tonight?',
        'I don\'t know what you think but sometimes programming gets really boring doesn\'t it?',
        'Are you able to drive a car?'
    ]
    print(process.extract('car', choices=sentences))
    print(process.extract('car', choices=sentences, limit=2))
    print(process.extract('car', choices=sentences, limit=2, scorer=fuzz.WRatio))
    print(process.extract('car', choices=sentences, limit=2, scorer=fuzz.partial_token_sort_ratio))
    print(process.extract('car', choices=sentences, limit=2, scorer=fuzz.partial_token_set_ratio))
    print('process.extractOne')
    names = [
        'Alice', 
        'Bob', 
        'Charlie',
        'David', 
        'Emma', 
        'Frank', 
        'Grace', 
        'Hannah', 
        'Ian', 
        'Jessica'
    ]
    print(process.extractOne('ra', names))
    print(process.extractOne('ra', names, score_cutoff=95))
    print(process.extractOne('ra', names, scorer=fuzz.WRatio))
    print(process.extractOne('ra', names, scorer=fuzz.partial_token_sort_ratio))
    print(process.extractOne('ra', names, scorer=fuzz.partial_token_set_ratio))