def temp_teller():
    week_temps = ((33, 34, 28), (24, 31, 27), (24, 23, 27), (28, 32, 34), (33, 21, 28), (20, 25, 31), (21, 31, 28))

    day_counter = 0 
    week = 0 
    
    for day in week_temps:
        total_temperature = 0
        counter = 0
        max_temp = 0
        
        for temp in day:
            total_temperature += temp
            counter += 1
            if temp > max_temp: 
                max_temp = temp
        
        min_temp = max_temp
        for temp in day:
            if temp < min_temp:
                min_temp = temp 
        
        average = total_temperature / counter
        day_counter += 1
        week += average
        
        print(f"Day {day_counter} average: {average.__round__(2)}")
        print(f"Max temperature: {max_temp}")
        print(f"Min temperature: {min_temp}")
        print()
    print(f"Week Average: {(week / 7).__round__(2)}")


if __name__ == "__main__":
    temp_teller()

