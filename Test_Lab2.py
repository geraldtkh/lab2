import Lab2

def test_min_max():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    correct_result=[11,90]
    result=Lab2.find_min_max(input_arr)
    assert (result==correct_result)

def test_calc_average():
    input_arr = [2,4,6,8,10,12,14,16,18]
    correct_result=10
    result=Lab2.calc_average(input_arr)
    assert (result==correct_result)
    
def test_median_temperature():
    input_arr = [2,4,6,8,10,12,14,16,18]
    correct_result=10
    result=Lab2.calc_median_temperature(input_arr)
    assert (result==correct_result)