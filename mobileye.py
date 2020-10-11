# Given a line of letters and spaces, split it to parts
# so that each part is no longer than 10 symbols,
# the words of 10 symbols and less are never split,
# and there are no unnecessary splits.

class SpecialString:
    def __init__(self, string):
        self.result = []
        self.string_words = string.split()
        self.section = ''
        
    def add_section(self):
        if self.section:
            self.result.append(self.section.rstrip())
        self.section = ''

    def add_result(self, *args):
        """Accept variable number of arguments to simplify appending to results array"""
        self.result += args


def split_string(string):
    string = SpecialString(string)

    for word in string.string_words:
        word_length = len(word)
        section_length = len(string.section)

        if word_length == 10:
            string.add_section()
            string.add_result(word)
        elif word_length > 10:
            string.add_section()
            string.add_result(word[:10], word[10:])
        else:
            if section_length + word_length >= 10:
                string.add_section()
            string.section += word + ' '

    string.add_section()

    return string.result
