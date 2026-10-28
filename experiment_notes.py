EXPERIMENT = r"""
## Experiment: Interfacing a Stepper Motor with 8086 Using 8255 PPI

### Aim
To study how an 8086 microprocessor can control a stepper motor through the 8255 Programmable Peripheral Interface (PPI).

### Theory
A stepper motor converts a sequence of electrical phase signals into discrete angular movements. The 8086 executes an assembly program. The 8255 provides programmable I/O ports, and a suitable driver supplies the current required by the motor windings.

### Basic operation
1. Configure the 8255 control register for the required port directions and mode.
2. Write a phase pattern to the selected output port.
3. Wait for a delay.
4. Write the next pattern in the required order.
5. Repeat for the required number of steps.

### Important notes
- I/O port addresses differ between trainer kits.
- Phase patterns depend on the motor, wiring, driver and lab manual.
- The 8255 must not directly power a motor; use a suitable driver circuit.
- The software simulator in this project models patterns only. It does not model real torque, speed, inertia or electrical current.
- Confirm all settings with the instructor/lab manual before connecting hardware.

### Algorithm
1. Start.
2. Initialize data segment if required by the assembler/program format.
3. Configure the 8255.
4. Load the selected phase pattern.
5. Output the pattern.
6. Execute a delay.
7. Select the next pattern.
8. Repeat until the requested step count is reached.
9. Stop.

### Result
The software model displays the selected sequence of phase patterns. Actual hardware results must be verified on the college trainer kit.
"""

VIVA = [
    ("What is a stepper motor?", "A motor that rotates in discrete steps in response to electrical pulses."),
    ("What is the function of 8086?", "It executes instructions and controls the sequence of output data."),
    ("What is 8255 PPI?", "A programmable peripheral interface providing digital I/O ports."),
    ("Why is a driver used?", "The driver supplies the current needed by motor windings; the 8255 cannot directly power the motor."),
    ("How is direction changed?", "By reversing the order of the phase sequence."),
    ("How is speed controlled in a basic program?", "By changing the delay between successive phase patterns."),
    ("What does OUT do?", "It writes data from AL/AX to an I/O port specified directly or through DX, depending on the instruction form."),
    ("What is a control word?", "A byte written to the 8255 control register to configure its mode and port directions."),
    ("What is the purpose of a delay routine?", "It provides time between phase changes so the motor can respond."),
    ("Why must port addresses be checked?", "The addresses depend on the trainer kit's hardware decoding."),
    ("Can an 8255 drive a motor directly?", "No. A suitable motor driver stage is required."),
    ("What does a software simulation verify?", "It can check the intended sequence and program logic, but not real mechanical performance."),
]
