import gradio as gr
from simulator import simulate_sequence
from code_generator import generate_assembly
from experiment_notes import EXPERIMENT, VIVA
from ai_tutor import explain_or_debug

def run_simulation(direction, mode, steps, delay):
    result = simulate_sequence(direction, mode, int(steps), int(delay))
    rows = "\n".join(
        f"Step {r['step']}: pattern={r['pattern']}  phases={r['phases']}"
        for r in result["rows"]
    )
    return rows, result["summary"]

def make_code(direction, mode, steps, delay, port, control):
    return generate_assembly(
        direction=direction, mode=mode, steps=int(steps), delay=int(delay),
        data_port=port.strip() or "DATA_PORT", control_port=control.strip() or "CONTROL_PORT"
    )

def tutor(question, code):
    return explain_or_debug(question, code)

def viva_topic(topic):
    if topic == "All":
        return "\n\n".join(f"Q: {q}\nA: {a}" for q, a in VIVA)
    matches = [(q, a) for q, a in VIVA if topic.lower() in (q + " " + a).lower()]
    return "\n\n".join(f"Q: {q}\nA: {a}" for q, a in matches) or "No exact match. Choose All to see the complete viva set."

with gr.Blocks(title="8086 Stepper Motor Agentic AI Lab Tutor", theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        "# 8086 Stepper Motor Lab Tutor\n"
        "### Interfacing a Stepper Motor with 8086 and 8255 PPI\n"
        "Learn the experiment, generate commented assembly templates, simulate phase sequences, "
        "and practice debugging. **Software-only educational simulation; not connected to real hardware.**"
    )
    with gr.Tab("Experiment Guide"):
        gr.Markdown(EXPERIMENT)
    with gr.Tab("Phase Sequence Simulator"):
        gr.Markdown("This models output patterns only. Select the sequence taught in your lab manual.")
        direction = gr.Radio(["Clockwise", "Anticlockwise"], value="Clockwise", label="Direction")
        mode = gr.Radio(["One-phase-on (illustrative)", "Two-phase-on (illustrative)"],
                        value="One-phase-on (illustrative)", label="Drive sequence")
        steps = gr.Slider(4, 32, value=8, step=4, label="Number of steps (multiple of 4)")
        delay = gr.Slider(1, 1000, value=100, step=1, label="Illustrative delay value")
        sim_btn = gr.Button("Simulate sequence", variant="primary")
        sequence_out = gr.Textbox(label="Output sequence", lines=10)
        summary_out = gr.Markdown()
        sim_btn.click(run_simulation, [direction, mode, steps, delay], [sequence_out, summary_out])

    with gr.Tab("8086 Assembly Code Generator"):
        gr.Markdown(
            "**Important:** port addresses are trainer-kit specific. Enter the values from your lab manual. "
            "Generated code is a commented template and must be adapted to your assembler and kit."
        )
        g_direction = gr.Radio(["Clockwise", "Anticlockwise"], value="Clockwise", label="Direction")
        g_mode = gr.Radio(["One-phase-on (illustrative)", "Two-phase-on (illustrative)"],
                          value="One-phase-on (illustrative)", label="Drive sequence")
        g_steps = gr.Slider(4, 32, value=8, step=4, label="Number of steps")
        g_delay = gr.Slider(1, 1000, value=100, step=1, label="Delay loop count (illustrative)")
        data_port = gr.Textbox(value="DATA_PORT", label="8255 output port symbol/address from your kit")
        control_port = gr.Textbox(value="CONTROL_PORT", label="8255 control port symbol/address from your kit")
        gen_btn = gr.Button("Generate assembly template", variant="primary")
        code_out = gr.Code(label="8086 assembly template")
        gen_btn.click(make_code, [g_direction, g_mode, g_steps, g_delay, data_port, control_port], code_out)

    with gr.Tab("AI Tutor & Debug Helper"):
        gr.Markdown(
            "This starter includes a rule-based tutor. To use a real LLM, configure a provider in a later step. "
            "Do not paste private API keys into this page or commit them to GitHub."
        )
        question = gr.Textbox(label="Ask a question or describe the error",
                              placeholder="Example: Why do we use OUT DX, AL?", lines=3)
        student_code = gr.Textbox(label="Optional 8086 assembly code to review", lines=10,
                                  placeholder="Paste your code here...")
        tutor_btn = gr.Button("Explain / check code", variant="primary")
        tutor_out = gr.Markdown()
        tutor_btn.click(tutor, [question, student_code], tutor_out)

    with gr.Tab("Viva Practice"):
        topic = gr.Dropdown(["All", "8086", "8255", "Stepper motor", "Assembly", "Sequence"],
                            value="All", label="Filter")
        viva_btn = gr.Button("Show viva questions")
        viva_out = gr.Markdown()
        viva_btn.click(viva_topic, topic, viva_out)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
