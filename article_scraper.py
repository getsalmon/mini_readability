import re
import bs4


class SearchState:
    def __init__(self):
        self.sentences_count = 0
        self.found_tag = None


class ArticleScraper:
    def __init__(self, content):
        self.stop_tag_names = ['script', 'img', 'svg',
                               'meta', 'link', 'nav', 'iframe']
        self.container_tagnames = ['div', 'article', 'main', 'section']
        self.soup = bs4.BeautifulSoup(content, 'lxml')

    def cleanup_soup(self):
        """
        Очищаем контент от стоп-тэгов
        :return:
        """
        for el in self.soup(self.stop_tag_names):
            el.extract()

    def find_best_tag_by_sentences_count(self) -> bs4.Tag:
        """
        Будем идти максимально вглубь DOM и искать элементы обозначенных
        выше тэгов с наиб. кол-вом предложений
        Предложения будем искать регвыром
        :return:
        """
        body = self.soup.find('body')
        search_state = SearchState()
        self.traverse_dom_and_search_tag(body, search_state)
        return search_state.found_tag

    def traverse_dom_and_search_tag(self, root: bs4.Tag,
                                    search_state: SearchState):
        """
        Рекурсивный обход дерева
        Максимально углубляемся в дерево. Если нашли нужный тэг,
        то считаем в нем количество предложений и,
        если оно больше текущего, запоминаем этот тэг как искомый

        :param root: Корень, из которого будем производить поиск
        :param search_state: Состояние поиска
        :return:
        """
        # re для предложений
        # https://stackoverflow.com/a/20320820
        sentence_regex = r"\s*[^.!?]*[.!?]"

        for child in root.findChildren(recursive=False):
            self.traverse_dom_and_search_tag(child, search_state)
            if child.name in self.container_tagnames:
                current_tag = child.extract()
                current_sentence_count = len(list(re.findall(sentence_regex,
                                                             child.text)))
                if current_sentence_count > search_state.sentences_count:
                    search_state.sentences_count = current_sentence_count
                    search_state.found_tag = current_tag


