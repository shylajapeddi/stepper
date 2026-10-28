# 8086 Stepper Motor Agentic AI Lab Tutor

An educational starter application for learning the experiment **Interfacing a Stepper Motor with 8086 using 8255 PPI**.

## Current features
- Experiment theory, aim, algorithm and precautions
- Software phase-sequence simulator
- Commented 8086 assembly template generator
- Rule-based learning and basic code-review helper
- Viva question bank

## Important limitations
- This is a software-only educational model; it does not control physical hardware.
- Port addresses and phase sequences are trainer-kit-specific.
- Generated assembly is a template and may need changes for your assembler and trainer kit.
- The tutor performs basic rule-based checks, not a full 8086 assembly or hardware verification.
- No real LLM API is included in this starter version.

## Run locally (Windows)
1. Install Python 3.10 or newer.
2. Open Command Prompt in this folder.
3. Create a virtual environment:

   ```bash
   py -m venv .venv
   .venv\Scripts\activate
   ```

4. Install requirements:

   ```bash
   python -m pip install -r requirements.txt
   ```

5. Start the application:

   ```bash
   python app.py
   ```

6. Open the local URL printed by Gradio, usually `http://127.0.0.1:7860`.

## Upload to GitHub
1. Create a new empty repository named `8086-Stepper-Motor-Agentic-AI`.
2. Upload the files and folders from this project directory.
3. Do not upload `.venv`, API keys, passwords or personal information.

## Next development stages
1. Confirm the lab manual's 8255 port addresses and required phase sequence.
2. Improve code generation to match the specific assembler and lab kit.
3. Add an actual assembler/emulator integration if suitable for the chosen environment.
4. Add an LLM-backed agent workflow using an environment variable for the API key.
5. Add automated tests and improve the simulator.
