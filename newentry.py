import datetime

d = datetime.datetime.now()
action = input('w for waking up, s for sleeping: ')
with open('./data/sleepandwaketimes.txt', mode='a') as f:
    if action == 'w':
        f.write('w ')
        f.write(d.strftime('%c') + '\n')
    elif action == 's':
        f.write('s ')
        f.write(d.strftime('%c') + '\n')
    else:
        print('Not valid')