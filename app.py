import gradio as gr
from coherence import UniversalTopologyDetector
import numpy as np

detector = UniversalTopologyDetector()

def analyze_coherence(text):
    if not text.strip():
        return "Please enter some text.", "", ""
    
    # Process the text
    result = detector.process_text(text)
    score = result["coherence"]
    state = result["state"]
    details = result["details"]
    
    # Format score with 3 decimal places
    score_text = f"{score:.3f}"
    
    # Determine status message and color
    if score > 0.7:
        status = f"🔒 LOCKED — {state}: Strong closure detected"
        status_color = "green"
    elif score < 0.3:
        status = f"🛡️ DEFENSE — {state}: Significant drift"
        status_color = "orange"
    else:
        status = f"🔍 SEARCHING — {state}: Moderate structure"
        status_color = "blue"
    
    return score_text, status, details

# Create the Gradio interface
with gr.Blocks(title="Topological Coherence Verifier") as demo:
    gr.Markdown("# 🌌 Topological Coherence Verifier")
    gr.Markdown("""
    Paste any text — a reasoning trace, market narrative, scientific argument, or story —  
    and see how strongly it exhibits **inversion-within-bounds** (chiastic closure + synchronization).
    """)
    
    with gr.Row():
        with gr.Column():
            text_input = gr.Textbox(
                label="Enter text to analyze",
                placeholder="Example: The first shall be last, and the last shall be first...",
                lines=8
            )
            analyze_btn = gr.Button("Compute Coherence", variant="primary")
        
        with gr.Column():
            score_output = gr.Number(label="Coherence Score (χ)", precision=3)
            status_output = gr.Textbox(label="Status", interactive=False)
            details_output = gr.Textbox(label="Details", interactive=False, lines=2)
    
    # Example inputs
    gr.Examples(
        examples=[
            ["The first shall be last, and the last shall be first.\nWhat goes up must come down.\nEvery beginning has an end."],
            ["Random text without structure.\nUnrelated sentences here.\nNo pattern at all."],
            ["Science seeks truth.\nTruth requires evidence.\nEvidence comes from observation.\nObservation guides science."]
        ],
        inputs=text_input
    )
    
    gr.Markdown("---")
    gr.Markdown("*By Benjamin De Kraker (@BenjaminDEKR) — exploring coherence as a universal operator.*")
    
    # Set up the interaction
    analyze_btn.click(
        analyze_coherence,
        inputs=text_input,
        outputs=[score_output, status_output, details_output]
    )

# Launch the app
if __name__ == "__main__":
    demo.launch()