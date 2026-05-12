# 📘 Assignment: Python Text Processing

## 🎯 Objective

Master essential text processing techniques including string manipulation, file I/O operations, and text analysis. You'll build a text analysis tool that reads files, processes text, and generates useful insights from the data.

## 📝 Tasks

### 🛠️	Text File Reader and Analyzer

#### Description
Write a Python program that reads a text file and performs basic text analysis. Your program should open a file, read its contents, and compute statistics about the text (word count, character count, and line count).

#### Requirements
Completed program should:

- Read the contents of a text file provided by the user
- Calculate the total number of lines, words, and characters
- Display the results in a clear, formatted output
- Handle the case where the file doesn't exist with an appropriate error message


### 🛠️	Text Transformation and Cleaning

#### Description
Extend your program to clean and transform the text. Implement functions that remove extra whitespace, convert text to different cases, and filter out common words (stopwords). Apply these transformations to the file content and save the results.

#### Requirements
Completed program should:

- Remove leading/trailing whitespace and collapse multiple spaces into one
- Implement a function to convert text to uppercase, lowercase, or title case
- Filter out common stopwords (e.g., "the", "a", "and", "is") from the text
- Save the cleaned text to a new output file
- Display before/after comparison of text statistics


### 🛠️	Advanced Text Search and Replace

#### Description
Create advanced text processing features. Implement functions to search for specific words or patterns in the text, count occurrences of words, and perform find-and-replace operations while preserving case when possible.

#### Requirements
Completed program should:

- Search for a word in the text and report all line numbers where it appears
- Count word frequencies and identify the most common words (excluding stopwords)
- Implement a case-preserving find-and-replace function (if word is capitalized, keep replacement capitalized)
- Generate a summary report showing word frequency statistics
- Export the word frequency data to a CSV file with columns: word, frequency, percentage
