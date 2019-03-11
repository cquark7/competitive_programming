for tc in range(int(input())):
    inp = input().split()
    name = []
    for part in inp:
        name.append(part.title())
    if len(name) == 1:
        print(name[0])
    elif len(name) == 2:
        print('{}. {}'.format(name[0][0], name[1]))
    else:
        print('{}. {}. {}'.format(name[0][0], name[1][0], name[2]))
