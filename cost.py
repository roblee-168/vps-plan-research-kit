# ::ILANG [TYPE:utility][BOUNDARY:offline arithmetic only; no provider prices]
import argparse
from decimal import Decimal

def calculate(initial_total, initial_months, renewal_monthly, months):
    initial_total, renewal_monthly = Decimal(str(initial_total)), Decimal(str(renewal_monthly))
    if not initial_total.is_finite() or not renewal_monthly.is_finite() or initial_total < 0 or renewal_monthly < 0 or initial_months <= 0 or months <= 0:
        raise ValueError("Use finite nonnegative prices and positive month counts")
    total = initial_total + max(0, months - initial_months) * renewal_monthly
    return total, total / months

if __name__ == '__main__':
    p = argparse.ArgumentParser(description='Offline fixed-term VPS cost calculator; all monetary inputs must use the same currency.')
    p.add_argument('--initial-total', required=True)
    p.add_argument('--initial-months', type=int, required=True)
    p.add_argument('--renewal-monthly', required=True)
    p.add_argument('--months', type=int, required=True)
    a = p.parse_args()
    try:
        total, monthly = calculate(a.initial_total, a.initial_months, a.renewal_monthly, a.months)
    except (ValueError, ArithmeticError) as e:
        p.error(str(e))
    print(f'Total: {total:.2f}; effective monthly: {monthly:.2f} (input currency; excludes taxes and fees)')
