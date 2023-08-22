import numpy as np

def preprocessing(data):
    """
    inputs : data 
    return preprocessed data 

    1 means eye blink
    """
    queue = []
    if np.mean(data[0]) > 4400 and 1 not in queue:
        queue.append(1)
        if queue.length() > 3:
            queue.pop()
        return 1
    return 0
    