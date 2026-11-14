print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu(): 
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)" )
    
def get_user_input():
    x=input()
    values=x.split(",")    
    float_values = [float(v) for v in values]
    return float_values

def calc_average(values): 
    average=sum(values)/len(values)
    return average
 
def find_min_max(values):
    value_min=int(min(values))
    value_max=int(max(values))
    return value_min,value_max

def sort_temperature():
    print()

def calc_median_temperature():
    print()

display_main_menu()
numbers=get_user_input()
print("Average value: ", calc_average(numbers))
print("Minimum value: ", find_min_max[0])
print("Minimum value: ", find_min_max[1])