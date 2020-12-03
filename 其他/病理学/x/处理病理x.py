questions_dict = {}
q = ''

with open('病理x未去重.txt', 'r', encoding='UTF-8') as f1, \
    open('病理完整.txt', 'w', encoding='UTF-8') as f2:

    lines = f1.readlines()

    for l in lines:
        if l[0] in '123456789':
            q = l.split('.')[1]
            questions_dict[q] = []
        else:
            questions_dict[q].append(l)

    print(len(questions_dict))

    for k, v in questions_dict.items():
        f2.write(k)
        for i in v:
            f2.write(i)
        f2.write('\n')