import datetime
with open('./data/sleepandwaketimes.txt', 'r') as f:
    data = [line for line in f]
    
wake = [i[2:-1] for i in data if i.startswith('w')]
sleep = [j[2:-1] for j in data if j.startswith('s')]

wakedt = datetime.datetime.strptime(wake[0], '%c')

sleepdt = datetime.datetime.strptime(sleep[0], '%c')

sleeptime = wakedt - sleepdt
print(sleeptime)
