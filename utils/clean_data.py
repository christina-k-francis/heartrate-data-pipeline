"""
Here are utility functions for cleaning heartrate data
"""

def clean_heartrate_data(data: list) -> tuple:
    """
    Description: FX cleans raw heart-rate data by removing malformed or impossible values.
    """
    # documenting all removed values (missing + impossible)
    removed_values = {}

    # removing blank and missing values
    for idx, val in enumerate(data):
        if val == '' or val == 'NO DATA':
            removed_values[idx] = val

    # dropping blank/missing values from data (iterating in reverse to preserve indices)
    for idx in sorted(removed_values.keys(), reverse=True):
        del data[idx]

    # tracking indices for second pass removal to avoid mid-loop index shifting
    to_remove = {}
    # normal adult heart rate: 60-100 bpm
    for idx, val in enumerate(data): 
        # BPM < 60 suggest bradycardia, illness, or that the person is generally fit
        if int(val) < 60:
            # ensuring we're in a valid index range
            if idx > 1: 
                # check if BPM abnormally low for >= 15 minutes
                if (int(data[idx-1]) < 60) & (int(data[idx-2]) < 60):
                    # remove the likely malformed record
                    to_remove[idx] = val
            # ensuring we're in a valid index range
            if idx < (len(data)-3):
                # check if BPM abnormally low for >= 15 minutes
                if (int(data[idx+1]) < 60) & (int(data[idx+2]) < 60):
                    # remove the likely malformed record
                    to_remove[idx] = val
        
        # BPM > 100 suggest trachycardia, illness, stress, or high intensity cardio
        if int(val) > 100:
            # ensuring we're in a valid index range
            if idx > 1:
                # check if BPM abnormally high for >= 15 minutes
                if (int(data[idx-1]) > 100) & (int(data[idx-2]) > 100):
                    # remove the likely malformed record
                    to_remove[idx] = val
            # ensuring we're in a valid index range
            if idx < (len(data)-3):
                # check if BPM abnormally high for >= 15 minutes
                if (int(data[idx+1]) > 100) & (int(data[idx+2]) > 100):
                    # remove the likely malformed record
                    to_remove[idx] = val

    # now removing malformed/improbable records
    null_removed_count = len(removed_values)
    for local_idx in sorted(to_remove.keys(), reverse=True):
        # computing original idx based on already-removed blank entries
        original_idx = local_idx + null_removed_count
        # documenting newly removed improbable value
        removed_values[original_idx] = to_remove[local_idx]
        # deleting the improbable/malformed record
        del data[local_idx]

    # ensuring all values are numerical integers
    data = [int(val) for val in data]
    
    # outputting the cleaned dataset + removed values
    return data, removed_values