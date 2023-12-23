import csv, os, schedule
from __main__ import notification
from __main__ import get_sound

def read_reminders():
    with open('c:/devel/no-clock-python/misc/reminders.txt') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';',skipinitialspace=True)

        for row in reader:
            if row['enabled'] == 'true':
                eval ('schedule.' +  row['repeat'] + '.do(notification,msg="' + row['msg'] + '", icon="' + row['icon'] + '", once="' + row['once'] + '")')

def main():
    read_reminders()
