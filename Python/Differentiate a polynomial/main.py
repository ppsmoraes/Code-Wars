import re


def differentiate(equation: str, point: int) -> int:
    result: int = 0

    terms: list[str] = re.findall(r'([+-]?\d*)x\^?(\d*)', equation)

    for term in terms:
        coef, exp = term

        if not coef:
            coef = '1'
        elif coef in ['+', '-']:
            coef = coef + '1'

        if not exp:
            exp = '1'

        diff_coef: int = int(exp) * int(coef)
        diff_exp: int = int(exp) - 1

        term_point: int = diff_coef * point**diff_exp

        result += term_point

    return result
