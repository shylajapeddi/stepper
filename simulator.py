ONE_PHASE = [0b0001, 0b0010, 0b0100, 0b1000]
TWO_PHASE = [0b0011, 0b0110, 0b1100, 0b1001]

def bits4(value):
    return format(value, "04b")

def simulate_sequence(direction, mode, steps, delay):
    patterns = ONE_PHASE if mode.startswith("One-phase") else TWO_PHASE
    if direction == "Anticlockwise":
        patterns = list(reversed(patterns))
    rows = []
    for i in range(steps):
        pattern = patterns[i % len(patterns)]
        b = bits4(pattern)
        rows.append({
            "step": i + 1,
            "pattern": f"{pattern:02X}H (binary {b})",
            "phases": f"A={b[3]} B={b[2]} C={b[1]} D={b[0]}"
        })
    return {
        "rows": rows,
        "summary": (
            f"**Direction:** {direction}  \n"
            f"**Sequence:** {mode}  \n"
            f"**Requested steps:** {steps}  \n"
            f"**Illustrative delay setting:** {delay} (not calibrated to milliseconds or RPM)."
        )
    }
