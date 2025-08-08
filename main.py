import numpy as np

class InMemoryVectorDB:
    def __init__(self, dim):
        self.dim = dim
        self.vectors = []
        self.metadata = []

    def add(self, vector, metadata=None):
        if len(vector) != self.dim:
            print("Vector dimension mismatch") 
        self.vectors.append(np.array(vector))
        self.metadata.append(metadata)

