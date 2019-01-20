class TagFormatRules:
    """
    Описание правил форматирования тэгов
    """
    @staticmethod
    def rule_for_p(elem, soup):
        TagFormatRules.add_new_line(elem, soup)

    @staticmethod
    def rule_for_a(elem, _):
        if elem.attrs.get('href') is not None:
            elem.replace_with(f"[{elem.attrs['href']} | {elem.text}]")
        else:
            elem.replace_with(elem.text)

    @staticmethod
    def rule_for_header(elem, soup):
        TagFormatRules.add_new_line(elem, soup)

    @staticmethod
    def add_new_line(elem, soup):
        elem.insert_after(soup.new_tag('br'))
        elem.insert_after(soup.new_tag('br'))
