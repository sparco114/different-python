from html.parser import HTMLParser
from urllib.parse import urljoin


class LinkExtractor(HTMLParser):

    def __init__(self, base_url, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.links = []
        self.base_url = base_url

    def handle_starttag(self, tag, attrs):
        if tag not in ('link', 'script'):
            return
        attrs = dict(attrs)
        # print(tag, attrs)
        if tag == 'link':
            if 'rel' in attrs and attrs['rel'] == 'stylesheet':
                link = self._refine(attrs['href'])
                self.links.append(link)
        elif tag == 'script':
            if 'src' in attrs:
                link = self._refine(attrs['src'])
                self.links.append(link)

    def _refine(self, link):
        # print('link----', link)
        # print('joined link----', urljoin(self.base_url, link))
        return urljoin(self.base_url, link)
