def find_treasure(x_treasure, y_treasure):
    x, y = 0, 0  #начальное положение в точке (0 0)
    steps = 0  #кличество шагов

    while (x, y) != (x_treasure, y_treasure):
        direction = input().strip()
        distance = int(input().strip())

        if direction == 'север':
            y += distance
        elif direction == 'юг':
            y -= distance
        elif direction == 'восток':
            x += distance
        elif direction == 'запад':
            x -= distance

        steps += 1

    return steps

#чтение координат 
x_treasure, y_treasure = map(int, input().split())

#поиск и вывод
min_steps = find_treasure(x_treasure, y_treasure)
print(min_steps)
