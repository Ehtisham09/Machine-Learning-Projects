import os
import codecs
from gensim.summarization import summarize
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer, UrduTokenizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.UrduParser import *
from sumy.evaluation.rouge import *
import numpy as np
import nltk
import os
import statistics as stats
import itertools



from stemming import *


evaluated_sentences=list()
reference_sentences=list()
rouge_scores=list()
#from pythonrouge.pythonrouge.pythonrouge import *

length=0
total=0



total = 0
for file in os.listdir('datafiles'):
    with codecs.open('datafiles/' + file, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read().replace('\n',' ')

        inp = os.path.join(os.path.abspath('stemming'), os.path.abspath('data'), os.path.abspath('input.txt'))
        out = os.path.join(os.path.abspath('stemming'), os.path.abspath('data'), os.path.abspath('out.txt'))
        stopwordsfile = os.path.join(os.path.abspath('stemming'), os.path.abspath('data'),os.path.abspath('UrduStopWords.txt'))
        # urdustemmer(inp,out,stopwordsfile)
        parser = PlaintextParser.from_string(text, UrduTokenizer)
        refrDocModel = parser.document
        summ = summarize(text, word_count=75)
        for item in summ:
            evaluated_sentences.append(item.encode('utf-8', 'ignore'))
        with open('dataresults/' + file.split('.')[0] + '.txt', 'w') as fw:
            for sentence in evaluated_sentences:
                print(sentence)
                #s = u'\u06D4'
                fw.writelines(str(sentence))
                # length += len(str(sentence))
            total += length
            length = 0
        # list of rouge scores (bigrams)
        with codecs.open('dataresults/' + file, 'r', encoding='utf-8', errors='ignore') as ff:
            parser = PlaintextParser.from_string(ff.read().replace('\n', ' '), UrduTokenizer)
            evalDocModel = parser.document
            res = rouge_1(evalDocModel.sentences, refrDocModel.sentences)
            rouge_scores.append(res)
            evaluated_sentences[:] = []

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