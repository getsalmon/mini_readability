import requests

import article_scraper
import filesystem_worker
import format_rules

import txtmaker

url = 'https://docs.python.org/2/library/textwrap.html'

if __name__ == '__main__':
    raw_content = requests.get(url).content
    node_to_save = article_scraper.ArticleScraper(raw_content).\
        find_node_with_biggest_sentences_count()
    rules = {'a': format_rules.TagFormatRules.rule_for_a,
             'p': format_rules.TagFormatRules.rule_for_p}

    text = txtmaker.TxtMaker(node_to_save, rules).get_formatted_text()
    filesystem_worker.FileSystemWorker.save_page_to_txt_file(url, text, '.')
