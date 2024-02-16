import matplotlib.pyplot as plt
import datetime

# Set the font family to Arial
plt.rcParams['font.family'] = 'Arial'

# Read data from a .txt file
data_file = 'date_wordCount_pageCount.txt'  # file name

# Initialize empty lists to store data
dates = []
word_counts = []
pages = []

# Read data from the file
with open(data_file, 'r') as file:
    for line in file:
        date_str, count_str, pages_str = line.strip().split()
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        word_count = int(count_str)
        page_count = int(pages_str)
        dates.append(date)
        word_counts.append(word_count)
        pages.append(page_count)

# Create the plot
fig, ax1 = plt.subplots(figsize=(10, 8))


lns1 = ax1.plot(dates, word_counts, linestyle='-', color='teal', label='Word Count',  marker='o')  # Word count on the left y-axis
ax1.set_xlabel('Date', fontsize=16, fontweight='bold',labelpad=10)
ax1.set_ylabel('Word Count', fontsize=16, fontweight='bold', labelpad=20, color = 'teal')

# Customize the x-axis date format
plt.gcf().autofmt_xdate()
plt.xticks(rotation=45)
xticks = []
xtick_labels = []
for i, date in enumerate(dates):
    xticks.append(date)
    if i % 3 == 0:
        xtick_labels.append(date.strftime('%d-%m-%y'))
    else:
        xtick_labels.append('')

plt.xticks(xticks, xtick_labels, fontsize=12)

# Adjust the fontsize of y-axis tick labels
plt.yticks(fontsize=12)

# Make the grid lines less visible by adjusting alpha
plt.grid(True, linestyle='-', alpha=0.3)


# Create a second y-axis for page count on the right side
ax2 = ax1.twinx()
lns2 = ax2.plot(dates, pages, linestyle='-', color='plum', label='Page Count',  marker='o')  # Page count on the right y-axis
ax2.set_ylabel('Page Count', fontsize=16, fontweight='bold', labelpad=20, color = 'plum')

# Set labels and title
plt.title('Thesis Progress', fontsize=16, fontweight='bold')

# Make the grid lines less visible by adjusting alpha
plt.grid(True, linestyle='-', alpha=0.3)

# Customize the x-axis date format
plt.gcf().autofmt_xdate()
plt.xticks(rotation=45)
xticks = []
xtick_labels = []
for i, date in enumerate(dates):
    xticks.append(date)
    if i % 1 == 0:
        xtick_labels.append(date.strftime('%d-%m-%y'))
    else:
        xtick_labels.append('')

plt.xticks(xticks, xtick_labels, fontsize=12)

# Adjust the fontsize of y-axis tick labels
plt.yticks(fontsize=12)

# Remove grid lines
#plt.grid(False)

# Customize the x-axis date format
plt.gcf().autofmt_xdate()
plt.xticks(rotation=45)
xticks = []
xtick_labels = []
for i, date in enumerate(dates):
    xticks.append(date)
    if i % 3 == 0:
        xtick_labels.append(date.strftime('%d-%m-%y'))
    else:
        xtick_labels.append('')

plt.xticks(xticks, xtick_labels, fontsize=12)
# Adjust the fontsize of y-axis tick labels
plt.yticks(fontsize=12)


# Make the grid lines less visible by adjusting alpha
plt.grid(True, linestyle='--', alpha=0.3)

# Add legend to the plot
lns = lns1+lns2
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc="upper left", fontsize = 12,  frameon=False)


# Save the plot as an image (e.g., PNG format)
plt.savefig('thesis_word_and_page_counts_over_time.png')

# Show the plot
#plt.show()