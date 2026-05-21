# Context Analysis with Word Frequency, N-Grams, and TF–IDF

In this exercise, we will perform a context analysis of a text by finding the most common words, identifying common word combinations (n-grams), and calculating TF–IDF scores using the Gensim library. These techniques help us understand the themes and topics present in the text.

---

1. First, we need to install the Gensim library. You can do this by running the following command in your terminal:

   ```bash
   pip install --upgrade gensim
   ```

2. Now you can open the file `exercise_3.py`. In Exercise 1, we have preprocessed the text by lowercasing, tokenizing, lemmatizing, and removing stopwords. We will work with this preprocessed text for our context analysis. The file `exercise_3.py` already contains the preprocessing steps from Exercise 1, so you can start right there.
   You need to import the following modules after the existing import statements:

   ```python
   from collections import Counter
   from nltk.util import ngrams
   from gensim import corpora
   from gensim.models import TfidfModel
   import os
   ```

3. Next, we want to access our example text files. This time, we will load **all `.txt` files** from a folder (e.g. `../data/`) to later compare their vocabulary.

   ```python
   folder_path = '../data/'
   all_texts = []
   for filename in os.listdir(folder_path):
       if filename.endswith('.txt'):
           with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
               all_texts.append(file.read())
   ```

   Each element in the list `all_texts` now contains the text of one file.

4. In this exercise we want to look at the most common words and their contexts. We will start by defining a function called `word_frequency` that takes a list of tokens as input and returns the most common words in the text. You can use the `Counter` class from the `collections` module to count the occurrences of each word. The function should look like this:

   ```python
   def word_frequency(tokens, n=10):
       word_counts = Counter(tokens)
       return word_counts.most_common(n)
   ```

   The parameter `n` specifies how many of the most common words you want to return. You can call this function with the `clean_tokens` variable from Exercise 1 and print the result to see the most common words in the text.

5. Next, we will define a function called `find_ngrams` that takes a list of tokens and an integer `n` as input and returns the most common n-grams in the text. N-grams are contiguous sequences of `n` items from a given sample of text.

   ```python
   def find_ngrams(tokens, n=2, top_k=10):
       n_grams = ngrams(tokens, n)
       ngram_counts = Counter(n_grams)
       return ngram_counts.most_common(top_k)
   ```

   The parameter `n` specifies the size of the n-grams (e.g., 2 for bigrams, 3 for trigrams), and `top_k` specifies how many of the most common n-grams you want to return. You can call this function with the `clean_tokens` variable and print the result to see the most common bigrams in the text.


So, what did we learned about the sources?
- The most common words in the text give us an idea of the main themes and topics discussed. For example, if we see words like "witch," "trial," and "accused" frequently, it indicates that the text is likely about witch trials. However, this method simply counts the words without taking any other parameters into account.
- The n-grams help us identify common phrases or word combinations that might be significant in the context of the text. For example, if we find bigrams like "witch trial" or "accused witch," it suggests that these phrases are important in the narrative.
