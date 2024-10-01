# Text Pre-processing with NLP
This project demonstrates basic text pre-processing techniques such as tokenization, stopword removal, spell correction, stemming, and lemmatization using Python's Natural Language Toolkit (NLTK), Spacy, and PySpellChecker libraries.

# Requirements
This project requires the following Python packages:

- NLTK: Used for tokenization, stopword removal, stemming, and lemmatization.
- Spacy: Used for advanced lemmatization and named entity recognition.
- PySpellChecker: Used for spell checking and correction.
- Certifi: To handle SSL certificates for downloading data in some systems.

# Prerequisites
Make sure you have Python installed on your system. You can download Python from here.

# Installation of Required Packages
Open a terminal or command prompt and follow these steps:
1. Clone the repository (if applicable) or download the code to your local machine.
2. Navigate to the project directory: `cd /path/to/your/project `
3. Install the required Python packages:
   - run the following commands to install the necessary packages: `pip install nltk spacy pyspellchecker certifi`
4. Download NLTK datasets:
   - NLTK requires some datasets for tokenization and stopword removal. In the script, the following datasets are automatically downloaded:
     `import nltk
      nltk.download('punkt')
      nltk.download('punkt_tab')
      nltk.download('wordnet')
      nltk.download('stopwords')`
5.Download the Spacy English model:
  - Run the following command to download the required Spacy model for lemmatization: `python -m spacy download en_core_web_sm`

# Running the Project
1. Ensure that assignment_data.txt is in the same directory as your script or provide the absolute path to the file.
2. Run the Python script: `python main.py`
   - The script will output the following steps:
       *  Original Tokens
       *  Tokens after Stopword Removal
       * Corrected Text after Spell Correction
       * Stemmed Words
       * Lemmatized Words


# Project Structure
1. `main.py`: The main Python script containing the text pre-processing code.
2. assignment_data.txt: The sample text file that is processed by the script.






