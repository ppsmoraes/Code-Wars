import math


def get_frequencies(numbers: list[int]) -> dict[int, int]:
    frequency: dict[int, int] = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1

    return frequency


def divide(dividend: int, divisor: int) -> bool:
    return dividend % divisor == 0


def factor_into_primes(number: int) -> list[int]:
    result: list[int] = []

    max_prime: int = math.floor(math.sqrt(number))
    min_prime: int = 2

    while min_prime <= max_prime:
        if divide(number, min_prime):
            result.append(min_prime)

            max_prime = int(number / min_prime)
            result.extend(factor_into_primes(max_prime))
            break

        min_prime += 1

    if len(result) == 0:
        result = [number]

    return result


def zeroes(base: int, number: int) -> int:
    base_div_dict: dict[int, int] = get_frequencies(factor_into_primes(base))

    div_list: list[int] = []

    for p in base_div_dict.keys():
        for num in range(1, number + 1):
            cache_num: int = num
            while divide(cache_num, p):
                div_list.append(p)
                cache_num = int(cache_num / p)

    div_dict: dict[int, int] = get_frequencies(div_list)

    return math.floor(
        min(div_dict.get(p, 0) / freq for p, freq in base_div_dict.items())
    )
