import sys
def get_weekly_sales(week_number):
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    daily_sales = {}
    print(f"\n--- Enter Sales Data for WEEK {week_number} (in ₹) ---")
    for day in days_of_week:
        while True:
            sales = int(input(f"Enter sales for {day} (₹): "))
            if sales < 0:
                print("Sales cannot be negative. Please enter a positive value.")
                continue
            daily_sales[day] = sales
            break
    return daily_sales
def summarize_all_weeks(all_weeks_data):
    if not all_weeks_data:
        print("\nNo sales data entered to summarize.")
        return
    grand_total = 0
    best_week = {'week': 0, 'total': -1}
    worst_week = {'week': 0, 'total': sys.maxsize}
    
    highest_single_sale = {'week': 0, 'day': '', 'value': -1}
    lowest_single_sale = {'week': 0, 'day': '', 'value': sys.maxsize}
    for week_num, total_sales, daily_sales_dict in all_weeks_data:
        grand_total += total_sales
        if total_sales > best_week['total']:
            best_week.update({'week': week_num, 'total': total_sales})
        if total_sales < worst_week['total']:
            worst_week.update({'week': week_num, 'total': total_sales})
        for day, sale_value in daily_sales_dict.items():
            if sale_value > highest_single_sale['value']:
                highest_single_sale.update({'week': week_num, 'day': day, 'value': sale_value})
            if sale_value < lowest_single_sale['value']:
                lowest_single_sale.update({'week': week_num, 'day': day, 'value': sale_value})
    num_weeks = len(all_weeks_data)
    average_weekly_sales = grand_total / num_weeks
    print("\n" + "="*50)
    print("        COMPREHENSIVE MULTI-WEEK SALES ANALYSIS")
    print("="*50)
    print(f"Total Weeks Analyzed: {num_weeks}")
    print(f"Grand Total Sales: ₹{grand_total:,.2f}")
    print(f"Average Weekly Sales: ₹{average_weekly_sales:,.2f}")
    print("-" * 50)
    
    print(f"Best Performing Week: Week {best_week['week']} (Total: ₹{best_week['total']:,.2f})")
    print(f"Worst Performing Week: Week {worst_week['week']} (Total: ₹{worst_week['total']:,.2f})")
    print("-" * 50)
    
    print(f"Highest Single Day Sale:")
    print(f"₹{highest_single_sale['value']:,.2f} on {highest_single_sale['day']} (Week {highest_single_sale['week']})")
    
    print(f"Lowest Single Day Sale:")
    print(f"₹{lowest_single_sale['value']:,.2f} on {lowest_single_sale['day']} (Week {lowest_single_sale['week']})")
    print("="*50)
def main():
    all_weeks_data =[]
    week_counter=1
    print("Welcome to the Multi-Week Sales Analyzer!")
    while True:
        daily_sales_dict = get_weekly_sales(week_counter)
        week_total = sum(daily_sales_dict.values())
        all_weeks_data.append((week_counter, week_total, daily_sales_dict))
        print(f"\n>>> Week {week_counter} Total Sales: ₹{week_total:,.2f} recorded.")
        week_counter += 1
        user_input = input("\nDo you want to enter data for another week? (yes/no): ").strip().lower()
        if user_input not in ['yes', 'y']:
            break
    summarize_all_weeks(all_weeks_data)
    print("\nAnalysis Complete. Thank you!")

if __name__ == "__main__":
    main()