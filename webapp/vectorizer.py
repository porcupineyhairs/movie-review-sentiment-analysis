from sklearn.feature_extraction.text import HashingVectorizer
import re, os, pickle

cur_dir = os.path.dirname(__file__)
stop = pickle.load(open(os.path.join(cur_dir, 
                        'pickled_objects', 'stopwords.pkl'), 'rb'))
def tokenizer(text):
    text = re.sub('<[^>]*>', '', text)
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text)
    text = re.sub('[\W]+',' ',text.lower()) + ' '.join(emoticons).replace('-','')
    tokenized = [w for w in text.split() if w not in stop]
    return tokenized

vect = HashingVectorizer(decode_error='ignore',
                            n_features=2**21, preprocessor=None, tokenizer=tokenizer)

