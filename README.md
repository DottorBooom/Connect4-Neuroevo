# 🎓 Connect4-Neuroevo

This project explores **neuroevolution** applied to Connect 4 using the **NEAT algorithm** (NeuroEvolution of Augmenting Topologies). The goal is to evolve neural networks capable of playing Connect 4 against various opponents, from random agents to strategic greedy players.

## 📋 Project Overview

The notebook contains a complete pipeline for:

- **Connect 4 Environment**: Custom implementation with optimized win detection
- **Baseline Agents**: Random and greedy (heuristic-based) opponents
- **NEAT Integration**: Neural network evolution with multiple encoding strategies
- **Fitness Functions**: Various approaches including symmetric training, curriculum learning, and co-evolution
- **Analysis Tools**: Fitness plotting, network visualization, and agent comparison matrices

### 🧪 Key Experiments

| Experiment | Description |
|------------|-------------|
| NEAT vs Random | Basic training against random moves |
| NEAT vs Greedy | Training against heuristic opponent |
| Symmetric Training | Balanced first/second player performance |
| Curriculum Learning | Gradual difficulty increase |
| Co-evolution | Training against population peers |
| Encoding Comparison | Simple vs Double vs Pattern-based |

### 🔍 Main Findings

- NEAT successfully evolves agents for simple scenarios (beating random opponents)
- Feed-forward networks struggle with strategic depth required against greedy agents
- Networks fail to develop defensive/reactive play capabilities
- Larger populations with fewer generations outperform the inverse configuration

## 📁 Repository Structure

├── connect4-neuroevo.ipynb - Main notebook with all experiments

├── neat_config.txt - NEAT configuration parameters

├── best_genome/ - Saved evolved genomes

├── requirements.txt - Python dependencies

└── README.md - Project overview and instructions

## 🚀 Quick Start

### 📦 Installation

```bash
pip install -r requirements.txt
```

### ▶️ Running the Notebook

The notebook uses a control variable `execute_all_cells` at the top:

```python
execute_all_cells = False  # Default
```

#### Two Modes of Operation

| Mode | `execute_all_cells` | What Happens |
|------|---------------------|--------------|
| **Review Mode** | `False` | Loads pre-saved genomes from `best_genome/`, runs demo games and network visualizations. Fast execution (~minutes) |
| **Full Training Mode** | `True` | Re-runs all NEAT evolution experiments from scratch. Very slow execution (~hours) |

**💡 Recommendation**: Keep `execute_all_cells = False` unless you want to reproduce the full evolutionary training. All analysis cells (game demos, network plots, comparison matrices) will still execute using the saved best genomes.

### 🧠 Pre-trained Genomes

The `best_genome/` folder contains evolved networks from various experiments:

- `random_agent_encode0.pkl` - Trained vs random agent
- `greedy_agent_encode0.pkl` - Trained vs greedy agent  
- `tune_encode0_*.pkl` - Various fitness function experiments
- `specialist_first.pkl` / `specialist_second.pkl` - Position-specialized agents
- `compare_encode*.pkl` - Different encoding methods

## 📚 Dependencies

- `neat-python` - NEAT implementation
- `numpy` - Numerical operations
- `matplotlib` - Plotting
- `networkx` - Network visualization
- `pandas` / `seaborn` - Comparison matrices

## 🎓 Acknowledgments

This project was developed as part of a global and multi-objective optimization course, exploring the capabilities and limitations of neuroevolution for game-playing AI.
