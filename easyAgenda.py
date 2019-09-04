from ics import Calendar, Event
from ics.parse import ContentLine
from ics.utils import iso_to_arrow

calendar = Calendar()

def read_txt(filepath):
	for line in open(filepath):
		if len(line) == 11:
			date = line.replace('.', '')[:-1]
		else:
			if line[0] not in ['#', '-', '--', '//', '/']:
				start_time = line[0:5].replace(':', '')
				end_time = line[6:11].replace(':', '')
				event_name = line[12:-1]
				add_event(event_name, date, start_time, end_time)
	make_ics()

def add_event(event_name, date, start_time, end_time):
    global calendar
    event = Event()
    start = ContentLine.parse("DTSTART;TZID=Asia/Shanghai:{0}T{1}00".format(date, start_time))
    end = ContentLine.parse("DTSTART;TZID=Asia/Shanghai:{0}T{1}00".format(date, end_time))
    start_arr = iso_to_arrow(start)
    end_arr = iso_to_arrow(end)
    event.name = event_name
    event.begin = start_arr
    event.end = end_arr
    calendar.events.add(event)

def make_ics():
    global calendar
    with open('my.ics', 'w') as f:
        f.writelines(calendar)

if __name__ == "__main__":
    read_txt('agenda.txt')
    print("Success")
