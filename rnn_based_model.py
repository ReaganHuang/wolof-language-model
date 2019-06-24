from fastai import *
from fastai.text import *
from fastai.callbacks import *
import numpy as np
import spacy
import sys
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score


DATA_PATH = sys.argv[1]
EXTR_PATH = pathlib.Path(f"{DATA_PATH}/wiki_extr/wo")
LM_PATH = Path(f"{DATA_PATH}/model/wolooof/")
LM_PATH.mkdir(parents=True, exist_ok=True)
lang = 'wo'

# pretrained model
bs = 64
data= TextLMDataBunch.from_csv(LM_PATH, 'wolof_types.csv')
data.save('data_export.pkl')
data = load_data(LM_PATH, 'data_export.pkl', bs=bs)
learn = language_model_learner(data, AWD_LSTM, drop_mult=0.5, pretrained=False)
lr = 1e-2
lr *= bs/48 
learn.unfreeze()
learn.fit_one_cycle(10, lr, moms=(0.8,0.7))

# save pre-trained model and vocab
mdl_path = LM_PATH/'models'
mdl_path.mkdir(exist_ok=True)
lm_fns = [f'{lang}_wt', f'{lang}_wt_vocab']
learn.to_fp32().save(mdl_path/lm_fns[0], with_opt=False)
learn.data.vocab.save(mdl_path/(lm_fns[1] + '.pkl'))


# fine tune on new dataset
geoall = pd.read_csv(LM_PATH/'wiki_geo.csv')[['text','geo']]
train_df, test_df = train_test_split(geoall, test_size=0.2)
data_lm = (TextList.from_df(geoall, LM_PATH, cols='text')
        .split_by_rand_pct(0.1, seed=42)
        .label_for_lm()           
        .databunch(bs=bs, num_workers=1))

geoall = pd.read_csv(LM_PATH/'wiki_geo.csv')[['text','geo']]
train_df, test_df = train_test_split(geoall, test_size=0.2)

data_lm = (TextList.from_df(geoall, LM_PATH, cols='text')
    .split_by_rand_pct(0.1, seed=42)
    .label_for_lm()           
    .databunch(bs=bs, num_workers=1))
learn_lm = language_model_learner(data_lm, AWD_LSTM, pretrained_fnames=lm_fns, drop_mult=1.0)  # be careful about the path

lr = 1e-3
lr *= bs/48
learn_lm.unfreeze()
learn_lm.fit_one_cycle(8, lr, moms=(0.8,0.7))  # turn 1 to 8
learn_lm.save(f'{lang}fine_tuned')
learn_lm.save_encoder(f'{lang}fine_tuned_enc')

# build a classifier
data_clas = (TextList.from_df(geoall, LM_PATH, vocab=data_lm.vocab, cols='text')
    .split_by_rand_pct(0.1, seed=42)
    .label_from_df(cols='geo')
    .databunch(bs=bs, num_workers=1))
data_clas.save(f'{lang}_textlist_class')

data_clas = load_data(LM_PATH, f'{lang}_textlist_class', bs=bs, num_workers=1)

def f1(inp,targ): return f1_score(targ, np.argmax(inp, axis=-1))

learn_c = text_classifier_learner(data_clas, AWD_LSTM, drop_mult=0.5)
learn_c.load_encoder(f'{lang}fine_tuned_enc')
learn_c.freeze()

lr=2e-2
lr *= bs/48
learn_c.fit_one_cycle(2, lr, moms=(0.8,0.7))
learn_c.freeze_to(-2)
learn_c.fit_one_cycle(2, slice(lr/(2.6**4),lr), moms=(0.8,0.7))
learn_c.freeze_to(-3)
learn_c.fit_one_cycle(2, slice(lr/2/(2.6**4),lr/2), moms=(0.8,0.7))
learn_c.unfreeze()
learn_c.fit_one_cycle(1, slice(lr/10/(2.6**4),lr/10), moms=(0.8,0.7))
learn_c.save(f'{lang}clas')

# prediction 
preds,targs = learn_c.get_preds(ordered=True)
print(accuracy(preds,targs),f1(preds,targs))










