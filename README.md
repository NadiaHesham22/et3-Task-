# et3-Task-
## Word Frequency Analyzer
A program that analyzes a .txt file and reports word frequencies.

- It is a small program written in Python using VS code and two libraries NLTK and Matplotlib
- The approach was to clean the text by removing punctuation, numbers, stopwords, and very short words (two characters or fewer) so that the remaining words are more meaningful, producing clearer and more relevant results.

## How to run the program 

1. **Create a Python virtual environment**
    ```bash
    python -m venv env
    ```

2. **Activate the environment**
    ```bash
    # Windows
    env\Scripts\activate
    ```

3. **Install required libraries**
    ```bash
    pip install nltk
    pip install matplotlib
    ```

## Extra Features 
- The program has the feature to generate a bar chart of the top words.
- The ability to choose the text file at runtime.

  ## Example output for the bar chart when we tested a large text with 700 words

<img width="1051" height="779" alt="Capture" src="https://github.com/user-attachments/assets/240c7fda-8516-4a22-9f07-5e620487505f" />
