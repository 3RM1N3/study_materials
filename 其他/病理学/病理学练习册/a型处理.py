def f_ans(s):
    s = s.replace('.', '')
    s = s.replace(' ', '')
    s = s.replace('A', '.A ')
    s = s.replace('B', '.B ')
    s = s.replace('C', '.C ')
    s = s.replace('D', '.D ')
    s = s.replace('E', '.E ')
    s = s.strip()
    return s


def f1():
    with open('a型处理前.txt', 'r', encoding='UTF-8') as f1,\
        open('a型处理后.txt', 'w', encoding='UTF-8') as f2:

        lines = f1.readlines()
        for l in lines:
            l = l.strip()
            if l[0] in '123456789ABCDE':
                f2.write('\n' + l)
            else:
                f2.write(l)


def f2(ans):
    with open('a型处理前.txt', 'w', encoding='UTF-8') as f4,\
        open('a型处理后.txt', 'r', encoding='UTF-8') as f3:
        
        index = 0
        
        ans_list = ans.split(' ')
        lines = f3.readlines()
        for l in lines:
            if l[0] in '123456789':
                index = int(l.split('.')[0]) - 1
                f4.write(l.replace('\n', '@'))
            elif l[0] == ans_list[index].split('.')[1]:
                if ans_list[index].split('.')[0] == str(index+1):
                    f4.write(l[2:])
                else:
                    print(index)


# main
# 定义答案字符串
ans = '1.C 2.A 3.C 4.C 5.A 6.D 7.D 8.B 9.C 10.C 11.D 12.C 13.E 14.C 15.A 16.B 17.D 18.A 19.A 20.E 21.A 22.D23.A 24.E'

f1()
f2(f_ans(ans))