# Connect4-Neuroevo
This repository hosts a project for a global and multi‑objective optimization project that applies neuroevolution to the game of Connect‑4. It includes a Connect‑4 environment, deterministic win detection, baseline agents (random and greedy), and a NEAT‑based training pipeline with experiment management, logging and checkpointing. The objective is to explore neuroevolution strategies, study trade‑offs across multiple objectives (e.g. win rate, robustness, complexity), and compare evolved agents against classical baselines.

## Quick highlights:
- Lightweight, reproducible experiments (config, seeds, checkpoints)
- Fast game logic optimized for cache locality
- Baselines for evaluation and fitness design
- Scripts to run parameter sweeps and collect metrics

## Usage (quick start):
```bash
pip install -r requirements.txt
python main.py
```

## Development
Use task list in `ToDo.md` to track progress.
