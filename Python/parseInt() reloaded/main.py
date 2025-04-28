def parse_word_int(text_number: str) -> int:
    en_numbers: dict[str, int] = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        'eleven': 11,
        'twelve': 12,
        'thirteen': 13,
        'fourteen': 14,
        'fifteen': 15,
        'sixteen': 16,
        'seventeen': 17,
        'eighteen': 18,
        'nineteen': 19,
        'twenty': 20,
        'thirty': 30,
        'forty': 40,
        'fifty': 50,
        'sixty': 60,
        'seventy': 70,
        'eighty': 80,
        'ninety': 90,
    }

    return en_numbers[text_number]


def parse_separator(sep: str, words: list[str]) -> int:
    en_seps: dict[str, int] = {
        'million': 1000000,
        'thousand': 1000,
        'hundred': 100,
    }

    ix: int = words.index(sep)
    return en_seps[sep] * parse_int(' '.join(words[:ix])) + parse_int(' '.join(words[ix + 1 :]))


def parse_int(text_number: str) -> int:
    words: list[str] = text_number.replace('-', ' ').split()

    for sep in ['million', 'thousand', 'hundred']:
        if sep in words:
            return parse_separator(sep, words)

    result: int = 0
    for word in words:
        if word == 'and':
            continue
        result += parse_word_int(word)

    return result


def tests() -> None:
    tests: list[str] = [
        'zero',
        'twenty',
        'two hundred forty-six',
        'seven hundred eighty-three thousand nine hundred and nineteen',
        'one million',
        'twenty five hundred',
    ]

    for test in tests:
        print(test, parse_int(test))


if __name__ == '__main__':
    tests()
