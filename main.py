import article_scraper
import format_rules

import misc
import txtmaker

url = 'https://habr.com/ru/post/436698/'

if __name__ == '__main__':
    content = misc.get_content_from_url(url)
    tag = article_scraper.ArticleScraper(
        content).find_best_tag_by_sentences_count()
    rules = {'a': format_rules.TagFormatRules.rule_for_a,
             'p': format_rules.TagFormatRules.rule_for_p}
    text = txtmaker.TxtMaker(tag, rules).get_formatted_text()
    print(text)
