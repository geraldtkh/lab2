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
    return [value_min,value_max]

def sort_temperature(values):
    sorted_values = sorted(values)
    return sorted_values

def calc_median_temperature(values):
    sorted_values = sort_temperature(values)
    n = len(sorted_values)
    mid = n // 2
    if n % 2 == 1:
        median = sorted_values[mid]
    else:
        median = (sorted_values[mid - 1] + sorted_values[mid]) / 2
    return median
    
def main(): 
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python") 
    display_main_menu() 
    num_list = get_user_input() 
    print("Average value: ", calc_average(num_list))
    print("Min/Max =", find_min_max(num_list))
    print("Sorted =", sort_temperature(num_list))
    print("Median =", calc_median_temperature(num_list))
    
if __name__ == "__main__":
    main()