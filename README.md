# Multi-Week-Data-Analyzer
Term-End project on python essentials through vityarthi platform on Multi-week Data Analyzer and finance management.


How the Program Works (The Three Main Jobs)
# 1. Getting the Weekly Data (get_weekly_sales) ????
What it does: This function is a data entry assistant. For a given week, it guides you from Monday to Sunday to input the sales amount in Indian Rupees (₹) for that day.
Safety Check: It is programmed to be careful! In case you mistakenly input a number as negative, it alerts immediately since the amount of sales cannot be negative, and keeps on asking until you provide a non-negative amount.
Memory: It will organize all seven daily sales figures in a dictionary, labeled by the day of the week, and it returns that to the main program.

# 2. Summarizing Everything (summarize_all_weeks) ????
What it does: This function performs the in-depth analysis once you are done entering data. It takes all the information about weekly sales you provided and uses it to develop the key insights.
The Big Numbers: It calculates your Grand Total Sales across the whole period and figures out your Average Weekly Sales.
Extremes: This is where it highlights your best and worst performances.
It identifies the Best Performing Week, meaning the highest total sales.
It identifies the worst performing week (lowest total sales).
It finds the single day, across all weeks, with the Highest Single Day Sale.
It finds the single day, across all weeks, with the Lowest Single Day Sale.
The Report: Lastly, it prints a clean, organized, and readable report showing all these totals and extreme values.

# 3. Running the Show (main) ????
What it does: This is the conductor of the orchestra. It controls the entire process from start to finish.
The Loop: It starts by asking for Week 1's data, then calculates that week's total, and stores all the information. Crucially, it then asks you: "Do you want to enter data for another week?"
Stopping Point: If you say 'yes' or 'y', it goes through the process again for Week 2, Week 3, etc. If you say 'no' or 'n', it stops collecting data.
Grand Finale: Following the completion of data entry, it calls the function summarize_all_weeks with all the information that has been collected for final analysis.

# Key Strengths Flexible:
It can be used to track the sales of anything for two, five, or fifty weeks! Error-Proof: The program ensures that you enter only valid (that is, non-negative) sales figures. Insightful: Besides the mere total, it tells you when you were at your best and worst, providing you with actionable insights into your business performance.
