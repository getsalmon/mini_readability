import re
import textwrap

import bs4


class TxtMaker:
    def __init__(self, bs_tag: bs4.Tag, formatting_rules: dict = None):
        self.soup = bs4.BeautifulSoup(str(bs_tag), 'lxml')
        self.rules = formatting_rules or {}

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

    @staticmethod
    def _wrap_text(text, line_len):
        return '\n'.join('\n'.join(textwrap.wrap(x, width=80))
                         for x in text.split('\n'))

    def get_formatted_text(self):
        self._replace_html_tags_with_text()
        self._replace_br_tags_with_newlines()
        text = self._delete_unnecessary_newline_chars()
        text = self._wrap_text(text)
        return text.strip()
