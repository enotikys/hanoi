COLORS = [i + 31 for i in range(5)] * 4


def input_params_and_start_alg():
    temporary_variable = 6
    disks = int(input('Введите количество дисков от 3 до 20: '))
    towers = int(input('Введите количество башен от 3 до 10: '))
    start_t = int(input('Введите номер начальной башни: '))
    finish_t = int(input('Введите номер конечной башни: '))
    while True:
        temp = temporary_variable - start_t - finish_t
        if temp <= 0 or temp == start_t or temp == finish_t:
            temporary_variable += 1
        else:
            break
    towers = generate_start_towers(disks, towers, start_t)
    hanoi_algorithm(disks, start_t, finish_t, towers, temporary_variable, disks)


def generate_start_towers(n_disks, n_towers, start):
    towers = [[] for _ in range(n_towers)]
    towers[start - 1] = [i + 1 for i in reversed(range(n_disks))]
    print_towers(towers, n_disks)
    return towers


def hanoi_algorithm(n, start, finish, towers, temporary_variable, count_disks):
    if n <= 0:
        return
    temp = temporary_variable - start - finish
    hanoi_algorithm(n - 1, start, temp, towers, temporary_variable, count_disks)
    towers[finish - 1].append(towers[start - 1][-1])
    towers[start - 1].pop(-1)
    print_towers(towers, count_disks)
    hanoi_algorithm(n - 1, temp, finish, towers, temporary_variable, count_disks)


def print_towers(towers, count_disks):
    input()
    for i in reversed(range(count_disks)):
        for j in range(len(towers)):
            try:
                string = int(towers[j][i]) * '■'
                color_code = f'\033[{COLORS[towers[j][i] - 1]}m ' + '{:<' + str(count_disks) + '}'
                print(color_code.format(string), end='')
            except IndexError:
                format_string = '\033[37m {:<' + str(count_disks) + '}'
                print(format_string.format('|'), end='')
        print()
    print()


if __name__ == '__main__':
    input_params_and_start_alg()