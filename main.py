def clean_heartrate_data(data: list) -> tuple:
    """
    Description: FX cleans raw heart-rate data by removing malformed or impossible values.
    """
    # documenting all removed values (missing + impossible)
    removed_values = []

    # removing blank/null values
    for idx, val in enumerate(data):
        if val == '':
            # removing the blank record
            removed_values.append(data[idx])
            del data[idx]
        if val == 'NO DATA':
            # removing the missing record
            removed_values.append(data[idx])
            del data[idx]

    # normal adult heart rate: 60-100 bpm
    for idx, val in enumerate(data):
        
        # BPM < 60 suggest bradycardia, illness, or that the person is generally fit
        if int(val) < 60:
            # ensuring we're in a valid index range
            if idx > 1: 
                # check if BPM abnormally low for >= 15 minutes
                if (int(data[idx-1]) < 60) & (int(data[idx-2]) < 60):
                    # remove the likely malformed record
                    removed_values.append(data[idx])
                    del data[idx]
            # ensuring we're in a valid index range
            if idx < (len(data)-3):
                # check if BPM abnormally low for >= 15 minutes
                if (int(data[idx+1]) < 60) & (int(data[idx+2]) < 60):
                    # remove the likely malformed record
                    removed_values.append(data[idx])
                    del data[idx]
        
        # BPM > 100 suggest trachycardia, illness, stress, or high intensity cardio
        if int(val) > 100:
            # ensuring we're in a valid index range
            if idx > 1:
                # check if BPM abnormally high for >= 15 minutes
                if (int(data[idx-1]) > 100) & (int(data[idx-2]) > 100):
                    # remove the likely malformed record
                    removed_values.append(data[idx])
                    del data[idx]
            # ensuring we're in a valid index range
            if idx < (len(data)-3):
                # check if BPM abnormally high for >= 15 minutes
                if (int(data[idx+1]) > 100) & (int(data[idx+2]) > 100):
                    # remove the likely malformed record
                    removed_values.append(data[idx])
                    del data[idx]
    
    # outputting the cleaned dataset + removed values
    return data, removed_values


def average(data: list) -> float:
    """
    Definition: FX calculates the average of a list of integers using a for-loop. Assumes data is clean.
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
    Definition: FX returns the median value of the given list of integers
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


def run(file: str, k: int = 2):
    """
    Description:
        FX processes heart rate data from the a file by cleaning and
        calculating summary statistics. Prints out final values.

    Input:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').
        k (int): Interval for calculating the rolling average

    Output:
        float, float, float: average, median, and range.
    """
    data = []

    # reading the .txt heart rate file
    with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
    # creating a list of heart rate values, removing line breaks
    data = content.split('\n')

    # cleaning the data and removing invalid entries
    cleaned_list, removed_values = clean_heartrate_data(data)

    # calculating the average, median, range, and rolling average
    avg_val = average(data)
    median_val = median(data)
    range_val = range(data)
    rolling_average = rolling_avg(data, k)

    # printing out descriptive statistics to the console
    print(f'Filename: {file}')
    print('DESCRIPTIVE STATISTICS:')
    print(f'Average = {avg_val}')
    print(f'Median = {median_val}')
    print(f'Range = {range_val}')
    print(f'Rolling Average ({k}) = {rolling_average}')
    # printing out a data quality measure to the console
    print(f'Number of Removed Values = {len(removed_values)}\n')

if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")
