"""
The "STS for Keras" toolkit.  Contains various Keras blocks that make
putting together and comfortably running neural STS models a breeze.
"""


def graph_input(si0, si1, y, f0=None, f1=None):
    """ Produce Keras task specification from vocab-vectorized sentences. """
    gr = {'si0': si0, 'si1': si1, 'score': y}
    if f0 is not None:
        gr['f0'] = f0
        gr['f1'] = f1
    return gr