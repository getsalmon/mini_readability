import format_rules

markdown = False
max_len = 80
base_folder = 'articles'
stop_tag_names = ['script', 'img', 'svg',
                  'meta', 'link', 'nav', 'iframe']
container_tagnames = ['div', 'article', 'main', 'section']
output_to_console = True
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' \
             '(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
verbose = True

#################################

common_rules = {'p': format_rules.TagFormatRules.rule_for_p,
                'a': format_rules.TagFormatRules.common_rule_for_a,
                'h1': format_rules.TagFormatRules.common_rule_for_header,
                'h2': format_rules.TagFormatRules.common_rule_for_header,
                'h3': format_rules.TagFormatRules.common_rule_for_header,
                'h4': format_rules.TagFormatRules.common_rule_for_header,
                'h5': format_rules.TagFormatRules.common_rule_for_header,
                'h6': format_rules.TagFormatRules.common_rule_for_header,
                }

markdown_rules = {'p': format_rules.TagFormatRules.rule_for_p,
                  'a': format_rules.TagFormatRules.markdown_rule_for_a,
                  'h1': format_rules.TagFormatRules.markdown_rule_for_header,
                  'h2': format_rules.TagFormatRules.markdown_rule_for_header,
                  'h3': format_rules.TagFormatRules.markdown_rule_for_header,
                  'h4': format_rules.TagFormatRules.markdown_rule_for_header,
                  'h5': format_rules.TagFormatRules.markdown_rule_for_header,
                  'h6': format_rules.TagFormatRules.markdown_rule_for_header}


def get_rules():
    if markdown:
        return markdown_rules
    else:
        return common_rules


def get_extension():
    return 'md' if markdown else 'txt'
