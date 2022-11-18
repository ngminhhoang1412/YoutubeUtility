from random import randint
from underthesea import word_tokenize
class RandomSeq():
    def __init__(self , sequences):
        self.sequences = sequences

    def create_tos(self, sequences):
        return word_tokenize(sequences)
        
    def generate_seq(self, w_token):
        ulist = []
        #randint(1, len(token))
        for i in range(0 , len(w_token)):
            ulist.append(w_token[randint(0, len(w_token) - 1)]) # append random words from words token
        print(ulist)
        x = " ".join(sorted(set(ulist), key=ulist.index))
        return x
