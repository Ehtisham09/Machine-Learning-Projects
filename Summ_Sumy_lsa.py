import codecs
import os
import statistics as stats

import nltk
import numpy as np
from sumy.evaluation.rouge import *
from sumy.nlp.UrduParser import *
from sumy.nlp.stemmers import Stemmer
from sumy.nlp.tokenizers import UrduTokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.utils import get_stop_words

LANGUAGE = "english"
SENTENCES_COUNT = 3
evaluated_sentences=list()
reference_sentences=list()
rouge_scores=list()
for file in os.listdir('datafiles'):
    with codecs.open('datafiles/' + file, 'r', encoding='utf-8', errors='ignore') as f:
        parser = PlaintextParser.from_string(f.read().replace('\n',' '), UrduTokenizer)
        objectDocModel=parser.document
        print(objectDocModel.sentences)
        print(objectDocModel.paragraphs)
        print(objectDocModel.words)
        print(objectDocModel.headings)

        stemmer = Stemmer(LANGUAGE)
        summarizer = Summarizer(stemmer)
        summarizer.stop_words = get_stop_words("Urdu")
        summ = summarizer(parser.document, SENTENCES_COUNT)
        with open('dataresults/' + file.split('.')[0] + '.txt', 'w') as fw:
            for sentence in summ:
                #print sentence
                evaluated_sentences.append(sentence)
                fw.writelines(str(sentence))
        #list of rouge scores (bigrams)
        res=rouge_1(evaluated_sentences, objectDocModel.sentences)
        rouge_scores.append(res)
        evaluated_sentences.clear()

        fw.close()
    f.close()


# Evaluation scores
with codecs.open('datafiles/' + 'CurrentAffairs1.txt', 'r', encoding='utf-8', errors='ignore') as f:
    text=f.read()
    ref_sent=split_text(text)
    for sen in ref_sent:
        reference_sentences.append(sen)

    f.close()
#
# rr=itertools.cycle(objectDocModel.sentences)
# for t in rr:
#     print(t)
#rouge score
print('Rouge N score (avg)'+str(stats.mean(rouge_scores)))
#print('Rouge N score'+str(rouge_1(evaluated_sentences,reference_sentences)))
# print('Rouge N score'+str(rouge_l_sentence_level(evaluated_sentences,reference_sentences)))
# print('Rouge N score'+str(rouge_l_summary_level(evaluated_sentences,reference_sentences)))







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
