try:
    from thefuzz import fuzz as f
except:
    import os
    os.system('pip install thefuzz')


if __name__ == '__main__':
    source_txt = input('- Enter the source text to compare against (original):\n')
    target_txt = input('- Enter the target text to compare with (possible plagiarism):\n')
    result = f.partial_token_sort_ratio(source_txt, target_txt)
    if result >= 60:
        print('* It\'s a plagiarism.')
    else:
        print('* Not a plagiarism.')
    print(f'Similarity: {result}')
