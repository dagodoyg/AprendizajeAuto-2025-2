def reader(filepath: str, data_x, data_y):
    with open(filepath, "r") as file:
        data = file.readlines()
        for d in data:
            temp = d.split()
            temp = [float(temp[0]), float(temp[1])]
            data_x.append(temp[0])
            data_y.append(temp[1])
    return

data_x = []
data_y = []

reader("data.txt", data_x, data_y)

print(data_x)
print(data_y)
A = 0.5*( data_x[1]*data_y[2] - data_x[2]*data_y[1] - data_x[0]*data_y[2] + data_x[2]*data_y[0] + data_x[0]*data_y[1] - data_x[1]*data_y[0])

print(A)
