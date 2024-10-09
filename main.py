from datetime import date
from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == "__main__":
    current_date = date.today()
    print(f'Сегодня: {current_date}') 
    print("----------")
    calculate_salary()
    get_employees()
    print("----------")

    