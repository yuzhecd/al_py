
def permletter(words, rules):
    rules = rules.lower()
    for rule in rules:
        keys.add(rule)
    perm_helper(words, keys, 0, '')
    print(results)

def perm_helper(words, keys, index, prefix):
    length = len(words)
    for i in range(index, length):
        c = words[i]
        if c in keys:
            perm_helper(words, keys, i+1, prefix+c)

            c = c.upper()
            perm_helper(words, keys, i+1, prefix+c)
        else:
            prefix = prefix+c

    if (len(prefix)==len(words)):
        results.add(prefix)

if __name__ == '__main__':
    words = 'medium-one'
    rules = 'nm'
    results = set()
    keys = set()
    permletter(words, rules)