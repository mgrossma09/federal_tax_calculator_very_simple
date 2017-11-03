#!/usr/bin/env python

import argparse
import sys


tax_brackets = {
    '2017': {
        (0, 9325): lambda x: x * 0.1,
        (9325, 37950): lambda x: 932.50 + x * 0.15,
        (37950, 91900): lambda x: 5226.25 + x * 0.25,
        (91900, 191650): lambda x: 18713.75 + x * 0.28,
        (191650, 416700): lambda x: 46643.75 + x * 0.33,
        (416700, 418400): lambda x: 120910.25 + x * 0.396,
        (418400, 999999999999): lambda x: 121505.25 + x * 0.396,
    },
    'Trump': {
        (0, 37950): lambda x: x * 0.12,
        (37950, 416700): lambda x: 4554 + x * 0.25,
        (416700, 999999999999): lambda x: 99241.50 + x * 0.35,
    },
    'Trump_2017_11_02': {
        (0, 12000): lambda x: 0,
        (12000, 45000): lambda x: x * 0.12,
        (45000, 200000): lambda x: 3960 + x * 0.25,
        (200000, 500000): lambda x: 42710 + x * 0.35,
        (500000, 999999999999): lambda x: 147710 + x * 0.396,
    },
}

standard_deductions = {
    '2017': 6350,
    'Trump': 12000,
    'Trump_2017_11_02': 12000,
}

exemptions = {
    '2017': 4050,
    'Trump': 0,
    'Trump_2017_11_02': 0,
}


def get_taxes(income, num_exemptions, tax_plan_name):
    brackets = tax_brackets.get(tax_plan_name)
    standard_deduction = standard_deductions.get(tax_plan_name)
    exemption = exemptions.get(tax_plan_name)

    income -= standard_deduction
    income -= (exemption * num_exemptions)

    for (min, max), fn in brackets.iteritems():
        if income >= min and income < max:
            return fn(income - min)


def main(args):
    parser = argparse.ArgumentParser(description='Simple tax calculator')
    parser.add_argument('income')
    parser.add_argument('num_exemptions')
    args = parser.parse_args()

    try:
        income = float(args.income)
        num_exemptions = float(args.num_exemptions)
    except:
        print 'You have to supply a valid number for income and exemptions!'
        return False

    for tax_plan in tax_brackets:
        print '{}: {}'.format(tax_plan, get_taxes(income,
                                                  num_exemptions,
                                                  tax_plan))


if __name__ == '__main__':
    sys.exit(main(sys.argv))
