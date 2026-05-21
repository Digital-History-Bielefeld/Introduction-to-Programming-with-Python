import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import os
from collections import Counter
from nltk.util import ngrams
from gensim import corpora
from gensim.models import TfidfModel

nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('stopwords')

lemmatizer = WordNetLemmatizer()

def preprocess_text(raw_text, custom_stopwords=[]):
    text = raw_text.lower()
    tokens_full = nltk.word_tokenize(text)
    tokens= []
    for token in tokens_full:
        if token.isalpha():
            tokens.append(token)
    lemmas = []
    for token in tokens:
        lemma = lemmatizer.lemmatize(token)
        lemmas.append(lemma)
    stop_words = stopwords.words('english')
    stop_words.extend(custom_stopwords)
    clean_tokens = []
    for lemma in lemmas:
        if lemma not in stop_words:
            clean_tokens.append(lemma)
    return clean_tokens

def word_frequency(tokens, top_n=10):
    word_counts = Counter(tokens)
    return word_counts.most_common(top_n)

def find_ngrams(tokens, n=2, top_k=10):
    n_grams = ngrams(tokens, n)
    ngram_counts = Counter(n_grams)
    return ngram_counts.most_common(top_k)

folder_path = './section-3/data/'
all_texts = []
for filename in os.listdir(folder_path):
  with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
      all_texts.append(file.read())


our_text = all_texts[0]
custom_stopwords = ['thee', 'thy', 'thou', "wa", "made"]
clean_tokens = preprocess_text(our_text, custom_stopwords=custom_stopwords)

common_words = word_frequency(clean_tokens, top_n=10)
#print(common_words)

common_bigrams = find_ngrams(clean_tokens, n=2, top_k=10)
# print(common_bigrams)

common_trigrams = find_ngrams(clean_tokens, n=3, top_k=10)
# print(common_trigrams)

all_tokens = []
for text in all_texts:
    tokens = preprocess_text(text, custom_stopwords=custom_stopwords)
    all_tokens.append(tokens)
