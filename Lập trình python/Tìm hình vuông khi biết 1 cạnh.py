import math

a = list(map(int, input().split()))
b = list(map(int, input().split()))

vector = [b[0] - a[0], b[1] - a[1]]

def timToaDo1():
    list = []
    list.append([a[0], a[1]])
    list.append([a[0] - vector[1], a[1] + vector[0]])
    list.append([b[0], b[1]])
    list.append([b[0] - vector[1], b[1] + vector[0]])
    return list

def timToaDo2():
    list = []
    list.append([a[0], a[1]])
    list.append([a[0] + vector[1], a[1] - vector[0]])
    list.append([b[0], b[1]])
    list.append([b[0] + vector[1], b[1] - vector[0]])
    return list

def tinhTamHinhVuong(points):
    x_center = sum(point[0] for point in points) / 4
    y_center = sum(point[1] for point in points) / 4
    return (x_center, y_center)

def sapXepToaDo(start_point, points):
    start_x, start_y = start_point
    center = tinhTamHinhVuong(points)
    center_x, center_y = center

    def angle_from_center(point):
        x, y = point
        angle_point = math.atan2(y - center_y, x - center_x)
        angle_start = math.atan2(start_y - center_y, start_x- center_x)
        angle_diff = angle_start - angle_point
        if angle_diff < 0:
            angle_diff += 2 * math.pi
        return angle_diff

    sorted_points = sorted(points, key=angle_from_center)

    return sorted_points

list1 = timToaDo1()
list2 = timToaDo2()

list1 = sapXepToaDo(a, list1)
list2 = sapXepToaDo(a, list2)

result = ' '.join(f'({x}, {y})' for x, y in list1)
print(result)
result = ' '.join(f'({x}, {y})' for x, y in list2)
print(result)
    