# Wolof-language-model
Wolof (/ˈwoʊlɒf/) is a language of Senegal. About 12 million people speak this language in Africa. This project aims at builting language models for Wolof without labels. For this study, we mainly focus on Senegalese Wolof, and more precisely on the urban Wolof.

Following are the steps of the process of a statistical language model and a neural network.

## Statistical Language Model
- **scrape data from wolof Wikipedia** (reference: https://github.com/attardi/wikiextractor)
  * run WikiExtractor.py and get html files
  * save all html files in one: `cat * > allhtml.html`
- **clean the Wikipedia data** (with cld2)
  * run clean_text.py to clean Wikipedia data `python clean_text.py all.html  > cleaned_Wiki.txt`
- **retrieve other data** from https://github.com/ReaganHuang/ALFFA_PUBLIC/tree/master/ASR/WOLOF/LM
- **build a statistical language model**
  * statistical language model and its predictions using NLTK
- **validating using perplexity**
  * performance of a specific model
  * compare models that are built with different data source

## RNN based Language Model
- **scrape data from Wolof Wikipedia by article** (reference: https://github.com/fastai/fastai/tree/master/courses/dl2/imdb_scripts)  
- **create labels**
  * scrape the translation for Wolof Wikipedia articles
  * Label each article as "geo" or "nongeo"
- **build an RNN based language model**
  * scrape the translation for Wolof Wikipedia articles
  * Label each article as "geo" or "nongeo"
- **prediction and validation** 

