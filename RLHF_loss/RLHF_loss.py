import re
import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the txt file
with open('RLHF_loss.txt', 'r') as file:
    data = file.read()

# Use regular expressions to extract the epoch, batch, loss, and total_loss values
pattern = r'epoch (\d+), batch (\d+)/\d+, total_loss=\d+\.\d+, len \d+ ,loss=(\d+\.\d+)'
matches = re.findall(pattern, data)

# Create a Pandas DataFrame from the extracted data
df = pd.DataFrame(matches, columns=['epoch', 'batch', 'loss'])
df['loss'] = df['loss'].astype(float)

# Plot the loss values against the index
plt.plot(df.index, df['loss'])
plt.title('RL-agent Loss')
plt.xlabel('each 100 batch')
plt.ylabel('Loss value')

# Save the plot as a PNG file
plt.savefig('loss_plot.png')

# Display the plot
plt.show()