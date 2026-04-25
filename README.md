# CAER Financial Calculators

**By CAER Financial Group | caergroup.com | Jessica@caergroup.com**

> Faith · Family · Financial Responsibility

## Table of Contents

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Calculators Included](#calculators-included)
- [Installation & Usage](#installation--usage)
- [About CFG Young Investors](#about-cfg-young-investors)
- [Contributing](#contributing)
- [License](#license)

## Overview

Open-source financial calculators designed for educational use, created to support the CFG Young Investors financial literacy curriculum. These tools help students and educators understand key financial concepts through interactive calculators.

**Features:**
- Rule of 72 Calculator — estimate investment doubling time
- Compound Interest Calculator — compare savings vehicles
- Break-Even Calculator — analyze business profitability
- Retirement Income Estimator — plan for retirement using the 4% rule

## Quick Start

```python
from calculators import rule_of_72, compound_interest

# How long to double your money at 5% annual return?
years = rule_of_72(5.0)
print(f"Your money doubles in {years:.1f} years")  # Output: 14.4 years

# Compare bank savings vs. MYGA over 5 years
bank = compound_interest(100000, 0.005, 12, 5)
myga = compound_interest(100000, 0.05, 1, 5)
print(f"Bank: ${bank:,.2f}")    # $102,527.98
print(f"MYGA: ${myga:,.2f}")    # $127,628.16
```

## Calculators Included

### 1. Rule of 72 Calculator

Quickly estimate how many years it takes for an investment to double based on annual return rate.

**Use case:** Understanding the power of compound interest and comparing investment opportunities

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

Calculate how investments grow over time with different compounding frequencies.

**Use case:** Comparing savings accounts, MYGAs, and investment returns

```python
def compound_interest(principal, rate, n, t):
    """
    Calculate compound interest using A = P(1 + r/n)^(nt)
    
    Args:
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

Determine the sales volume or revenue needed to cover all costs and start making profit.

**Use case:** Business planning and understanding profitability thresholds

```python
def break_even_units(fixed_costs, selling_price, variable_cost):
    """Calculate break-even point in units"""
    contribution_margin = selling_price - variable_cost
    return fixed_costs / contribution_margin

def break_even_dollars(fixed_costs, selling_price, variable_cost):
    """Calculate break-even point in revenue dollars"""
    cm_ratio = (selling_price - variable_cost) / selling_price
    return fixed_costs / cm_ratio
```

### 4. Retirement Income Estimator

Project monthly retirement income based on savings rate, investment returns, and Social Security benefits.

**Use case:** Planning for retirement and understanding the 4% withdrawal rule

```python
def retirement_income_estimate(
    current_age, retirement_age, monthly_savings,
    annual_rate, ss_monthly_benefit
):
    """
    Estimate monthly retirement income using the 4% rule.
    
    Args:
        current_age: age now
        retirement_age: target retirement age
        monthly_savings: monthly contribution amount
        annual_rate: expected annual return rate (as decimal, e.g., 0.07 for 7%)
        ss_monthly_benefit: expected Social Security benefit
    
    Returns:
        Dictionary with portfolio value, monthly income, and total monthly income
    """
    years = retirement_age - current_age
    rate_monthly = annual_rate / 12
    months = years * 12
    fv = monthly_savings * ((1 + rate_monthly)**months - 1) / rate_monthly
    monthly_income = fv * 0.04 / 12  # 4% rule
    total = monthly_income + ss_monthly_benefit
    return {
        "portfolio_value": fv, 
        "monthly_income": monthly_income,
        "ss_benefit": ss_monthly_benefit, 
        "total_monthly": total
    }
```

## Installation & Usage

### Prerequisites
- Python 3.7 or higher

### Setup

```bash
# Clone the repository
git clone https://github.com/JessicaCFG/caer-financial-calculators.git
cd caer-financial-calculators

# Install dependencies (if any)
pip install -r requirements.txt

# Run a calculator
python calculators.py
```

### Using in Your Project

```python
from calculators import rule_of_72, compound_interest, break_even_units, retirement_income_estimate

# Use any calculator function
result = rule_of_72(7.0)
```

## About CFG Young Investors

This code supports our free financial literacy curriculum. If you're an educator, youth organization, or developer who wants to build on these tools — **fork this repo and contribute!**

We believe in making financial education accessible and open-source.

**Contact:** Jessica@caergroup.com | caergroup.com | 502-677-0176

## Contributing

We welcome contributions! Here's how to help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/add-calculator`)
3. Make your changes with clear commit messages
4. Submit a pull request with a description of your improvements

**Contribution ideas:**
- Add new financial calculators
- Improve existing calculations
- Add unit tests
- Enhance documentation
- Create interactive web interfaces

## License

MIT — Free for educational use. Attribution appreciated.

See `LICENSE` file for full details.
