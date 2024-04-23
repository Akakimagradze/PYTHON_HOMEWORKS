def midpoint(x1, y1, x2, y2):
    x_midpoint = (x1 + x2) / 2
    y_midpoint = (y1 + y2) / 2
    result_tuple = (x_midpoint, y_midpoint)
    return result_tuple

if __name__ == "__main__":
    print(midpoint(2.4, 2.7, 4.2, 4.6)) # X midpoint = 3.3, Y midpoint - 3.65
    print(midpoint(5, 10, 15, 20)) # midpoint = 10.0, Y midpoint - 15.0
    print(midpoint(7, 3, 11, 9)) # midpoint = 9.0, Y midpoint - 6.0
    
