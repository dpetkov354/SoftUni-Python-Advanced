from collections import defaultdict
from typing import DefaultDict


def get_char_count_map(s: str) -> DefaultDict[str, int]:
    occurrences: DefaultDict[str, int] = defaultdict(int)
    for c in s:
        occurrences[c] += 1
    return occurrences


def fmt_output(d: DefaultDict[str, int]) -> str:
    nl = '\n'
    return nl.join([f'{k}: {v} time/s' for k, v in sorted(d.items())])


def main() -> None:
    text = input()
    occurrences = get_char_count_map(text)
    print(fmt_output(occurrences))


main()
