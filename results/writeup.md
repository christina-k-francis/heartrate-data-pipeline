1) Which file appears to represent the most active period? Explain using at least two metrics. Consider that this is a 30 year old participant and compare your output to the column titled "Target HR Zone 50-85%" within this link: https://www.heart.org/en/healthy-living/fitness/fitness-basics/target-heart-rates

The Target Heartrate Zone for 30-year olds while exercising is 95-162 BPM. It appears that Phase1 was likely the most active period, with average and median values of 87.3 and 91.5 BPMs respectively. 

2) Which file had the **poorest** data quality? How do you know?

It appears that the 'phase3.txt' file had the poorest data quality. This is because it had the largest number of blanks, nulls, and improbable readings. 

3) Suppose one heart-rate file contains the following cleaned values: `68, 70, 71, 72, 72, 73, 74, 75, 180`. The value 180 was recorded during a sensor glitch.

a) Calculate the range of this dataset.

Range with the glitch = 180 - 68 = 112
Range w/o the glitch = 75 - 68 = 7

b) Explain how the extreme value affects the range.

The extreme value causes a huge skew in the dataset, and increases the calculated range by 16 FOLD. 

c) Identify a different statistic that would better represent the typical variability of the dataset. Why would this measure be better?

The interquartile range (IQR) would be a better statistic that is more representative of the typical variability of the dataset. This is because, the IQR is the difference betwene the 75th and 25th percentile values. If the data is normally distributed, these values would sit on the upper and lower edges of the majority of all other values in the dataset. This makes it a better statistic for measuring variabilty.  

On the other hand, range values tend to be skewed by outlier large and small values, and is thus an unreliable statistical measure of variability. 