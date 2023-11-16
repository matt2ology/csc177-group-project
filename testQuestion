import pandas as pd

# Given data
dictionary_data = {
    'Name': ['A', 'B', 'C', 'D', 'E'],
    'Math': [87, 90, 51, 25, 98],
    'English': [50, 68, 45, 88, 14]
}

dataframe = pd.DataFrame(dictionary_data)

# Calculate statistics for Math
math_mean = dataframe['Math'].mean()
math_std = dataframe['Math'].std()
math_25_percentile = dataframe['Math'].quantile(0.25)
math_50_percentile = dataframe['Math'].median()
math_75_percentile = dataframe['Math'].quantile(0.75)

# Calculate statistics for English
english_mean = dataframe['English'].mean()
english_std = dataframe['English'].std()
english_25_percentile = dataframe['English'].quantile(0.25)
english_50_percentile = dataframe['English'].median()
english_75_percentile = dataframe['English'].quantile(0.75)

print(f"Math:\nMean: {math_mean}\nStandard Deviation: {math_std}\n25th Percentile: {math_25_percentile}\n50th Percentile: {math_50_percentile}\n75th Percentile: {math_75_percentile}\n")
print(f"English:\nMean: {english_mean}\nStandard Deviation: {english_std}\n25th Percentile: {english_25_percentile}\n50th Percentile: {english_50_percentile}\n75th Percentile: {english_75_percentile}")