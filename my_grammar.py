# -*- coding: utf-8 -*-
"""
@author: Nayden Dochev

This is our grammer. Here we define the rules according to which we extract information.
"""

grammar = """
    # Currently only year and possibly month
    DATE:   <IN>{<NNP>?<CD><\,>?}


    # Organization or place (very buggy at the moment)
    ORG:    <IN>{<DT><PRP|NNP|POS>+(<NN>+)?}
            <JJ>{<PRP|NNP|POS>+}
    PLACE:  <IN|TO>{(<DT|IN>?<NNP|NNPS|NN>)+}


    # Complex adjective
    C_JJ:    {<JJ>((<CC|\,><JJ>)+)?}


    # Complex noun
    C_NN:    {<NN|NNS>((<CC|\,><C_JJ>?<NN|NNS>)+)?}


    # Related item to the person in question
    RELATED_NOUN: {<PRP\$><NN|NNS>+}


    # Matches person (Name or He/She ...)
    PERSON: {<PRP>}
            {<NNP>+}


    # Finally this rule gathers information based on the above rules
    # Every result is called fact
    # Every fact consists of simple sentence e.g. "She was born in 1986."
    # The sentence is chunked so we can later extract who did what and where
    FACT:

            {<DATE>?<PERSON><VBD><VBN>(<IN|TO>?<PLACE|DATE|ORG>+)}
            {<DATE>?<PERSON><VBD><DT>?(<IN|TO>?<PLACE|DATE|ORG>+)}
            {<DATE>?<PERSON><VBD><DT>?<C_JJ>?<C_NN>(<IN|TO>?<PLACE|DATE|ORG>+)}

"""