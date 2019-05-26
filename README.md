# wolof-language-model
Wolof (/ˈwoʊlɒf/) is a language of Senegal. About 12 million people speak this language in Africa. This project aims at builting language models for Wolof without labels. For this study, we mainly focus on Senegalese Wolof, and more precisely on the urban Wolof.

Following are the steps of the whole process      
- scrape data from wolof Wikipedia (reference: https://github.com/attardi/wikiextractor)
  * run WikiExtractor.py and get html files
  * save all html files in one: `cat * > allhtml.html`
- clean the Wikipedia data (with cld2)

- retrieve other data from https://github.com/ReaganHuang/ALFFA_PUBLIC/tree/master/ASR/WOLOF/LM
- modeling using NLTK
- validating using perplexity, which is a built-in function of nltk.lm

