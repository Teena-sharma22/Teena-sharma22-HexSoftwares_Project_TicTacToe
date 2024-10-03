from ex import Expense
import calendar
import datetime



def main():
    print("it's working")
    expense_file_path = "expense.csv"
    budget = 30000

    expense = expense_kitna()


    file_mai_save(expense,expense_file_path)    

    summarize_expenses(expense_file_path,budget)
        

def expense_kitna():
    expense_name = input("enter name of item : ")
    expense_price = eval(input("enter price of item : "))  
    category_list =  [ 'Food ','Clothes','Home','Fun','Extra']

    while True:
        print("In which category you want to add this item : ")
        for i ,expense_category in enumerate(category_list):
            print(f"{i+1}.{expense_category}")

        value_range = f"[1-{len(category_list)}]"
        selected_category = int(input(f"enter category {value_range} : "))-1
        
        if selected_category in range(len(category_list)):
            category = category_list[selected_category]
            print(category)

            new_expense = Expense(name=expense_name,categoryy=category,amount=expense_price)
            return (new_expense)
            # print(f" you took {expense_name} of {expense_price} in {category} category")

        else:
            print("invalid category")

        break


def file_mai_save(expense:Expense , expense_file_path):
    print(f"save all the kharcha : {expense} to {expense_file_path}")  

    with open(expense_file_path,"a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.categoryy}\n")  


def summarize_expenses(expense_file_path,budget):
    print("summarize of  user expenses : ")
    expenses = []
    with open(expense_file_path,'r') as f:
        lines = f.readlines()
        for line in lines:
            # print(line)

            expense_name ,expense_amount,expense_category = line.strip().split(",") 
            print(f"{expense_name} {expense_amount} {expense_category}")
            line_expense = Expense(name=expense_name,amount=float(expense_amount),categoryy=expense_category)
            # print(line_expense)  
            expenses.append(line_expense)
            print(expenses)
    amount_by_category = {}
    for expense in expenses:
        key = expense.categoryy

        if key in amount_by_category:
            amount_by_category[key] +=expense.amount
        else:
            amount_by_category[key] = expense.amount
    # print (amount_by_category) 
    print("aapka kharcha")
    for key ,amount in amount_by_category.items():
        print(f"{key} : {amount}")

    total_spent = sum([x.amount for x in expenses])
    print(f"total money spent : {total_spent:.2f}")


    remaining_budget = budget - (total_spent)
    print(f"remaining budget : {remaining_budget:.2f}")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year,now.month)[1]
    remaining_days = days_in_month - now.day
    print(f"remaining days in this month : {remaining_days}")

    daily_budget = remaining_budget/remaining_days
    print("daily budget :",daily_budget)

  

if __name__ =="__main__":
    main()    