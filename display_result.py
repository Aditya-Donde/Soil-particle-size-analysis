import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Particle width data in mm
particle_widths = [
]

# Convert to numpy array for easier manipulation
particle_widths = np.array(particle_widths)

# Summary Statistics
mean_width = np.mean(particle_widths)
median_width = np.median(particle_widths)
std_width = np.std(particle_widths)
min_width = np.min(particle_widths)
max_width = np.max(particle_widths)

print(f"Mean Width: {mean_width:.2f} mm")
print(f"Median Width: {median_width:.2f} mm")
print(f"Standard Deviation: {std_width:.2f} mm")
print(f"Minimum Width: {min_width:.2f} mm")
print(f"Maximum Width: {max_width:.2f} mm")

# Histogram
plt.figure(figsize=(10, 6))
plt.hist(particle_widths, bins=30, edgecolor='black')
plt.title('Histogram of Particle Widths')
plt.xlabel('Width (mm)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Cumulative Distribution Plot
plt.figure(figsize=(10, 6))
sorted_widths = np.sort(particle_widths)
cumulative = np.cumsum(sorted_widths)
cumulative_percentage = 100 * cumulative / cumulative[-1]
plt.plot(sorted_widths, cumulative_percentage, marker='.', linestyle='none')
plt.title('Cumulative Distribution of Particle Widths')
plt.xlabel('Width (mm)')
plt.ylabel('Cumulative Percentage (%)')
plt.grid(True)
plt.show()

# Box Plot
plt.figure(figsize=(10, 6))
sns.boxplot(x=particle_widths)
plt.title('Box Plot of Particle Widths')
plt.xlabel('Width (mm)')
plt.grid(True)
plt.show()

