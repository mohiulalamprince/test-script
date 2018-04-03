file_pointer2 = open("social-network.csv", "w")

with open("/home/mohiulalamprince/Downloads/jazz.net") as file_pointer:
    for line in file_pointer:
        data = line.split()
        file_pointer2.write(data[0] + "," + data[1] + "\n")
    file_pointer2.close()
