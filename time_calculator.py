def add_time(start, duration, starting_day=''):
    splits = start.split()
    time = splits[0]
    is_am = True if splits[1] == 'AM' else False
    splits = time.split(':')
    hour = int(splits[0])
    minutes = int(splits[1])
    splits = duration.split(':')
    hour_to_add = int(splits[0])
    minutes_to_add = int(splits[1])

    hour += 0 if is_am else 12
    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    min_res = (minutes + minutes_to_add)
    if min_res > 59:
        hour_to_add += 1
    min_res = int(min_res % 60)
    hour_res = (hour + hour_to_add) % 24

    if hour_res >= 12:
        hour_res -= 12
        is_am = False
    else:
        is_am = True
    cant_days = int((hour + hour_to_add) / 24)

    week_day = ''
    if starting_day != '':
        if cant_days == 0:
            week_day = ', ' + starting_day.capitalize()
        else:
            move_week = cant_days % 7
            week_index = week.index(starting_day.capitalize())
            week_day = ', ' + week[move_week + week_index - 7]

    result = str(hour_res if hour_res != 0 else 12) + ':' + str(min_res).rjust(2 if min_res < 10 else 0, '0') + (
        ' AM' if is_am else ' PM') + week_day
    if cant_days > 0:
        result += ' (' + str(cant_days) + ' days later)' if cant_days > 1 else ' (next day)'

    return result
