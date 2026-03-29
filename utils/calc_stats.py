"""
Here are utility functions for calculating statistics while evaluating heartrate data
"""

def average(data: list) -> float:
    """
    Description: FX calculates the average of a list of integers using a for-loop. Assumes data is clean.
    """
    sum = 0
    for val in data:
        # calculating a running sum of values in the dataset
        sum += int(val)
    # calculating the average
    avg = sum/len(data)
    # output the avg value
    return round(avg, 2)


def median(data: list) -> float:
    """
    Description: FX returns the median value of the given list of integers
    """
    # if the dataset length is even
    if len(data) % 2 == 0:
        # the median is the avg. between the 2 middle values
        median_value = float(( int(data[len(data)//2]) + int(data[(len(data)//2)-1])) / 2)
    # if the dataset length is odd
    elif len(data) % 2 == 1:
        # the median is the middle value on the dataset
        median_value = float(data[len(data)//2])
    # output the median value rounded to 2 decimal places
    return round(median_value, 2)


def range(data: list) -> float:
    """
    Description: FX returns the range (max-min) of the given list of integers
    """
    # converting every value to integer
    data_integer = [int(val) for val in data]
    
    # finding the largest value
    max = 0
    for val in data_integer:
        if val > max:
            max = val
    
    # finding the smallest value
    min = 120
    for val in data_integer:
        if val < min:
            min = val
    
    # calculating the range
    range_value = max - min

    # ouput the range value
    return range_value


def rolling_avg(data: list, k: int) -> float:
    """
    Description: FX calculates the average of integer values at K-interval indices 
    """
    sum = 0
    for idx, val in enumerate(data):
        if idx // k == 0:
            # calc running sum of k-interval values 
            sum += int(val)
    avg = sum/len(data)
    # output the avg value
    return round(avg, 2)


def variance(data: list) -> float:
    # squared deviation = (xi - xbar)^2
    squared_devs = []
    for val in data:
        # keeping a running list of squared deviations
        squared_devs.append((int(val) - average(data))**2)
    # calculating sample variance = average of squared deviations
    var = sum(squared_devs) / (len(data) - 1)
    # output rounded variance value
    return round(var, 2)


def stdev(variance: float) -> float: 
    # calculating stdev = square root of the variance 
    stdev = variance ** 0.5  
    # output rounded standard deviation
    return round(stdev, 2)    