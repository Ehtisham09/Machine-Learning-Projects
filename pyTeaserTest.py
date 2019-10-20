from pyteaser import SummarizeUrl
from pyteaser import *
from pprint import pprint
import re
import codecs
import os
import numpy as np
import nltk
import os
import itertools
from sumy.parsers.plaintext import PlaintextParser
from sumy.evaluation.rouge import *
from sumy.nlp.tokenizers import Tokenizer, UrduTokenizer
evaluated_sentences=list()
reference_sentences=list()
rouge_scores=list()
#from pythonrouge.pythonrouge.pythonrouge import *

length=0
total=0

# urls = (u'http://www.huffingtonpost.com/2013/11/22/twitter-forward-secrecy_n_4326599.html',
#         u'http://www.bbc.co.uk/news/world-europe-30035666',
#         u'http://www.bbc.co.uk/news/magazine-29631332')
#
# for url in urls:
#     summaries = SummarizeUrl(url)
#     pprint(summaries)


for file in os.listdir('datafiles'):
    with codecs.open('datafiles/' + file, 'r', encoding='utf-8', errors='ignore') as f:
        text=f.read()
        parser = PlaintextParser.from_string(text.replace('\n', ' '), UrduTokenizer)
        refrDocModel = parser.document
        for item in refrDocModel.sentences:
            reference_sentences.append(item)
            #print(item.encode('utf-8','ignore'))
        title=""
        #text=u'\u06D4'.join(str(bit) for bit in reference_sentences)
        dataresult=(Summarize(title,text))
        for item in dataresult:
            evaluated_sentences.append(item.encode('utf-8','ignore'))
        with open('dataresults/' + file.split('.')[0] + '.txt', 'w') as fw:
            for sentence in evaluated_sentences:
                print(sentence.decode())
                s=u'\u06D4'
                vc=s.encode('utf-8','ignore').decode()
                print(vc)
                fw.writelines(str(sentence.decode())+vc)
                #length += len(str(sentence))
            total += length
            length = 0
        # list of rouge scores (bigrams)

        with codecs.open('dataresults/' + file, 'r', encoding='utf-8', errors='ignore') as ff:
            parser = PlaintextParser.from_string(ff.read().replace('\n', ' '), UrduTokenizer)
            evalDocModel = parser.document
            res = rouge_1(evalDocModel.sentences, refrDocModel.sentences)
            rouge_scores.append(res)
            evaluated_sentences[:]=[]

        fw.close()
        ff.close()
    f.close()

print('Rouge N score (avg)' + str(np.mean(rouge_scores)))

def bleu (path2model, path2gold):

    files = os.listdir(path2model)

    bleu_scores = []
    for i in files:
        reference = []
        gold_summ = os.listdir(path2gold)
        with open(path2model + '/' + i, 'r') as fmodel:
            textmodel = fmodel.read()
            fmodel.close()
        for j in gold_summ:
            with open(path2gold + '/' + j, 'r') as fgold:
                textgold = fgold.read()
                fmodel.close()
        reference.append(textgold)

        bleu_scores.append(nltk.translate.bleu_score.sentence_bleu(reference, textmodel, weights=[0.4, 0.3, 0.2]))
    return bleu_scores



bleu_scores = bleu('dataresults','datagold')
print('BLUE_METRIC Scores='+str(np.mean(bleu_scores)))
print('BLUE_METRIC S.Deviation='+str(np.std(bleu_scores)))
print('****************')
#
# summary = [[" Tokyo is the one of the biggest city in the world."]]
# reference = [[["The capital of Japan, Tokyo, is the center of Japanese economy."]]]
# rouge = Pythonrouge(summary_file_exist=False,
#                     summary=summary, reference=reference,
#                     n_gram=2, ROUGE_SU4=True, ROUGE_L=False,
#                     recall_only=True, stemming=True, stopwords=True,
#                     word_level=True, length_limit=True, length=50,
#                     use_cf=False, cf=95, scoring_formula='average',
#                     resampling=True, samples=1000, favor=True, p=0.5)
# score = rouge.calc_score()
# print(score)
