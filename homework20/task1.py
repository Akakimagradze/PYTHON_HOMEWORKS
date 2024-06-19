import json

def main(file, department_number, employees_key, salary_key):
    try:
        with open(file) as f:
            data = json.load(f)
            
            departments = data[department_number][employees_key]
            department_salary = 0
            salary_count = 0
            
            for department in departments:
                try:
                    department_salary += int(department[salary_key])
                    salary_count += 1
                except ValueError:
                    continue
                
            try:
                department_average = department_salary / salary_count
            except ZeroDivisionError:
                return 0
            
            print(f"{department_number} Average Salary: {round(department_average, 2)}")
                
            return department_average 
              
    except FileNotFoundError as err:
        print(err)

    
if __name__ == "__main__":
    department1_average = main("data.json", "department_1", "employees", "salary")
    department2_average = main("data.json", "department_2", "employees", "salary")
    department3_average = main("data.json", "department_3", "employees", "salary")
    
    departments = ["department_1", "department_2", "department_3"]
    departments_averages = [department1_average, department2_average, department3_average]
    departments_dict = {}
    
    j = 0
    for i in departments:
        departments_dict[i] = str(departments_averages[j])
        j += 1
    
    with open("avg_salary.json", "w") as f:
        json.dump(departments_dict, f, indent=4) 
    
