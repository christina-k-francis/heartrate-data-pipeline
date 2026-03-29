"""
Here are utility functions for plotting/visualizing heartrate data
"""

import matplotlib.pyplot as plt

def create_lineplot(data: list, removed_data: dict, plot_name: str):
    """
    Description: This FX outputs a simple line plot of the provided heartrate data.
        Gaps in the line plot represent the location of values removed during cleaning.
    """

    # calculating length of original data before cleaning
    original_length = len(data) + len(removed_data)

    # building the full-length list with None at every removed original index
    plotting_data = []
    # tracking the cleaned indices
    cleaned_idx = 0
    for i in range(original_length):
        if i in removed_data:
            plotting_data.append(None)
        else:
            # ensure the data are numerical
            plotting_data.append(int(data[cleaned_idx]))
            cleaned_idx += 1

    # x-axis in minutes (one reading every 5 minutes)
    plotting_xaxis = range(0, 5 * original_length, 5)

    # flexible tick spacing: aim for ~20 ticks regardless of data length
    tick_step = max(5, (5 * original_length) // 25)
    # round up to the nearest multiple of 5 for clean labels
    tick_step = round(tick_step / 5) * 5

    # creating the plot
    plt.figure(figsize=(15, 5))
    plt.title('Heartrate Timeseries')
    plt.plot(plotting_xaxis, plotting_data,
             color='coral',
             linewidth=1.5,
             marker='s',
             ms=5,
             mfc='crimson')
    plt.xlabel('Minutes Elapsed')
    plt.xticks(range(0, 5 * original_length + tick_step, tick_step), rotation=45)
    plt.ylabel('Heartrate (BPM)')
    plt.yticks(range(50, 110, 5))
    plt.grid(True, which='both', alpha=0.3)
    plt.tight_layout()
    # saving the image
    output_dir = f'images/{plot_name}_heartrate_timeseries.png' 
    plt.savefig(output_dir)
    print(f'plot saved to {output_dir}!')

    plt.show()
