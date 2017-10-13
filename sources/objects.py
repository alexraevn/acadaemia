# python module to define the (inanimate) object class

class gameObject(object):
    def __init__(self, **kwargs):
        # initialize internal status dictionary
        self._status = {}
        for (k,v) in kwargs.items():
            self._status[k] = v
    