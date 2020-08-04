
# author: https://blog.furas.pl
# date: 2020.08.03
# link: https://stackoverflow.com/questions/63225718/pyparsing-precedence-breaks-with-unary-operator/

import pyparsing

variable_names = pyparsing.Combine(pyparsing.Literal('$') + pyparsing.Word(pyparsing.alphanums + '_'))

integer = pyparsing.Word(pyparsing.nums)

double = pyparsing.Combine(pyparsing.Word(pyparsing.nums) + '.' + pyparsing.Word(pyparsing.nums))

parser = pyparsing.operatorPrecedence(
            variable_names | double | integer,
            [
                ('-',  1, pyparsing.opAssoc.RIGHT),
                ('**', 2, pyparsing.opAssoc.RIGHT),
                (pyparsing.oneOf('* / // %'), 2, pyparsing.opAssoc.LEFT),
                (pyparsing.oneOf('+ -'), 2, pyparsing.opAssoc.LEFT),
                (pyparsing.oneOf('> >= < <= == !='), 2, pyparsing.opAssoc.LEFT),
                ('not', 1, pyparsing.opAssoc.RIGHT),
                ('and', 2, pyparsing.opAssoc.LEFT),
                ('or',  2, pyparsing.opAssoc.LEFT)
            ]
        )

examples = [
    "5 * 10 ** -2",
    "5 * 10 * -2",
    "5 * 10 ** (-2)",
    "5 * -10 ** 2",
    "5 * (-10) ** 2",    
    "5 and not 8",
    "5 and -8",
    "1 ** -2",
    "-1 ** 2",
]

longest = max(map(len, examples))

for ex in examples:
    result = parser.parseString(ex)
    print(f'{ex:{longest}}  <=>  {result}')

