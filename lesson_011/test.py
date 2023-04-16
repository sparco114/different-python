def parse_nok():
    res = {}
    with open('events-.txt', mode='r') as events:
        prev_date = None
        for line in events:
            date = line[1:17]
            if 'NOK' in line:
                if date == prev_date:
                    res[date] += 1
                else:
                    if prev_date:
                        yield prev_date, res[prev_date]
                    res[date] = 1
                    prev_date = date
        if prev_date:
            yield prev_date, res[prev_date]


grouped_events = parse_nok()
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
    # with open('result.txt', mode='a') as ff:
    #     ff.write(f'{group_time} {event_count}\n')

