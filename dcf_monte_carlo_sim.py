import numpy as np
import matplotlib.pyplot as plt

# Parameters
iterations = 10000
years = 5

# Actual data and assumptions
branches_2025 = 1449
onsites_2025 = 2131
rev_per_branch_2025 = 2.82 
rev_per_onsite_2025 = 1.58 
other_rev_2025 = 688.9    
ebit_margin = 0.205
tax_rate = 0.246
cogs_margin = 0.547
da_margin = 0.022
capex_margin = 0.026
dso = 55.4
dio = 141.5
dpo = 25.6
shares_out = 1150.3
net_debt = 120.0 - 204.7
exit_multiple = 18.0

# 2025 NWC baseline
cogs_2025 = (branches_2025 * rev_per_branch_2025 + onsites_2025 * rev_per_onsite_2025 + other_rev_2025) * cogs_margin
nwc_2025 = ((8200.5 / 365) * dso) + ((cogs_2025 / 365) * dio) - ((cogs_2025 / 365) * dpo)

# Random variables for simulation 
np.random.seed(11) #birth date 
# Target is 400, model as N(300,50)
sim_onsite_adds = np.random.normal(loc=300, scale=50, size=(iterations, years))
# inflation ~ N(3%, 1%)
sim_pricing_power = np.random.normal(loc=0.03, scale=0.01, size=(iterations, years))
# WACC ~ N(9%, 0.5%)
sim_wacc = np.random.normal(loc=0.09, scale=0.005, size=iterations)

implied_share_prices = np.zeros(iterations)

# Run loop
for i in range(iterations):
    ufcf = np.zeros(years)
    prev_nwc = nwc_2025
    
    curr_branches = branches_2025
    curr_onsites = onsites_2025
    curr_rev_branch = rev_per_branch_2025
    curr_rev_onsite = rev_per_onsite_2025
    curr_other_rev = other_rev_2025
    
    for t in range(years):
        curr_branches -= 50  # Closing 50 branches a year
        curr_onsites += sim_onsite_adds[i, t] # Randomly adding onsites
        
        curr_rev_branch *= (1 + sim_pricing_power[i, t])
        curr_rev_onsite *= (1 + sim_pricing_power[i, t])
        curr_other_rev *= 1.10 # Flat 10% growth for Specialty/International
        
        # Calculate Sales
        sales = (curr_branches * curr_rev_branch) + (curr_onsites * curr_rev_onsite) + curr_other_rev
        cogs = sales * cogs_margin
        
        # Income Statement
        ebit = sales * ebit_margin
        taxes = ebit * tax_rate
        ebiat = ebit - taxes
        da = sales * da_margin
        capex = sales * capex_margin if t > 0 else 320.0
        
        # NWC
        ar = (sales / 365) * dso
        inv = (cogs / 365) * dio
        ap = (cogs / 365) * dpo
        curr_nwc = ar + inv - ap
        
        dnwc = curr_nwc - prev_nwc
        prev_nwc = curr_nwc
        
        # UFCF
        ufcf[t] = ebiat + da - capex - dnwc

    # TV and DCF
    terminal_ebitda = ebit + da
    terminal_value = terminal_ebitda * exit_multiple
    
    pv_fcfs = sum([ufcf[t] / ((1 + sim_wacc[i])**(t + 0.5)) for t in range(years)])
    pv_tv = terminal_value / ((1 + sim_wacc[i])**years)
    
    enterprise_value = pv_fcfs + pv_tv
    equity_value = enterprise_value - net_debt
    implied_share_prices[i] = equity_value / shares_out

# Visuals 
median_price = np.percentile(implied_share_prices, 50)
p10 = np.percentile(implied_share_prices, 10)
p90 = np.percentile(implied_share_prices, 90)

print(f"--- Advanced FP&A Monte Carlo Results ---")
print(f"10th Percentile (Downside): ${p10:.2f}")
print(f"50th Percentile (Base Case): ${median_price:.2f}")
print(f"90th Percentile (Upside): ${p90:.2f}")

plt.figure(figsize=(10, 6))
plt.hist(implied_share_prices, bins=50, color='mediumseagreen', edgecolor='black', alpha=0.7)
plt.axvline(median_price, color='black', linestyle='dashed', linewidth=2, label=f'Median: ${median_price:.2f}')
plt.axvline(p10, color='red', linestyle='dashed', linewidth=2, label=f'10th %ile: ${p10:.2f}')
plt.axvline(p90, color='blue', linestyle='dashed', linewidth=2, label=f'90th %ile: ${p90:.2f}')
plt.title('Fastenal: Stochastic FP&A Unit Economics Valuation')
plt.xlabel('Implied Share Price ($)')
plt.ylabel('Frequency')
plt.legend()
plt.grid(axis='y', alpha=0.5)
plt.show()