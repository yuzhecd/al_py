def reverse_string(string_use):
    n = len(string_use)
    list_string = list(string_use)
    for i in range(n // 2):
        list_string[i], list_string[n-1-i] = list_string[n-1-i], list_string[i]

    final_string = ''.join(list_string)

    print(final_string)

if __name__ == '__main__':
    string_use = input('Please input a string: ')
    reverse_string(string_use)