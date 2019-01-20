import argparse

import article_scraper
import config
import filesystem_worker
import misc
import txtmaker

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url', type=str, help='ссылка на статью, которую нужно'
                                              'сохранить')
    args = parser.parse_args()
    url = args.url

    raw_content = misc.get_content_from_url(url)
    if config.verbose:
        print('статья скачана')
    scraper = article_scraper.ArticleScraper(raw_content, url)
    node_to_save = scraper.find_node_with_biggest_sentences_count()
    if config.verbose:
        print('найден нужный узел в DOM')
    rules = config.get_rules()
    text = txtmaker.TxtMaker(node_to_save,
                             rules,
                             wrap_len=config.max_len,
                             title=scraper.title).get_formatted_text()
    if config.verbose:
        print('статья преобразована в текстовый вид')
    if config.output_to_console:
        print('\n' + text)
    else:
        filesystem_worker.FileSystemWorker. \
            save_page_to_txt_file(url, text, config.base_folder,
                                  extension=config.get_extension())
        if config.verbose:
            print(f'статья сохранена')
