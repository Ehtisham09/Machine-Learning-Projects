import os
import codecs
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer,UrduTokenizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sumy.nlp.UrduParser import *
from sumy.evaluation.rouge import *
import numpy as np
import nltk
import os
import statistics as stats
import itertools
evaluated_sentences=list()
reference_sentences=list()
rouge_scores=list()

length=0
total=0

LANGUAGE = "english"
SENTENCES_COUNT = 3

for file in os.listdir('datafiles'):
    with codecs.open('datafiles/' + file, 'r', encoding='utf-8', errors='ignore') as f:
        parser = PlaintextParser.from_string(f.read().replace('\n',' '), UrduTokenizer)
        objectDocModel = parser.document
        print(objectDocModel.sentences)
        print(objectDocModel.paragraphs)
        print(objectDocModel.words)
        print(objectDocModel.headings)
        stemmer = Stemmer(LANGUAGE)
        summarizer = LuhnSummarizer(stemmer)
        summarizer.stop_words = get_stop_words(LANGUAGE)
        summ = summarizer(parser.document, SENTENCES_COUNT)
        with open('dataresults/' + file.split('.')[0] + '.txt', 'w') as fw:
            for sentence in summ:
                print(repr(type(sentence)))
                # print sentence
                evaluated_sentences.append(sentence)
                fw.writelines(str(sentence))
                length += len(str(sentence))
            total += length
            length = 0
        # list of rouge scores (bigrams)
        res = rouge_1(evaluated_sentences, objectDocModel.sentences)
        rouge_scores.append(res)
        evaluated_sentences.clear()

        fw.close()
    f.close()

print('Rouge N score (avg)' + str(stats.mean(rouge_scores)))

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
