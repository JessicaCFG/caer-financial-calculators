"""
Compound Interest Visualizer

Displays ASCII charts of investment growth curves over time,
comparing different interest rates and investment vehicles.
"""

def compound_interest(principal, rate, n, t):
    """
    Calculate compound interest using A = P(1 + r/n)^(nt)
    
    Args:
        principal: initial amount
        rate: annual rate as decimal (0.05 for 5%)
        n: compounding periods per year
        t: time in years
    
    Returns:
        Final amount after compound interest
    """
    return principal * (1 + rate/n) ** (n * t)


def calculate_growth_curve(principal, rate, n, years):
    """
    Calculate investment growth for each year.
    
    Args:
        principal: initial amount
        rate: annual rate as decimal
        n: compounding periods per year
        years: number of years to project
    
    Returns:
        List of (year, amount) tuples
    """
    curve = []
    for year in range(years + 1):
        amount = compound_interest(principal, rate, n, year)
        curve.append((year, amount))
    return curve


def normalize_for_chart(values, chart_height=15):
    """
    Normalize values to fit in chart height.
    
    Args:
        values: list of numeric values
        chart_height: desired height of chart in lines
    
    Returns:
        List of normalized values (0 to chart_height)
    """
    if not values:
        return []
    
    min_val = min(values)
    max_val = max(values)
    
    if min_val == max_val:
        return [chart_height // 2] * len(values)
    
    range_val = max_val - min_val
    normalized = []
    for val in values:
        normalized_val = int(((val - min_val) / range_val) * chart_height)
        normalized.append(normalized_val)
    
    return normalized


def create_ascii_chart(curves_data, title="Investment Growth Comparison", years=30, width=80):
    """
    Create an ASCII chart comparing multiple investment curves.
    
    Args:
        curves_data: list of dicts with keys 'label', 'principal', 'rate', 'n'
        title: chart title
        years: number of years to project
        width: chart width in characters
    
    Returns:
        String containing the ASCII chart
    """
    chart_height = 15
    chart_width = min(width - 15, years + 1)
    
    # Calculate all curves
    all_curves = []
    all_final_values = []
    
    for curve_info in curves_data:
        curve = calculate_growth_curve(
            curve_info['principal'],
            curve_info['rate'],
            curve_info['n'],
            years
        )
        all_curves.append((curve_info['label'], curve))
        all_final_values.extend([amount for _, amount in curve])
    
    # Normalize all values together for consistent scaling
    min_val = min(all_final_values)
    max_val = max(all_final_values)
    range_val = max_val - min_val if max_val != min_val else 1
    
    # Create chart grid
    output = []
    output.append(f"\n{title}")
    output.append("=" * min(len(title), width))
    output.append("")
    
    # Calculate step size for x-axis
    step = max(1, years // chart_width)
    
    # Create legend
    legend = []
    for label, _ in all_curves:
        legend.append(f"  {label}")
    output.append("Legend:\n" + "\n".join(legend))
    output.append("")
    
    # Create ASCII chart rows (top to bottom)
    for row in range(chart_height, -1, -1):
        line = f"${(min_val + (row / chart_height) * range_val):>10,.0f} |"
        
        # Plot each column
        for col in range(0, years + 1, step):
            if col < len(all_curves[0][1]):  # Make sure we have data for this year
                # Check if any curve has a point at this height for this year
                point = ""
                for curve_idx, (label, curve) in enumerate(all_curves):
                    if col < len(curve):
                        _, amount = curve[col]
                        normalized = int(((amount - min_val) / range_val) * chart_height)
                        if normalized == row:
                            # Use different characters for different curves
                            point = chr(65 + curve_idx)  # A, B, C, etc.
                            break
                
                line += f" {point} " if point else "   "
        
        output.append(line)
    
    # X-axis
    x_axis = "          +"
    for col in range(0, years + 1, step):
        x_axis += "---"
    output.append(x_axis)
    
    # X-axis labels
    x_labels = "   Years  |"
    for col in range(0, years + 1, step):
        x_labels += f"{col:>3}"
    output.append(x_labels)
    
    # Add summary table
    output.append("\n" + "=" * min(60, width))
    output.append(f"{'Investment':<20} {'Final Value':>15} {'Total Growth':>15}")
    output.append("-" * min(60, width))
    
    for label, curve in all_curves:
        initial = curve[0][1]
        final = curve[-1][1]
        growth = final - initial
        output.append(f"{label:<20} ${final:>14,.2f} ${growth:>14,.2f}")
    
    output.append("=" * min(60, width))
    
    return "\n".join(output)


def compare_investments(principal=100000, years=30):
    """
    Compare common investment scenarios.
    
    Args:
        principal: initial investment amount
        years: projection period
    
    Returns:
        ASCII chart comparing different investment types
    """
    curves = [
        {
            'label': 'A = Bank (0.5%)',
            'principal': principal,
            'rate': 0.005,
            'n': 12  # Monthly compounding
        },
        {
            'label': 'B = MYGA (5.0%)',
            'principal': principal,
            'rate': 0.05,
            'n': 1  # Annual compounding
        },
        {
            'label': 'C = Stock Average (10%)',
            'principal': principal,
            'rate': 0.10,
            'n': 1  # Annual compounding
        },
    ]
    
    return create_ascii_chart(curves, f"Investment Growth: ${principal:,} over {years} years", years)


def compare_rates(principal=100000, years=30):
    """
    Compare the same investment at different rates.
    
    Args:
        principal: initial investment amount
        years: projection period
    
    Returns:
        ASCII chart comparing different interest rates
    """
    curves = [
        {
            'label': 'A = 2% Annual',
            'principal': principal,
            'rate': 0.02,
            'n': 1
        },
        {
            'label': 'B = 5% Annual',
            'principal': principal,
            'rate': 0.05,
            'n': 1
        },
        {
            'label': 'C = 8% Annual',
            'principal': principal,
            'rate': 0.08,
            'n': 1
        },
        {
            'label': 'D = 12% Annual',
            'principal': principal,
            'rate': 0.12,
            'n': 1
        },
    ]
    
    return create_ascii_chart(curves, f"Impact of Interest Rate: ${principal:,} over {years} years", years)


if __name__ == "__main__":
    # Display investment comparison
    print(compare_investments(100000, 30))
    
    # Display rate comparison
    print("\n\n")
    print(compare_rates(100000, 30))
    
    # Example: Custom comparison
    print("\n\n")
    custom_curves = [
        {
            'label': 'Conservative ($50k @ 3%)',
            'principal': 50000,
            'rate': 0.03,
            'n': 1
        },
        {
            'label': 'Moderate ($50k @ 7%)',
            'principal': 50000,
            'rate': 0.07,
            'n': 1
        },
        {
            'label': 'Aggressive ($50k @ 10%)',
            'principal': 50000,
            'rate': 0.10,
            'n': 1
        },
    ]
    print(create_ascii_chart(custom_curves, "Portfolio Strategy Comparison: 20 Years", 20))
