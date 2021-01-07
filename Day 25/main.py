# with open('weather_data.csv') as file:
#     data = file.readlines()
#     print(data)

import csv

# with open('weather_data.csv') as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] == 'temp':
#             pass
#         else:
#             temperatures.append(int(row[1]))
#     # for row in data:
#     #     print(row)
#     #     print(row[1])
#     print(temperatures)
#
import pandas

data = pandas.read_csv('weather_data.csv')
# # print(data['temp'])
# temp_list = data['temp'].to_list()
# average1 = sum(data['temp'])/len(data)
# average2 = sum(temp_list)/len(temp_list)
# maxi = max(data['temp'])
# print(maxi)
# print(average1)
# print(average2)

# print(data[data.temp == data['temp'].max()])
monday = data[data['day'] == 'Monday']
monday_temp = monday['temp']
monday_temp = (monday_temp * 9/5) + 32
print(monday_temp)