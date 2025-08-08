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

    def search(self, query_vector, top_k=5):
        query = np.array(query_vector)
        scores = []

        for idx, vec in enumerate(self.vectors):
            similarity = np.dot(vec, query) / (np.linalg.norm(vec) * np.linalg.norm(query))

            scores.append((similarity, idx))

        scores.sort(reverse=True)
        top_results = [(self.metadata[idx], self.vectors[idx], score) for score, idx in scores[:top_k]]
        return top_results

