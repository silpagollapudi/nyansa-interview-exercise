import datetime
import operator

filename = input('Enter a filename: ')
file = open(filename, "r")

if file.mode == 'r':
    data = file.read()

# process data
arr = data.split('\n')
for i in range(len(arr)):
    arr[i] = arr[i].split('|')
    if (arr[i] != ['']):
        epoch_time = float(arr[i][0])
        arr[i][0] = datetime.datetime.fromtimestamp((epoch_time)).strftime('%m/%d/%Y GMT')
arr.remove([''])
map = {}

# convert to map data structure
for i in range(len(arr)):
    curr = arr[i]
    converted_date = curr[0]
    url = curr[1]
    if converted_date not in map:
        map[converted_date] = [url]
    else:
        vals = map[converted_date]
        vals.append(url)
        map[converted_date] = vals

# print results
for k in map.keys():
    print(k)
    temp = {}
    for v in map[k]:
        if v not in temp:
            temp[v] = 1
        else:
            count = temp[v] + 1
            temp[v] = count
    sorted_temp = sorted(temp.items(), key=operator.itemgetter(1), reverse=True)
    for i in range(len(sorted_temp)):
        curr = sorted_temp[i]
        print curr[0] + " " + str(curr[1])
