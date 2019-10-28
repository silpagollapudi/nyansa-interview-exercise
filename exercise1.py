import datetime

filename = input('Enter a filename: ')
file = open(filename, "r")

map = {}
for line in file:
    curr = line.split("|")
    epoch_time = curr[0]
    url = curr[1]
    converted_date = datetime.datetime.fromtimestamp(float(epoch_time)).strftime('%m/%d/%Y GMT')
    if converted_date not in map:
        map[converted_date] = [url]
    else:
        vals = map[converted_date]
        vals.append(url)
        map[converted_date] = vals


for k in map.keys():
    print(k)
    temp = {}
    for v in map[k]:
        if v not in temp:
            temp[v] = 1
        else:
            count = temp[v] + 1
            temp[v] = count
    for k, v in temp.items():
        print k.strip() + " " + str(v)
