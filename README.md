# wolof-language-model
Built language models for the African language Wolof. For this study, we mainly focus on Senegalese Wolof, and more precisely on the urban Wolof.

Following are the steps of the modeling process      
- scrape data from wolof Wikipedia
- retrieve data from https://github.com/ReaganHuang/ALFFA_PUBLIC/tree/master/ASR/WOLOF/LM
- clean the data (with cld2)
- modeling using NLTK
- validating using perplexity, which is a built-in function of nltk.lm
