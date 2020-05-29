from . import nltk_util
from . import document_util
from . import sastrawi_util
from . import gensim_util
import random

def read_document(dir, limit=0):
    listOfDocument = {}

    docInDir = document_util.read_all_document(dir+'/')
    index = 0

    for doc in docInDir:
        docName = dir+'/'+doc
        listOfDocument[doc] = sastrawi_util.remove_stopwords_ina(nltk_util.tokenize_words(document_util.read_document(docName)))

        if limit is not 0:
            index = index+1
            if index == limit:
                break
    
    return listOfDocument

def train_document(listOfDoc, saveModel=False, saveModelDir="", fileName=""):
    corpus = list(gensim_util.read_corpus(listOfDoc))
    model = gensim_util.train_data(corpus, 50, 10)

    if saveModel:
        gensim_util.save_model(model=model, dir=saveModelDir, fileName=fileName)

    return model

def infer_vectors_between_document(model, listOfDoc):
    result = {}

    for docName, docContent in listOfDoc.items():
        result[docName] = gensim_util.infer_vectors(model, docContent)

    return result

def find_similarities_between_document(model, listOfDoc):
    result = {}

    for docName, docContent in listOfDoc.items():
        result[docName] = gensim_util.find_similarities_between_doc_using_tag(model, docName)

    return result

def find_similarities_between_doc_and_dataset(model, inferred_vec_from_listOfDoc):
    result = {}

    for docName, docContent in inferred_vec_from_listOfDoc.items():
        result[docName] = gensim_util.find_similarities(model, docContent)

    return result

# listOfDoc = read_document('dataset example', 10)
# model = train_document(listOfDoc, saveModel=True, saveModelDir="saved_model/", fileName="default.model")
# model = gensim_util.load_model("saved_model/", "default.model")
# infer_vec = infer_vectors_between_document(model, listOfDoc)
# res = find_similarities_between_doc_and_dataset(model, infer_vec)

# for checking with DB, most similar is it self, change the index to get from 2

# model = train_document(listOfDoc)
# res = find_similarities_between_document(model, listOfDoc)

# for docName, listRes in res.items():
#     print(docName+": ")
#     for suspectDoc, acc in listRes:
#         print("suspect doc: "+suspectDoc+" acc: "+str(acc*100)+"; ", end='')
#     print("")