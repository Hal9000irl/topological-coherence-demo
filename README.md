# Topological Coherence Verifier

Live demo: [https://huggingface.co/spaces/yourusername/coherence-demo](https://huggingface.co/spaces/yourusername/coherence-demo)

An interactive tool to test **topological coherence** — the degree to which text exhibits inversion-within-bounds symmetry (chiastic closure + structural synchronization).

Based on the framework developed by Benjamin De Kraker (@BenjaminDEKR).

## How to Use
1. Paste any text (reasoning chain, narrative, scientific argument).
2. Click "Compute Coherence".
3. View the score (0–1) and interpretation.

Higher scores indicate stronger self-consistent closure — a signal of integrity across domains from AI outputs to physical theories.

## Local Run
```bash
git clone https://github.com/yourusername/topological-coherence-demo
cd topological-coherence-demo
pip install -r requirements.txt
streamlit run app.py