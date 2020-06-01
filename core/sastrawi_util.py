from . import document_util
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

def remove_stopwords_ina(inputWords):
    stopWordFactory = StopWordRemoverFactory()
    stopWord = stopWordFactory.create_stop_word_remover()
    stopWordResult = []

    for word in inputWords:
        newWord = document_util.remove_unused_symbols(stopWord.remove(word))
        
        if newWord != "":
            stopWordResult.append(newWord)

    return stopWordResult