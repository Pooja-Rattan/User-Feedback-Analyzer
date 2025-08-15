import matplotlib.pyplot as plt
from collections import Counter
import string

# Step 1: Read feedback from file
with open("feedback.txt", "r") as file:
    text = file.read()

# Step 2: Clean and split words
text = text.lower()
text = text.translate(str.maketrans("", "", string.punctuation))
words = text.split()

# Step 3: Count word frequencies
word_counts = Counter(words)

# Step 4: Get top 5 most common words
top_words = word_counts.most_common(5)

# Step 5: Separate words and counts for plotting
labels, counts = zip(*top_words)

# Step 6: Plot
plt.bar(labels, counts)
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Top 5 Most Frequent Words in Feedback")
plt.show()