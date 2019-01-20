import re
import bs4


class TxtMaker:
    def __init__(self, bs_tag: bs4.Tag, rules: dict = None):
        self.soup = bs4.BeautifulSoup(str(bs_tag).strip(), 'lxml')
        self.rules = rules if rules is not None else {}

    def _format_tags(self):
        for formatting_tag in self.rules:
            func = self.rules[formatting_tag]
            for child in self.soup.findAll(formatting_tag):
                func(child, self.soup)

    def _finalize_formatting(self):
        for br in self.soup.find_all('br'):
            br.replace_with('\n')
        text = self.soup.text
        text = re.sub('\r', '', text)
        text = re.sub('\n', '\r\n', text)
        text = re.sub('(\r\n){3,}', '\r\n\r\n', text)
        return text

    def get_formatted_text(self):
        self._format_tags()
        return self._finalize_formatting().strip()
