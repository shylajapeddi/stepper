import re

def explain_or_debug(question, code):
    q = (question or "").strip()
    source = (code or "").strip()
    parts = []

    if q:
        low = q.lower()
        if "out" in low or "dx, al" in low:
            parts.append("**Explanation:** `OUT DX, AL` writes the byte in register `AL` to the I/O port whose address is in `DX`. It is commonly used to send a control word or output pattern to the 8255.")
        elif "8255" in low or "ppi" in low:
            parts.append("**Explanation:** The 8255 PPI provides programmable ports. The 8086 writes a control word to configure the ports, then sends output patterns to the selected port. Port addresses depend on the trainer kit.")
        elif "direction" in low or "clockwise" in low or "anticlockwise" in low:
            parts.append("**Explanation:** Direction is controlled by the order of phase patterns. Reversing the sequence reverses the intended direction, provided the phase wiring and driver mapping match.")
        elif "delay" in low or "speed" in low:
            parts.append("**Explanation:** A delay between phase changes gives the motor time to respond. A longer delay usually reduces stepping rate; exact speed depends on the code, clock, motor and load.")
        elif "reg" in low:
            parts.append("**Explanation:** In 8086 assembly, `REG` is not a universal instruction by itself. Register names include AX, BX, CX, DX, SI, DI, BP, SP and their supported byte halves such as AL and AH.")
        else:
            parts.append("**Tutor guidance:** Break the experiment into: configure 8255 → output a phase pattern → delay → output the next pattern → repeat. Confirm the port addresses and sequence from your lab manual.")

    if source:
        checks = []
        if source.count("PROC") != source.count("ENDP"):
            checks.append("The number of `PROC` and `ENDP` directives differs; check procedure boundaries.")
        if re.search(r"\bOUT\s+[A-Z_]+\s*,", source, re.I):
            checks.append("An `OUT` instruction may need an accepted port operand form. For variable port addresses, a common form is `OUT DX, AL` or `OUT DX, AX`; confirm assembler syntax.")
        if "CONTROL_PORT" in source or "DATA_PORT" in source:
            checks.append("Port placeholders remain. Replace them with the actual I/O addresses from your trainer-kit manual before assembling.")
        if "80H" in source and "8255" in source:
            checks.append("Confirm that control word `80H` matches your required 8255 mode and port directions.")
        if not re.search(r"\b(OUT|MOV|JMP|LOOP|CALL)\b", source, re.I):
            checks.append("No common motor-control instructions were detected. Check that you pasted 8086 assembly code.")
        if not checks:
            checks.append("Basic text checks found no obvious issue, but this is not a real assembler run. Verify labels, address syntax, and the phase sequence with your lab setup.")
        parts.append("**Code review (basic checks, not a full assembler):**\n" + "\n".join(f"- {c}" for c in checks))

    if not parts:
        parts.append("Enter a question or paste an assembly program to get learning guidance and basic checks.")
    return "\n\n".join(parts)
