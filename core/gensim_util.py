import gensim
import collections

def read_corpus(corpus, tokens_only=False):
    for name, line in corpus.items():
        if tokens_only:
            yield line
        else:
            # For training data, add tags
            yield gensim.models.doc2vec.TaggedDocument(line, [name])

def train_data(dataset, vector_size, epochs, alpha=0.25):
    model = gensim.models.doc2vec.Doc2Vec(
        vector_size=vector_size, 
        alpha=alpha, 
        min_alpha=0.025, 
        epochs=epochs,
        min_count=1,
        dm=1)
    model.build_vocab(dataset)
    model.train(dataset, total_examples=model.corpus_count, epochs=model.epochs)
    return model

def save_model(model, dir, fileName):
    model.save(str(dir)+str(fileName))

def load_model(dir, fileName):
    return gensim.models.doc2vec.Doc2Vec.load(str(dir)+str(fileName))

def delete_temp_training_data(model):
    model.delete_temporary_training_data(keep_doctags_vectors=True, keep_inference=True)

def infer_vectors(model, listOfWord):
    return model.infer_vector(listOfWord)

def find_similarities_between_doc_using_tag(model, tag):
    return model.docvecs.most_similar(str(tag), topn=3)

def find_similarities(model, inferred_vec_input_document):
    sims = model.docvecs.most_similar([inferred_vec_input_document], topn=3)

    return sims