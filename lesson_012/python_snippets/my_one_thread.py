import requests
from termcolor import cprint

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


class PageSizer:
    url_counter = 0

    def __init__(self, url):
        self.url = url
        self.total_bytes = 0

    def run(self, url_counter=url_counter):
        html_data = self._get_html(self.url)
        if html_data is None:
            return
        self.total_bytes += len(html_data)
        extractor = LinkExtractor(self.url)
        extractor.feed(html_data)
        PageSizer.url_counter += 1
        # pprint(extractor.links)
        for link in extractor.links:
            # print(f'    Go {link}')
            extra_data = self._get_html(link)
            # print('--------------', extra_data)
            if extra_data:
                self.total_bytes += len(extra_data)
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
        sizer.run()

    for sizer in sizers:
        cprint(f'For {sizer.url} need download {round(sizer.total_bytes / 1024, 2)} Kb', color='green')


if __name__ == '__main__':
    main()
    print('PageSizer--------', PageSizer.url_counter)
