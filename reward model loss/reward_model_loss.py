import pandas as pd

import csv

# Open the input file
with open('input_file.txt', 'r') as f:
    lines = f.readlines()

# Extract the loss numbers
losses = []
for line in lines:
    if 'loss=' in line:
        loss = line.split('loss=')[1].strip()
        losses.append(loss)

# Write the losses to a CSV file
with open('output_file.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Loss'])
    for loss in losses:
        writer.writerow([loss])

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('reward_loss.csv')

# Add an index column to the DataFrame
df['index'] = range(1, len(df)+1)

# Save the DataFrame back to a CSV file
df.to_csv("reward_loss.csv")