import nltk
import os

def bleu (path2model, path2gold):

    files = os.listdir(path2model)

    bleu_scores = []
    for i in files:
        reference = []
        gold_summ = os.listdir(path2gold + '/' + i.split('.txt')[0])
        with open(path2model + '/' + i, 'r') as fmodel:
            textmodel = fmodel.read()
            fmodel.close()
        for j in gold_summ:
            with open(path2gold + '/' + i.split('.txt')[0] + '/' + j, 'r') as fgold:
                textgold = fgold.read()
                fmodel.close()
        reference.append(textgold)

        bleu_scores.append(nltk.translate.bleu_score.sentence_bleu(reference, textmodel, weights=[0.4, 0.3, 0.2]))
    return bleu_scores