# caer-financial-calculators
Rule of 72 Calculator, Compound Interest Calculator, Break-Even Calculator, Retirement Income Estimator
# CAER Financial Calculators

**By CAER Financial Group | caergroup.com | Jessica@caergroup.com**

> Faith · Family · Financial Responsibility

## Overview
Open-source financial calculators designed for educational use, created to support the CFG Young Investors financial literacy curriculum.

## Calculators Included

### 1. Rule of 72 Calculator
```python
def rule_of_72(rate: float) -> float:
    """
    Calculate years to double using Rule of 72.
    Args: rate — annual interest rate as percentage (e.g., 5.0 for 5%)
    Returns: approximate years to double
    """
    if rate <= 0:
        raise ValueError("Rate must be positive")
    return 72 / rate

# Examples
print(rule_of_72(0.5))   # 144.0 years (bank savings)
print(rule_of_72(5.0))   # 14.4 years (MYGA)
print(rule_of_72(7.0))   # 10.3 years (IUL average)
print(rule_of_72(20.0))  # 3.6 years (credit card debt)
```

### 2. Compound Interest Calculator
```python
def compound_interest(principal, rate, n, t):
    """
    A = P(1 + r/n)^(nt)
    principal: initial amount
    rate: annual rate as decimal (0.05 for 5%)
    n: compounding periods per year
    t: time in years
    """
    return principal * (1 + rate/n) ** (n * t)

# Compare bank vs MYGA over 5 years
bank = compound_interest(100000, 0.005, 12, 5)
myga = compound_interest(100000, 0.05, 1, 5)
print(f"Bank: ${bank:,.2f}")    # $102,527.98
print(f"MYGA: ${myga:,.2f}")    # $127,628.16
print(f"Difference: ${myga-bank:,.2f}")  # $25,100.18
```

### 3. Break-Even Calculator
```python
def break_even_units(fixed_costs, selling_price, variable_cost):
    contribution_margin = selling_price - variable_cost
    return fixed_costs / contribution_margin

def break_even_dollars(fixed_costs, selling_price, variable_cost):
    cm_ratio = (selling_price - variable_cost) / selling_price
    return fixed_costs / cm_ratio
```

### 4. Retirement Income Estimator
```python
def retirement_income_estimate(
    current_age, retirement_age, monthly_savings,
    annual_rate, ss_monthly_benefit
):
    years = retirement_age - current_age
    rate_monthly = annual_rate / 12
    months = years * 12
    fv = monthly_savings * ((1 + rate_monthly)**months - 1) / rate_monthly
    monthly_income = fv * 0.04 / 12  # 4% rule
    total = monthly_income + ss_monthly_benefit
    return {"portfolio_value": fv, "monthly_income": monthly_income,
            "ss_benefit": ss_monthly_benefit, "total_monthly": total}
```

## About CFG Young Investors
This code supports our free financial literacy curriculum. If you're an educator, youth organization, or developer who wants to build on these tools — fork this repo.

**Contact:** Amberly@caergroup.com | caergroup.com | 502-677-0176

## License
MIT — Free for educational use. Attribution appreciated.
