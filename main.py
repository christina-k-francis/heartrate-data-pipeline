import utils.calc_stats as cs
import utils.clean_data as cd

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
    cleaned_list, removed_values = cd.clean_heartrate_data(data)

    # calculating descriptive statistics
    avg_val = cs.average(data)
    median_val = cs.median(data)
    range_val = cs.range(data)
    rolling_average = cs.rolling_avg(data, k)
    variance_val = cs.variance(data)
    stdev_val = cs.stdev(variance_val)

    # printing out descriptive statistics to the console
    print(f'Filename: {file}')
    print('DESCRIPTIVE STATISTICS:')
    print(f'Range = {range_val}')
    print(f'Median = {median_val}')
    print(f'Average = {avg_val}')
    print(f'Rolling Average ({k}) = {rolling_average}')
    print(f'Variance = {variance_val}')
    print(f'Standard Deviation = {stdev_val}')
    # printing out a data quality measure to the console
    print(f'Number of Removed Values = {len(removed_values)}\n')

if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")
