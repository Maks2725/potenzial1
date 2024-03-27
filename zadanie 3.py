f = open('students.csv', encoding='utf8')
a = f.readlines()
f.close()

shapka = a.pop(0)
for i in range(len(a)):
    a[i] = a[i].strip().split(',')

while True:
    l = input()
    f = 1
    for x in a:
        if x[0] == l:
            f, i, o = x[1].split()
            name = f'{i[0]}. {f}'
            print(f'Проект № {x[2]} делал: {name} он(а) получил(а) оценку - {x[-1]}')
            f = 0
    if f == 1:
        print('Ничего не найдено')


