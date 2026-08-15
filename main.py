# برنامج حساب الأرباح البسيط - أول مشروع لزهراء
def calculate_profit(revenue, expenses):
    profit = revenue - expenses
    return profit

# تجربة البرنامج
my_revenue = 5000
my_expenses = 2000

final_profit = calculate_profit(my_revenue, my_expenses)
print(f"تم حساب الأرباح بنجاح: {final_profit} دولار")