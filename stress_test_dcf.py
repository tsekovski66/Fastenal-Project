import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Baseline 2025 financials
sales_2025 = 8200.5
interest_expense = 6.0  # estimated annual interest on $120M debt

# Stress vectors
# Array of 10 revenue scenarios
revenue_shocks = np.linspace(0.0, -0.30, 10) 

# Array of 10 EBIT margin scenarios
margin_shocks = np.linspace(0.205, 0.105, 10) 

# Empty grid (10x10 matrix) to hold results
coverage_matrix = np.zeros((len(margin_shocks), len(revenue_shocks)))

# 4. Nested loops to calculate ratio for each scenario combination
for i, margin in enumerate(margin_shocks):
    for j, rev_shock in enumerate(revenue_shocks):
        
        # Calculate stressed sales based on revenue shock
        stressed_sales = sales_2025 * (1 + rev_shock)
        
        # Calculate stressed EBITDA (DA margin flat at 2.2% of sales)
        stressed_ebit = stressed_sales * margin
        stressed_da = stressed_sales * 0.022
        stressed_ebitda = stressed_ebit + stressed_da
        
        # Calculate Interest Coverage Ratio
        coverage_ratio = stressed_ebitda / interest_expense
        
        # Store result
        coverage_matrix[i, j] = coverage_ratio

# Format labels
rev_labels = [f"{x*100:.0f}%" for x in revenue_shocks]
margin_labels = [f"{x*100:.1f}%" for x in margin_shocks]

# Risk matrix visuals
plt.figure(figsize=(12, 7))
sns.heatmap(coverage_matrix, 
            annot=True,          # Show the numbers
            fmt=".0f",           # Whole numbers
            cmap="RdYlGn",       # Color scale, red(bad) to green(good)
            xticklabels=rev_labels, 
            yticklabels=margin_labels,
            vmin=10, vmax=250)   # Color threshold limits

plt.title('Credit Risk Matrix: Fastenal Interest Coverage Ratio', fontsize=14)
plt.xlabel('Revenue Shock (Volume Contraction)', fontsize=12)
plt.ylabel('Stressed EBIT Margin', fontsize=12)
plt.yticks(rotation=0)
plt.show()