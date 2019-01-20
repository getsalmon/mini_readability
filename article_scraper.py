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
        self.cleanup_soup()

    def cleanup_soup(self):
        """
        Очищаем контент от стоп-тэгов
        :return:
        """
        for el in self.soup(self.stop_tag_names):
            el.extract()

    def find_node_with_biggest_sentences_count(self) -> bs4.Tag:
        """
        Будем искать узел в котором наибольшее количество предложений.
        Узел при этом должен быть из пула тэгов self.container_tagnames
        :return:
        """
        body = self.soup.find('body')
        search_state = SearchState()
        self.search_for_tag_recursively(body, search_state)
        return search_state.found_tag

    def search_for_tag_recursively(self, root: bs4.Tag,
                                   search_state: SearchState):
        """
        Рекурсивный обход дерева
        1. Рекурсивно ищем узлы из пула тэгов self.container_tagnames
        2. Если узел не имеет потомков из пула self.container_tagnames,
        то считаем в этом узле кол-во предложений и удаляем этот узел из DOM
        3. Возращаемся в предка
        4. Goto 2

        :param root: Корень, из которого будем производить поиск
        :param search_state: Состояние поиска
        :return:
        """
        # re для предложений
        sentence_regex = r"\s*[^.!?]*[.!?]"

        for child in root.find_all(recursive=False):
            self.search_for_tag_recursively(child, search_state)
            if child.name in self.container_tagnames:

                current_sentence_count = len(list(re.findall(sentence_regex,
                                                             child.text)))
                child.extract()
                if current_sentence_count > search_state.sentences_count:
                    search_state.sentences_count = current_sentence_count
                    search_state.found_tag = child


