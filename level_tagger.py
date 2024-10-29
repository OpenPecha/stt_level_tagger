import pandas as pd

# Load the CSV file
df = pd.read_csv('./data/KH_1_to_89.csv')

# Define a function to categorize audio duration
def determine_level(duration):
    if duration < 4:
        return 'easy'
    elif 4 <= duration < 8:
        return 'medium'
    else:
        return 'hard'

# Apply the function to create the 'level' column
df['level'] = df['audio_duration'].apply(determine_level)

# Save the modified DataFrame to a new CSV file
df.to_csv('./data/catalog_with_level.csv', index=False)

print("File saved as catalog_with_level.csv with the new 'level' column.")
