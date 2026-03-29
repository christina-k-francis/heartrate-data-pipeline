"""
Here are utility functions for cleaning heartrate data
"""

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