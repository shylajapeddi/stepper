def generate_assembly(direction, mode, steps, delay, data_port, control_port):
    one_phase = [0x01, 0x02, 0x04, 0x08]
    two_phase = [0x03, 0x06, 0x0C, 0x09]
    patterns = one_phase if mode.startswith("One-phase") else two_phase
    if direction == "Anticlockwise":
        patterns = list(reversed(patterns))

    patterns_text = ", ".join(f"{p:02X}H" for p in patterns)
    return f"""; Educational 8086 + 8255 stepper-motor template
; Direction: {direction}
; Sequence type: {mode}
; Requested steps: {steps}
; Delay count: {delay} (illustrative only)
;
; BEFORE RUNNING:
; 1. Replace {data_port} and {control_port} with the I/O addresses from your kit manual.
; 2. Verify the motor driver, winding order and active logic.
; 3. This template uses MASM/TASM-style syntax and may need adaptation.
; 4. 8255 control word 80H configures Mode 0 with all ports as outputs;
;    use it only if that matches your lab's wiring and configuration.
;
; Illustrative phase patterns: {patterns_text}
; The lower four output bits are treated as phases A-D.
; This code writes each phase pattern once per cycle; adapt for your lab requirements.

.MODEL SMALL
.STACK 100H
.DATA
    phase_table DB {patterns_text}
    step_count  DW {steps}
    delay_count DW {delay}

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX

    ; Configure 8255 (verify control word and address for your kit)
    MOV DX, {control_port}
    MOV AL, 80H
    OUT DX, AL

    MOV CX, step_count
    XOR SI, SI

NEXT_STEP:
    ; Select pattern from phase_table; SI cycles through four entries
    MOV BX, SI
    MOV AL, phase_table[BX]
    MOV DX, {data_port}
    OUT DX, AL

    CALL DELAY

    INC SI
    CMP SI, 4
    JB INDEX_OK
    XOR SI, SI
INDEX_OK:
    LOOP NEXT_STEP

    MOV AX, 4C00H
    INT 21H
MAIN ENDP

DELAY PROC
    PUSH CX
    MOV CX, delay_count
DELAY_LOOP:
    LOOP DELAY_LOOP
    POP CX
    RET
DELAY ENDP

END MAIN
"""
