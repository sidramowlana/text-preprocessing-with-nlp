import nltk
import ssl
import certifi

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import spacy
from spellchecker import SpellChecker
ssl._create_default_https_context = ssl._create_unverified_context

# Download necessary NLTK datasets
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('stopwords')

# Load Spacy for lemmatization and named entity recognition
nlp = spacy.load("en_core_web_sm")

# Open the file and read its contents
with open('assignment_data.txt', 'r', encoding='utf-8') as file:
    text_data = file.read()

# Now text_data contains the content of assignment_data.txt
print("text data: "+ text_data)  # Optional: To check the content read from the file

# Tokenization
print("Start Tokenizing the data")
tokens = word_tokenize(text_data)

# Output results
print("Original Tokens:", tokens)
print("**********************************************************\n")