from collections import Counter

def count_word(s):
    c = s.split(' ')
    result = {}
    for element in c:
        result[element] = 1 + result.get(element, 0)
    print(result)

def count_word_counter(s):
    word_count = Counter(s.split(' '))
    print(word_count)

if __name__ == '__main__':
    s = "Hello world how are you I am fine and you"
    count_word(s)
    count_word_counter(s)