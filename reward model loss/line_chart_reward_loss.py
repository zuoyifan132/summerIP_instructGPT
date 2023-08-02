import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file into a Pandas DataFrame
df = pd.read_csv('reward_loss.csv')

# Extract the x and y data
x = df['index']
y = df['Loss']

# Create a line chart using Matplotlib
fig, ax = plt.subplots()
ax.plot(x, y)

# Set the chart title and axis labels
ax.set_title('Reward Model Loss')
ax.set_xlabel('each batch')
ax.set_ylabel('loss value')

# Save the chart as a PNG file
fig.savefig('reward_loss_plot.png')

# Display the chart
plt.show()