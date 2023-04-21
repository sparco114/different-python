import requests
from termcolor import cprint
from threading import Thread
from my_utils import time_track
from my_extractor import LinkExtractor

sites = [
    'https://www.fl.ru',
    'https://www.apple.com/',
    'https://www.udemy.com/',
    'https://www.python.org/',
    'https://www.vk.com/',
    'https://artstation.com/',
]


class PageSizer(Thread):
    url_counter = 0
    thread_counter = 0

    def __init__(self, url, go_ahead=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = url
        self.total_bytes = 0
        self.go_ahead = go_ahead
        PageSizer.thread_counter += 1

    def run(self):
        html_data = self._get_html(self.url)
        if html_data is None:
            return
        self.total_bytes += len(html_data)
        if self.go_ahead:
            PageSizer.url_counter += 1
            extractor = LinkExtractor(self.url)
            extractor.feed(html_data)
            sizs = [PageSizer(url=link, go_ahead=False) for link in extractor.links]
            # pprint(extractor.links)
            for siz in sizs:
                print(f'Go {siz.url}')
                siz.start()
            for siz in sizs:
                siz.join()
            for siz in sizs:
                # print(f'    Go {siz.url}')
                # extra_data = self._get_html(siz.url)
                self.total_bytes += siz.total_bytes
                PageSizer.url_counter += 1

    def _get_html(self, url):
        try:
            res = requests.get(url)
        except Exception as ex:
            cprint(str(ex), color='red')
            pass
        else:
            return res.text


@time_track
def main():
    sizers = [PageSizer(url) for url in sites]

    for sizer in sizers:
        print(f'Go {sizer.url}')
        sizer.start()
    for sizer in sizers:
        sizer.join()

    for sizer in sizers:
        cprint(f'For {sizer.url} need download {round(sizer.total_bytes / 1024, 2)} Kb', color='green')


if __name__ == '__main__':
    main()
    print('PageSizer--------', PageSizer.url_counter)
    print(f'thread_counter-------{PageSizer.thread_counter}')
