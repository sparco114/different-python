# def parse_nok():
#     res = {}
#     with open('events-.txt', mode='r') as events:
#         prev_date = None
#         for line in events:
#             date = line[1:17]
#             if 'NOK' in line:
#                 if date == prev_date:
#                     res[date] += 1
#                 else:
#                     if prev_date:
#                         yield prev_date, res[prev_date]
#                     res[date] = 1
#                     prev_date = date
#         if prev_date:
#             yield prev_date, res[prev_date]


class ParseNokIter:

    def __init__(self, file_to_parse):
        self.file_to_parse = file_to_parse
        self.res = {}
        self.prev_date = None
        self.events = None

    def __iter__(self):
        self.res = {}
        self.events = open(self.file_to_parse, mode='r')
        self.prev_date = None
        return self

    def __next__(self):
        # res = {}
        self.prev_date = None
        for line in self.events:
            date = line[1:17]
            if 'NOK' in line:
                if date == self.prev_date:
                    self.res[date] += 1
                else:
                    if self.prev_date:
                        return self.prev_date, self.res[self.prev_date]
                    self.res[date] = 1
                    self.prev_date = date
        if self.prev_date:
            return self.prev_date, self.res[self.prev_date]
        else:
            raise StopIteration


grouped_events = ParseNokIter('events-.txt')
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
# with open('result.txt', mode='a') as ff:
#     ff.write(f'{group_time} {event_count}\n')
