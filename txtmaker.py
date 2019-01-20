import re
import textwrap

import bs4


class TxtMaker:
    def __init__(self,
                 bs_tag: bs4.Tag,
                 formatting_rules: dict = None,
                 wrap_len: int = 80,
                 title: str = None):
        self.soup = bs4.BeautifulSoup(str(bs_tag), 'lxml')
        self.rules = formatting_rules or {}
        self.wrap_len = wrap_len
        self.title = title

    def _replace_html_tags_with_text(self):
        for tag_to_format in self.rules:
            reformat_function = self.rules[tag_to_format]
            for child in self.soup.findAll(tag_to_format):
                reformat_function(child, self.soup)

    def _replace_br_tags_with_newlines(self):
        [br.replace_with('\n') for br in self.soup.find_all('br')]

    def _delete_unnecessary_newline_chars(self):
        text = self.soup.text
        text = re.sub('\r', '', text)
        text = re.sub('\n{3,}', '\n\n', text)
        return text

    def _wrap_text(self, text):
        return '\n'.join('\n'.join(textwrap.wrap(x, width=self.wrap_len))
                         for x in text.split('\n'))

    def get_formatted_text(self):
        self._replace_html_tags_with_text()
        self._replace_br_tags_with_newlines()
        text = self._delete_unnecessary_newline_chars()
        if self.title:
            text = self.title + '\n\n' + text.strip()
        text = self._wrap_text(text)

        return text.strip()
