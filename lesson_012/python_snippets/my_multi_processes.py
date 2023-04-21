import requests
from termcolor import cprint
from threading import Thread
from my_utils import time_track
from my_extractor import LinkExtractor
from multiprocessing import Process, Queue

sites = [
    'https://www.fl.ru',
    'https://www.apple.com/',
    'https://www.udemy.com/',
    'https://www.python.org/',
    'https://www.vk.com/',
    'https://artstation.com/',
]


class PageSizer(Process):
    url_counter = 0
    process_counter = 0

    def __init__(self, url, collector, go_ahead=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = url
        self.go_ahead = go_ahead
        self.total_bytes = 0
        self.collector = collector
        PageSizer.process_counter += 1

    def run(self):
        self.total_bytes = 0
        html_data = self._get_html(self.url)
        if html_data is None:
            return
        self.total_bytes += len(html_data)
        PageSizer.url_counter += 1
        if self.go_ahead:
            extractor = LinkExtractor(self.url)
            extractor.feed(html_data)
            collector = Queue()
            sizs = [PageSizer(url=link, go_ahead=False, collector=collector) for link in extractor.links]
            for siz in sizs:
                print(f'Go {siz.url}')
                siz.start()
            for siz in sizs:
                siz.join()
            while not collector.empty():
                data = collector.get()
                self.total_bytes += data['total_bytes']
                PageSizer.url_counter += 1
        self.collector.put(dict(url=self.url, total_bytes=self.total_bytes, url_counter=self.url_counter, process_counter=PageSizer.process_counter))

    def _get_html(self, url):
        try:
            res = requests.get(url)
        except Exception as ex:
            cprint(str(ex), color='red')
        else:
            return res.text


@time_track
def main():
    full_url_counter = 0
    full_process_counter = 0
    collector = Queue()
    sizers = [PageSizer(url=url, collector=collector) for url in sites]

    for sizer in sizers:
        print(f'Go {sizer.url}')
        sizer.start()
    for sizer in sizers:
        sizer.join()

    while not collector.empty():
        data = collector.get()
        full_url_counter += data['url_counter']
        full_process_counter += data['process_counter']
        cprint(f"For {data['url']} need download {round(data['total_bytes'] / 1024, 2)} Kb", color='green')
    print('PageSizer--------', full_url_counter)
    print('full_url_counter--------', full_url_counter)


if __name__ == '__main__':
    main()
