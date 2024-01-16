# with open("weather_data (1).csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data (1).csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data (1).csv")
# print(data)
# print(type(data))
# print(data["temp"])
# print(data.temp)

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(len(temp_list))

# average = sum(temp_list)/ len(temp_list)
# print(average)
# print(data["temp"].mean())

# get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# create data from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "Scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
# print(data)
data.to_csv("new_data.csv")