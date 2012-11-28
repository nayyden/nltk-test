# -*- coding: utf-8 -*-
"""
@author: Nayden Dochev
"""

import nltk

import my_corpus
import my_grammar
import my_helpers

from name_evaluator import NameEvaluator

# Compile the grammer to a nltk parser
cp = nltk.RegexpParser(my_grammar.grammar)


for text in my_corpus.texts:
    
    tagged_sentences = list()
    
    # Convert free form text to list of sentences
    for sentence in  nltk.sent_tokenize(text):
        words = list()
        # Turn every sentence into list of words
        for word in nltk.word_tokenize(sentence):
            words.append(word)
        
        # Add tags to every word in sentence using nltk's built in function
        sent = nltk.pos_tag(words)
        
        # Parse the sentence using our grammer
        new_sent = cp.parse(sent)
        
        tagged_sentences.append(new_sent)

    name_ev = NameEvaluator()

    # Walk the sentences and extract the facts
    # Then use the name evaluator to analyse them
    for sentence in tagged_sentences:
        for fact in sentence.subtrees(filter=lambda t: t.node == 'FACT'):

            # for every person in the fact
            for p in fact.subtrees(filter=lambda t: t.node == 'PERSON'):

                # Merge the list of strings into name
                p_name = my_helpers.list_to_string(p)
                name_ev.addName(p_name)

    print name_ev.getName()
    print name_ev.getGender()
    print "\n"