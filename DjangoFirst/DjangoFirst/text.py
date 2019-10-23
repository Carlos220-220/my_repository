def get_num():
    strings = ''
    for c in range(1, 10):
        if c % 2 == 0:
            strings += '<tr class="two">'
        else:
            strings += '<tr class="one">'
        for r in range(1, c + 1):
            strings += ('<td>{}*{}={:<2}</td>'.format(r, c, r * c))
        strings += '</tr>'

    return strings

print(get_num())