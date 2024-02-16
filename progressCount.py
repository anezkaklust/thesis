import matplotlib.pyplot as plt
import matplotlib.dates as mdates  # Import the dates module
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
plt.figure(figsize=(10, 8))  # Adjust the figure size as needed
plt.plot(dates, word_counts, linestyle='-', color = 'teal', marker='o') # marker='o'
plt.xlabel('Date', fontsize=16, fontweight='bold',labelpad=10)  # Set the fontsize for the x-axis title
plt.ylabel('Word Count', fontsize=16, fontweight='bold', labelpad=20)  # Set the fontsize and fontweight for the y-axis title with an offset
plt.title('Thesis Progress', fontsize=16, fontweight='bold')
plt.grid(True)

# Label every 7th day
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

# Customize the x-axis date format
plt.gcf().autofmt_xdate()
plt.xticks(rotation=45)

# Make the grid lines less visible by adjusting alpha
plt.grid(True, linestyle='--', alpha=0.3)
# Remove the grid lines
#plt.grid(False)

# Remove borders
#plt.gca().spines["top"].set_alpha(0.3)    
#plt.gca().spines["bottom"].set_alpha(0.3)
#plt.gca().spines["right"].set_alpha(0.3)    
#plt.gca().spines["left"].set_alpha(0.3) 


# Save the plot as an image (e.g., PNG format)
plt.savefig('thesis_word_counts_over_time.png')

# Show the plot
#plt.show()

# Create the second plot for page counts
plt.figure(figsize=(10, 8))
plt.plot(dates, pages, linestyle='-', color='plum',  marker='o')  # Change the color to orange for page counts
plt.xlabel('Date', fontsize=16, fontweight='bold', labelpad=10)
plt.ylabel('Page Count', fontsize=16, fontweight='bold', labelpad=20)
plt.title('Thesis Progress', fontsize=16, fontweight='bold')
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
plt.grid(True, linestyle='--', alpha=0.4)  # Change the grid color to orange for page counts
plt.yticks(fontsize=12)
plt.xticks(rotation=45)

# Remove borders
#plt.gca().spines["top"].set_alpha(0.3)    
#plt.gca().spines["bottom"].set_alpha(0.3)
#plt.gca().spines["right"].set_alpha(0.3)    
#plt.gca().spines["left"].set_alpha(0.3) 

plt.savefig('thesis_page_counts_over_time.png')