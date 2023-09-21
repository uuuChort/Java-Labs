def find_max_height(num_roads, roads_data):
    max_height = 0
    road_number = 0

    for i in range(num_roads):
        tunnels = roads_data[i][0]
        max_tunnel_height = max(roads_data[i][1:])
        if max_tunnel_height > max_height:
            max_height = max_tunnel_height
            road_number = i + 1

    return road_number, max_height

#чтение данных
num_roads = int(input("Введите количество дорог: "))

roads_data = []
for i in range(num_roads):
    tunnels = int(input("Введите количество туннелей для дороги {}: ".format(i + 1)))
    tunnel_heights = list(map(int, input("Введите высоты туннелей через пробел: ").split()))
    roads_data.append([tunnels] + tunnel_heights)

#поиск макс высоты и номера
road_number, max_height = find_max_height(num_roads, roads_data)

#вывод
print("Наибольшая высота грузовика: {}".format(max_height))
print("Номер дороги для наибольшей высоты: {}".format(road_number))
