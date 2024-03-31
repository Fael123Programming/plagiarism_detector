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
    ratio_strs = (
        'ontem fui a escola',
        'Ontem fui a escola',
        'Ontem fui à escola',
        'Ontem fui à escola.',
    )
    ratio_str_origin = 'Ontem fui à escola.'
    for ratio_str in ratio_strs:
        ratio = fuzz.partial_ratio(ratio_str, ratio_str_origin)
        print(f'\'{ratio_str}\' -> \'{ratio_str_origin}\': {ratio}')

# Quinto slide: Métodos Extra
# -> String extraction: extrair uma string de um lista de strings que possui maior correspondência.
# -> Métodos mais importantes:
#    --> *process.extract*: encontra as strings com maior correspondência com a string passada como argumento de uma lista de strings;
#    -->