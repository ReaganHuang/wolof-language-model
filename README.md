# wolof-language-model
Wolof (/ˈwoʊlɒf/) is a language of Senegal. About 12 million people speak this language in Africa. This project aims at builting language models for Wolof without labels. For this study, we mainly focus on Senegalese Wolof, and more precisely on the urban Wolof.

Following are the steps of the whole process      
- **scrape data from wolof Wikipedia** (reference: https://github.com/attardi/wikiextractor)
  * run WikiExtractor.py and get html files
  * save all html files in one: `cat * > allhtml.html`
- **clean the Wikipedia data** (with cld2)
  * run clean_text.py to clean Wikipedia data `python clean_text.py all.html  > cleaned_Wiki.txt`
- **retrieve other data** from https://github.com/ReaganHuang/ALFFA_PUBLIC/tree/master/ASR/WOLOF/LM
- **modeling using NLTK**
  * statistical language model and its predictions
- **validating using perplexity**
  * performance of a specific model
  * compare models that are built with different data source

