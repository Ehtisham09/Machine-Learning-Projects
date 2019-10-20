import os
import codecs
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer, UrduTokenizer
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

LANGUAGE = "english"
SENTENCES_COUNT = 3
corpus=list()
length = 0
total = 0
for file in os.listdir('datafiles'):
    with codecs.open('datafiles/' + file, 'r', encoding='utf-8', errors='ignore') as f:
        text=f.read().replace('\n', ' ')
        corpus.append(customtokenize(text))
        parser = PlaintextParser.from_string(text, UrduTokenizer)
        objectDocModel = parser.document
        print(objectDocModel.sentences)
        print(objectDocModel.paragraphs)
        print(objectDocModel.words)
        print(objectDocModel.headings)
        stemmer = Stemmer(LANGUAGE)
        summarizer = LexRankSummarizer(stemmer)
        summarizer.stop_words = get_stop_words(LANGUAGE)
        summ = summarizer(parser.document, SENTENCES_COUNT)
        with open('dataresults/' + file.split('.')[0] + '.txt', 'w') as fw:
            for sentence in summ:
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


print('Rouge N score (avg)'+str(stats.mean(rouge_scores)))
#print('Rouge N score'+str(rouge_1(evaluated_sentences,reference_sentences)))
# print('Rouge N score'+str(rouge_l_sentence_level(evaluated_sentences,reference_sentences)))
# print('Rouge N score'+str(rouge_l_summary_level(evaluated_sentences,reference_sentences)))

# db=itertools.chain(corpus)
# st=''.join(db)
# myDict=nltk.FreqDist(st)
# for word, frequency in myDict.most_common(500):
#     with codecs.open('stopwords.txt', 'w', encoding='utf-8', errors='ignore') as f:
#         f.writelines(word+ "\n")



f.close()
#mostcommon=myDict.most_common(500).keys()



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






def tokenizaion(text,algo=1):
    if algo==1:
        tokens=customtokenize(text)
        return tokens
    else:
        return tokens

bleu_scores = bleu('dataresults','datagold')
print('BLUE_METRIC Scores='+str(np.mean(bleu_scores)))
print('BLUE_METRIC S.Deviation='+str(np.std(bleu_scores)))
