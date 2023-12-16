# 996能否减少不平等？
# 996指的是每天早上九点上班晚上九点下班每周工作六天。
# 全球总财富为$454.8 trillion，人口为540 million，富人占比13.1%，控制全球财富的85.2%，穷人占比86.9%，控制全球财富的14.8%（Global Wealth Report, 2023）。
# 劳动收入计算规则如下，在八小时工作时间内，收入=Q(t)*p，Q(t)是生产函数，根据边际递减规律，它是递减的。p是每单位劳动所获得的价格，全球平均工资为$9,733 per year(Jack Flynn, 2023)，在八小时工作时间外，也就是工作日加班4小时，周末加班12小时，不考虑中途吃饭去卫生间等时间消耗，加班过程中，每单位劳动所获得的价格变为原来的1.5倍。
# 资本收入计算规则如下，如果存入银行，每年利率为1%。如果用于投资，10%的概率资本翻倍，50%的概率资本不变，40%的概率资本减少20%.富人中有60%的人愿意投资而40%愿意储蓄，且富人中有0.01%的人愿意996，其余人是八小时工作制。穷人全部996，挣的钱全部用于储蓄。


# Can 996 reduce income inequality? 

# 996 refers to working from 9am to 9pm, six days a week. The global total wealth is $454.8 trillion with a population of 540 million. The rich make up 13.1% of the population and control 85.2% of the global wealth, while the poor make up 86.9% of the population and control 14.8% of the global wealth (Global Wealth Report, 2023).

#  labor income calculation rule is as follows: within an eight-hour workday, income = Q(t) * p, where Q(t) is the production function and decreases according to the law of diminishing marginal returns. p is the price per unit of labor, and the global average wage is $9,733 per year (Jack Flynn, 2023). During overtime, which is four hours on workdays and 12 hours on weekends, the price per unit of labor increases by 1.5 times.

# The capital income calculation rule is as follows: If deposited in a bank, the annual interest rate is 1%. If invested, there is a 10% chance of doubling the capital, a 50% chance of not changing, and a 40% chance of decreasing the capital by 20%. 60% of the rich are willing to invest while 40% prefer to save, and only 0.01% of the rich are willing to work under the 996 system, while the rest work eight hours a day. All poor people work under the 996 system and save all their earnings.


import matplotlib.pyplot as plt
import numpy as np

# Parameters
total_wealth = 454.8e12  # Total global wealth in dollars
population = 540e6       # Global population
avg_annual_wage = 9733   # Average global wage per year in dollars

# Wealth distribution
rich_population_ratio = 0.131
poor_population_ratio = 0.869
rich_wealth_ratio = 0.852
poor_wealth_ratio = 0.148

# Initial wealth distribution
initial_rich_wealth = total_wealth * rich_wealth_ratio
initial_poor_wealth = total_wealth * poor_wealth_ratio

# Labor income calculation
work_hours_per_week_normal = 8 * 5  # 8 hours per day, 5 days a week
work_hours_per_week_996 = 9 * 6     # 9 hours per day, 6 days a week
overtime_multiplier = 1.5

# Assume Q(t) is constant for simplicity
Q_t = 1

# Calculate hourly wage
hourly_wage = avg_annual_wage / (work_hours_per_week_normal * 52)

# Wealth growth over time
years = 200
rich_wealth = np.zeros(years)
poor_wealth = np.zeros(years)
rich_wealth[0] = initial_rich_wealth
poor_wealth[0] = initial_poor_wealth

# Wealth growth parameters for rich
rich_investment_rate = 0.6
rich_savings_rate = 0.4
investment_return = [2, 1, 0.8]  # Possible investment returns
investment_prob = [0.1, 0.5, 0.4]

for year in range(1, years):
    # Update rich wealth
    invested_wealth = rich_wealth[year - 1] * rich_investment_rate
    saved_wealth = rich_wealth[year - 1] * rich_savings_rate
    investment_growth = np.dot(investment_return, investment_prob) * invested_wealth
    savings_growth = saved_wealth * 1.01  # 1% interest on savings
    rich_wealth[year] = investment_growth + savings_growth

    # Update poor wealth
    normal_income = hourly_wage * work_hours_per_week_normal * 52
    overtime_income = hourly_wage * overtime_multiplier * (work_hours_per_week_996 - work_hours_per_week_normal) * 52
    total_annual_income = normal_income + overtime_income
    poor_wealth[year] = poor_wealth[year - 1] + total_annual_income

# Plotting the graph
plt.figure(figsize=(12, 6), dpi=1200)
plt.plot(rich_wealth, label='Wealth of Rich')
plt.plot(poor_wealth, label='Wealth of Poor')
plt.xlabel('Years')
plt.ylabel('Total Wealth ($)')
plt.title('Total Wealth of Rich and Poor Over Time')
plt.legend()
plt.grid(True)
plt.savefig('C:/Users/Jiacheng Zheng/Desktop/my_plot3.png')
# plt.show()
