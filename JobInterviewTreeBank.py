import os
from pickle import load

# import nltk
# from nltk.parse.corenlp import DependencyGraph

folder = 'corpus'
path_words = os.path.join(folder, 'words.pkl')
path_sents = os.path.join(folder, 'sents.pkl')
path_tagged_words = os.path.join(folder, 'tagged_words.pkl')
path_tagged_sents = os.path.join(folder, 'tagged_sents.pkl')
path_parsed_sents = os.path.join(folder, 'parsed_sents.pkl')
path_dependency_parsed_sents = os.path.join(folder, 'dependecy_parsed_sents.pkl')
path_raw = os.path.join(folder, 'raw.pkl')
path_raw_text = os.path.join(folder, 'raw_text.pkl')
path_qs_as_text = os.path.join(folder, 'qs_as_text.pkl')

def raw_text():
    '''
    Return str raw corpus text.
    '''
    return load(open(path_raw_text, 'rb'))

def raw_question_answer():
    '''
    Return pandas dataframe of raw corpus text 
    
    each row represents a question and its answer
    '''
    return load(open(path_qs_as_text, 'rb'))

def words():
    '''
    Return list of str 
    
    each element of the list represents a word in the corpus
    '''
    return load(open(path_words, 'rb'))

def sents():
    '''
    Return list of list of str of word. 
    
    each element of the list represents a sentence in the corpus
    '''
    return load(open(path_sents, 'rb'))

def tagged_words():
    '''
    Return list of (str,str) tuple.
    
    each tuple element represents (word, POS tag).
    '''
    return load(open(path_tagged_words, 'rb'))

def tagged_sents():
    '''
    Return list of (list of (str,str))
    
    each element contains a list of tuples containing (word, POS tag).
    '''
    return load(open(path_tagged_sents, 'rb'))

def parsed_sents():
    '''
    Return list of (Tree with str leaves)
    '''
    return load(open(path_parsed_sents, 'rb'))

def raw():
    '''
    Return unprocessed corpus contents
    '''
    return load(open(path_raw, 'rb'))

def dependency_parsed_sents():
    '''
    Return list of dependency parsed text
    '''
    return load(open(path_dependency_parsed_sents, 'rb'))

def visualize_parsed_tree(parsed_sent_tree, print_raw=False):
    if print_raw : 
        print(parsed_sent_tree)
        print(parsed_sent_tree.pformat_latex_qtree())
    parsed_sent_tree.pretty_print() 
