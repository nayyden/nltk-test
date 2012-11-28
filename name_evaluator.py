# -*- coding: utf-8 -*-
"""
@author: Nayden Dochev
"""
import operator

class NameEvaluator:
    # lists of words we understand
    # We don't know what to extract when we find this word
    __throw_titles   = ['they', 'it'];
    # If the perseon is called with these prabably she is woman
    __female_titles  = ['She', 'she'];
    # If the perseon is called with these prabably he is man
    __male_titles    = ['He', 'he'];

    def __init__(self):
        # name occurences
        self.__names      = dict()
        # male title occurences
        self.__male_occ   = float(0)
        # female title occurences
        self.__female_occ = float(0)


    # Decide which of the found names to use
    def getName(self):

        # Find the name with max occurences
        name = max(self.__names.iteritems(), key=operator.itemgetter(1))[0]

        # Measure the accuracy (simplest possible)
        accuracy = float(self.__names[name])/sum(self.__names.values())

        return name + " (" + str(accuracy*100) + "%)"


    # Choose the gender simply by checking if we got more he or she
    def getGender(self):

        if(self.__male_occ == self.__female_occ):
            return '50/50 :('

        elif(self.__male_occ > self.__female_occ):
            gender = 'Male'
            accuracy = self.__male_occ / (self.__female_occ + self.__male_occ)
            return gender + " (" + str(accuracy*100.) + "%)"

        elif(self.__male_occ < self.__female_occ):
            gender = 'Fmale'
            accuracy = self.__female_occ / (self.__female_occ + self.__male_occ)
            return gender + " (" + str(accuracy*100.) + "%)"


    # On adding the name decide
    def addName(self, name):
        if name not in self.__throw_titles:
            if name in self.__male_titles:
                self.__male_occ += 1
            elif name in self.__female_titles:
                self.__female_occ += 1
            else:
                if name in self.__names:
                    self.__names[name] += 1
                else:
                    proceed = 1
                    for n in self.__names:
                        if name in n:
                            self.__names[n] += 1
                            proceed = 0
                    if name != '1234567890' and proceed:
                        self.__names[name] = int(1)

