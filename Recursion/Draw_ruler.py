def draw_line(length_ruler, label = ''):
    line = length_ruler * '-'
    if label:
        line += '' + str(label)
    print(line)

def draw_interval(length_ruler):
    if length_ruler > 0:
        draw_interval(length_ruler-1)
        draw_line(length_ruler)
        draw_interval(length_ruler-1)

def draw_ruler(length_label, length_ruler):
    draw_line(length_label, '0')
    for i in range(1, length_label + 1):
        draw_interval(length_ruler)
        draw_line(length_label, i)

if __name__ == '__main__':
    n =3
    draw_ruler(5, 3)
    