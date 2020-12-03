def f_ans(s):
    '''处理答案字符串'''

    s = s.replace('.', '')
    s = s.replace(' ', '')
    s = s.replace('A', '.A ')
    s = s.replace('B', '.B ')
    s = s.replace('C', '.C ')
    s = s.replace('D', '.D ')
    s = s.replace('E', '.E ')
    s = s.strip()
    d = {}
    for i in s.split(' '):
        d[i.split('.')[0]] = i.split('.')[1]
    return d


def f1():
    '''保证题目在同一行'''

    with open('b型处理前.txt', 'r', encoding='UTF-8') as f1,\
        open('b型处理后.txt', 'w', encoding='UTF-8') as f2:

        lines = f1.readlines()
        for l in lines:
            l = l.strip()
            if l[0] in '123456789ABCDE':
                f2.write('\n' + l)
            else:
                f2.write(l)


def f2(d):
    '''保证题目在同一行'''

    with open('b型处理前.txt', 'w', encoding='UTF-8') as f2,\
        open('b型处理后.txt', 'r', encoding='UTF-8') as f1:

        ans_dict = {}
        lines = f1.readlines()
        for l in lines[1:]:
            l = l.strip()
            if l[0] in 'ABCDE':
                ans_dict[l[0]] = l[2:]
            elif l[0] in '123456789':
                f2.write(l + '@')
                f2.write(ans_dict[d[l.split('.')[0]]] + '\n')
                

# main
ans = '\
    25.E 26.BD 27.A 28.B 29.D 30.B 31.A'
f1()
f2(f_ans(ans))