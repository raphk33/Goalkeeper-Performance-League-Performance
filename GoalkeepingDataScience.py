import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to normalize columns where higher values are better
def normalize_higher_is_better(column):
    return (column - column.min()) / (column.max() - column.min())

# Function to normalize columns where lower values are better
def normalize_lower_is_better(column):
    return (column.max() - column) / (column.max() - column.min())

# Load the excel file
file_path = r"C:\Users\rapha\OneDrive\Desktop\ENM 3440\GoalkeepingDataExcel.xlsx"
df = pd.read_excel(file_path)

# Normalizing the data
df['NPGA_norm'] = normalize_lower_is_better(df['NPG Allowed'])
df['NPSP_norm'] = normalize_higher_is_better(df['NPSavePctg'])
df['CleanSheets_norm'] = normalize_higher_is_better(df['Clean Sheets'])
df['PSxG_norm'] = normalize_lower_is_better(df['PSxG'])
df['PSxG_GA_norm'] = normalize_higher_is_better(df['PSxG - GA'])

# Calculating the weighted score
df['total_score'] = (df['NPGA_norm'] * 0.15 +
                     df['NPSP_norm'] * 0.25 +
                     df['CleanSheets_norm'] * 0.15 +
                     df['PSxG_norm'] * 0.10 +
                     df['PSxG_GA_norm'] * 0.35)

# Sorting the dataframe based on the total_score column
sorted_df = df.sort_values(by='total_score', ascending=False)

# Display the sorted teams with their scores
correlation = df['total_score'].corr(df['League Position'])
print(f"Correlation between Goalkeeper Rankings and Final League Position: {correlation:.2f}")


# 1. Scatter plot with line of best fit
plt.figure(figsize=(10, 6))
sns.regplot(x='total_score', y='League Position', data=df, ci=None)  # ci=None removes the confidence interval band
plt.title('Relationship between Goalkeeper Rankings and Final League Position')
plt.xlabel('Goalkeeper Ranking Score')
plt.ylabel('Final League Position')
plt.gca().invert_yaxis()  # To make the top league position (e.g., 1st) appear at the top
plt.show()

# 2. Distribution plot of goalkeeper rankings
plt.figure(figsize=(10, 6))
sns.histplot(df['total_score'], kde=True)
plt.title('Distribution of Goalkeeper Rankings')
plt.xlabel('Goalkeeper Ranking Score')
plt.ylabel('Frequency')
plt.show()







