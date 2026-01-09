import streamlit as st
from coherence import UniversalTopologyDetector
import numpy as np

st.set_page_config(page_title="Topological Coherence Verifier", layout="centered")

st.title("🌌 Topological Coherence Verifier")
st.markdown("""
Paste any text — a reasoning trace, market narrative, scientific argument, or story —  
and see how strongly it exhibits **inversion-within-bounds** (chiastic closure + synchronization).
""")

detector = UniversalTopologyDetector()

text = st.text_area("Enter text to analyze", height=200, placeholder="Example: The first shall be last, and the last shall be first...")

if st.button("Compute Coherence"):
    if text.strip():
        with st.spinner("Analyzing..."):
            # Simple tokenization + mock embeddings (real demo uses lightweight model)
            result = detector.process_text(text)
        score = result["coherence"]
        state = result["state"]
        details = result["details"]

        st.metric("Coherence Score (χ)", f"{score:.3f}")

        if score > 0.7:
            st.success(f"🔒 LOCKED — {state}: Strong closure detected")
        elif score < 0.3:
            st.warning(f"🛡️ DEFENSE — {state}: Significant drift")
        else:
            st.info(f"🔍 SEARCHING — {state}: Moderate structure")

        st.caption(details)
    else:
        st.warning("Please enter some text.")

st.markdown("---")
st.caption("By Benjamin De Kraker (@BenjaminDEKR) — exploring coherence as a universal operator.")