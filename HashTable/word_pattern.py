def parttern_word(pattern, words):
    p = pattern
    temp = words.split(' ')
    return len(set(zip(p, temp))) == len(set(p)) == len(set(temp)) and len(p) == len(temp)

if __name__ == '__main__':
    pattern = 'abba'
    a = 'dog cat cat dog'
    b = 'dog cat cat fish'
    print(parttern_word(pattern, b))
