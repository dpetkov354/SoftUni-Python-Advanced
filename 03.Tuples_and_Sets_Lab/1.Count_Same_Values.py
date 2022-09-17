from collections import defaultdict
from typing import DefaultDict, List


def get_occurrence(nums: List[float]) -> dict:
    occurrence: DefaultDict = defaultdict(int)
    for num in nums:
        occurrence[num] += 1
    return occurrence


def fmt_occurrence(occurrence: dict) -> str:
    result = []
    nl = '\n'
    for num, count in occurrence.items():
        result.append(f'{num} - {count} times')
    return nl.join(result)


def main() -> None:
    numbers = list(map(float, input().split()))
    occurrence = get_occurrence(numbers)
    print(fmt_occurrence(occurrence))


main()
