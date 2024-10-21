import os
from collections import Counter
import socket

# Function to read the file and return word counts
def word_count(file_path):
    with open(file_path, 'r') as file:
        text = file.read().replace('\n', ' ')
        words = text.split()
        return words

# Function to handle contractions by splitting them
def split_contractions(words):
    expanded_words = []
    for word in words:
        word = word.replace("’", "'")  # Replace smart quotes with apostrophes
        if "'" in word:
            expanded_words.extend(word.split("'"))
        else:
            expanded_words.append(word)
    return expanded_words

# Read both files
if_words = word_count('/home/data/IF.txt')
always_words = word_count('/home/data/AlwaysRememberUsThisWay.txt')

# Calculate total word counts
if_word_count = len(if_words)
always_word_count = len(always_words)
grand_total = if_word_count + always_word_count

# Find top 3 most frequent words in IF.txt
if_counter = Counter(if_words)
top_3_if = if_counter.most_common(3)

# Handle contractions and find top 3 in AlwaysRememberUsThisWay.txt
expanded_always_words = split_contractions(always_words)
always_counter = Counter(expanded_always_words)
top_3_always = always_counter.most_common(3)

# Get the IP address of the machine running the container
ip_address = socket.gethostbyname(socket.gethostname())

# Write results to result.txt
with open('/home/data/output/result.txt', 'w') as result_file:
    result_file.write(f"IF.txt word count: {if_word_count}\n")
    result_file.write(f"AlwaysRememberUsThisWay.txt word count: {always_word_count}\n")
    result_file.write(f"Grand total word count: {grand_total}\n")
    result_file.write(f"Top 3 words in IF.txt: {top_3_if}\n")
    result_file.write(f"Top 3 words in AlwaysRememberUsThisWay.txt (handling contractions): {top_3_always}\n")
    result_file.write(f"Container IP address: {ip_address}\n")

# Print result to the console
with open('/home/data/output/result.txt', 'r') as result_file:
    print(result_file.read())
