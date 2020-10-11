# Given a line of letters and spaces, split it to parts
# so that each part is no longer than 10 symbols,
# the words of 10 symbols and less are never split,
# and there are no unnecessary splits.
section = ''


def add_section(result):
    """Add section if it exists"""
    global section
    if section:
        result.append(section.rstrip())
    section = ''


def split_string(string):
    string_words = string.split()
    result = []
    global section

    for word in string_words:
        word_length = len(word)
        section_length = len(section)

        if word_length == 10:
            add_section(result)
            result.append(word)
        elif word_length > 10:
            add_section(result)
            result += (word[:10], word[10:])
        else:
            if section_length + word_length >= 10:
                add_section(result)
            section += word + ' '

    add_section(result)

    return result


# print(split_string("what a disgusting food"))

