def find_day(volume, inject):
    i = 0
    while volume > 0:
        i += 1
        volume += inject
        if volume > 5:
            volume = 5
            volume -= i
        else:
            volume -= i
    return i

if __name__ == '__main__':
    result = find_day(5, 2)
    print(result)