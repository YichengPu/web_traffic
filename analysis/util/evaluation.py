import numpy as np
def SMAPE(truth,pred):

    """return SMAPE score
    Args:
    truth(ndarray): truth
    pred(ndarray): prediciton
    Return:
    recall score(float)
    """
    dom=(np.abs(truth)+np.abs(pred))
    if dom>0:
        return np.mean(np.abs(truth-pred)*2/)
    else:
        return 0