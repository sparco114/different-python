import requests

from extractor import LinkExtractor
from utils import time_track

sites = [
    'https://www.fl.ru',
    'https://www.apple.com/',
    'https://www.udemy.com/',
    'https://www.python.org/',
    'https://www.vk.com/',
    'https://artstation.com/',
]


class PageSizer:

    def __init__(self, url):
        self.url = url
        self.total_bytes = 0

    def run(self):
        self.total_bytes = 0
        html_data = self._get_html(url=self.url)
        print(f'Go {self.url}...')
        if html_data is None:
            return
        self.total_bytes += len(html_data)
        extractor = LinkExtractor(base_url=self.url)
        extractor.feed(html_data)
        for link in extractor.links:
            extra_data = self._get_html(url=link)
            if extra_data:
                self.total_bytes += len(extra_data)

    def _get_html(self, url):
        try:
            res = requests.get(url)
        except Exception as exc:
            print(exc)
        else:
            return res.text


@time_track
def main():
    sizers = [PageSizer(url=url) for url in sites]

    for sizer in sizers:
        sizer.run()

    for sizer in sizers:
        print(f'For url {sizer.url} need download {sizer.total_bytes//1024} Kb ({sizer.total_bytes} bytes)')


if __name__ == '__main__':
    main()
