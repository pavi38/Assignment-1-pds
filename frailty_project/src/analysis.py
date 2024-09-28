import matplotlib.pyplot as plt
import pandas as pd

frailty_df = pd.read_csv('data_clean/clean_frailty_data.csv')

# Define colors based on frailty ('blue' for 'N' and 'red' for 'Y')
colors = ['red' if f == 'Y' else 'grey' for f in frailty_df['Frailty']]

# Create scatter plot
plt.scatter(frailty_df['Age'], frailty_df['Grip Strength'], c=colors)

# Add labels and title
plt.xlabel('Age')
plt.ylabel('Grip Strength')
plt.title('Age vs Grip Strength with Frailty Indication')

# Display plot
plt.savefig('results/age_Vs_grip.png')
print("graph saved")