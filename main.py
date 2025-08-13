import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

# Hide the main Tkinter window
root = tk.Tk()
root.withdraw()

# Open file dialog
file_path = filedialog.askopenfilename(
    title="Select a text file",
    filetypes=[("Text files", "*.txt")]
)

print(f"Selected file: {file_path}")
#nltk.download("stopwords")

#file_path=r"C:\Users\Dell\Desktop\et3 task\large text.txt"

with open(file_path,"r",encoding="utf-8") as file:  #opening the file in read mode
    text = file.read().lower()  #reading the file contents and converting all text to lower

# making a string with all available characters so that numbers and punctuations are ignored
allowed_chars = "abcdefghijklmnopqrstuvwxyz "

text_no_punct_nums = []
for char in text:
    if char in allowed_chars:
        text_no_punct_nums.append(char)
    else:
        text_no_punct_nums.append(" ")  
text_no_punct_nums = "".join(text_no_punct_nums)

#removing stopwords and words with length less than or equal to 2
stop_words = stopwords.words("english")
words = text_no_punct_nums.split()  # split into words
filtered_words = [w for w in words if w not in stop_words and len(w) >= 2]

#counting frequency for each word
word_freq = {}

for word in filtered_words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

#sort them with top 10 most frequent words
sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

# printing top 10 words
for word, count in sorted_words[:10]:
    print(word, ":", count)

# generating bar chart of the top words
top_10 = sorted_words[:10]
top_words, top_counts = zip(*top_10)

plt.figure(figsize=(10, 6))
plt.bar(top_words, top_counts, color='skyblue')
plt.title("Top 10 Words Frequency")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.show()
