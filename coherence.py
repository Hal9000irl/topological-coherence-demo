import numpy as np
from sentence_transformers import SentenceTransformer

class UniversalTopologyDetector:
    def __init__(self, threshold=0.7):
        self.threshold = threshold
        self.model = SentenceTransformer('all-MiniLM-L6-v2')  # Lightweight, fast

    def _cosine_sim(self, a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    def _get_embeddings(self, sentences):
        return self.model.encode(sentences)

    def detect_coherence(self, embeddings):
        n = len(embeddings)
        if n < 4:
            return 0.0, "Too short"

        sim_matrix = np.array([[self._cosine_sim(e1, e2) for e2 in embeddings] for e1 in embeddings])

        # Chiastic pairs (mirrored)
        pairs = [sim_matrix[i, n-1-i] for i in range(n//2)]
        mu_chi = np.mean(pairs) if pairs else 0

        # Linear noise (adjacent)
        adj = [sim_matrix[i, i+1] for i in range(n-1)]
        mu_adj = np.mean(adj) if adj else 0

        # Simple coherence score
        c_score = mu_chi - 0.5 * mu_adj
        return max(0.0, min(1.0, c_score)), f"Chiastic: {mu_chi:.2f} | Adjacent: {mu_adj:.2f}"

    def process_text(self, text):
        sentences = [s.strip() for s in text.split('\n') if s.strip()]
        if len(sentences) < 2:
            return {"coherence": 0.0, "state": "Insufficient data", "details": "Need multiple sentences"}

        embeddings = self._get_embeddings(sentences)
        score, details = self.detect_coherence(embeddings)

        if score > self.threshold:
            state = "Locked Coherence"
        elif score < 0.3:
            state = "Defense / Drift"
        else:
            state = "Searching"

        return {"coherence": score, "state": state, "details": details}