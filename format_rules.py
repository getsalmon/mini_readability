
class TagFormatRules:
    """
    Описание правил форматирования тэгов
    """

    @staticmethod
    def rule_for_p(elem, soup):
        TagFormatRules._add_empty_line(elem, soup)

    @staticmethod
    def common_rule_for_header(elem, soup):
        TagFormatRules._add_empty_line(elem, soup)

    @staticmethod
    def markdown_rule_for_header(elem, soup):
        TagFormatRules._add_empty_line(elem, soup)
        number_of_hashtags = int(elem.name[1])
        elem.replace_with('#' * number_of_hashtags + ' ' + elem.text)

    @staticmethod
    def common_rule_for_a(elem, _):
        if elem.attrs.get('href') is not None:
            elem.replace_with(f"{elem.text.strip()} [{elem.attrs['href']}]")
        else:
            elem.replace_with(elem.text)

    @staticmethod
    def alternative_rule_for_a(elem, _):
        if elem.attrs.get('href') is not None:
            elem.replace_with(f"[{elem.attrs['href']} | {elem.text.strip()}]")
        else:
            elem.replace_with(elem.text)

    @staticmethod
    def markdown_rule_for_a(elem, _):
        if elem.attrs.get('href') is not None:
            elem.replace_with(f"[{elem.text.strip()}]({elem.attrs['href']})")
        else:
            elem.replace_with(elem.text)

    @staticmethod
    def rule_for_header(elem, soup):
        TagFormatRules._add_empty_line(elem, soup)

    @staticmethod
    def _add_empty_line(elem, soup):
        elem.insert_after(soup.new_tag('br'))
        elem.insert_after(soup.new_tag('br'))
