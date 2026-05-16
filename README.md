# DeepSpace

DeepSpace is a modular Python architecture for autonomous robotic probes and machine-colony systems.

The project is based on a simple principle:

> Narrow agents observe.  
> The LLM reasons.  
> The verifier protects the machine.  
> The action bus executes only approved actions.

## Core Idea

A real autonomous space machine should not be controlled by one giant AI brain.

Instead, it should be built from many boring specialist systems:

- battery agent
- thermal agent
- terrain agent
- navigation agent
- science agent
- damage agent
- repair agent
- risk agent
- communications agent
- resource agent
- mission agent
- self-preservation agent

The LLM acts as a reasoning layer, not as direct motor control.

## Safety Rule

The LLM may propose actions.

It may not directly execute actions.

Every proposed action must pass through the verifier before reaching the robot.

## Architecture

```text
Robot sensors
    ↓
Specialist Python agents
    ↓
Shared blackboard state
    ↓
Decision engine / LLM layer
    ↓
Verifier
    ↓
Action bus
    ↓
Robot hardware or simulation
```

## First Milestone

A simulated probe that can survive fake scenarios:

- low battery
- wheel damage
- bad terrain
- weak signal
- valuable science target nearby
- unsafe collection attempt

## Run

```bash
python main.py
```

## Test

```bash
pip install -r requirements.txt
pytest
```
