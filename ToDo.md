Development plan (phases) — concise version

1) Connect‑4 environment
   - [x] <del>implement CLI logic: valid moves, terminal state, winner detection</del>
   - [x] <del>unit tests for game logic</del>

1.5) Notebook implementation
   - [x] <del>changhe the hole project environment to a notebook. This will results in a better environment for the project</del>

2) Baseline agents
   - [x] <del>implement random and greedy; optional: depth‑limited minimax</del>
   - [x] <del>use as reference for fitness design and debugging</del>

3) Neuroevolution (NEAT)
   - [] define inputs/outputs (board encoding, turn), topology/genome limits
   - [] choose primary fitness (e.g. win rate vs baselines) and penalties

4) Training & experiments pipeline
   - [] scripts to run repeated runs with seed, config and checkpoints
   - [] minimal hyperparameter sweep schema (pop size, mutation rate)

5) Logging & reproducibility
   - [] save config, seed, checkpoints; generation logs (csv/json)
   - [] save replays or logs of best games

6) Evaluation & analysis
   - [] compare best individuals vs baselines: win/draw/loss, variance
   - [] generate essential plots and a concise results report

7) Minimum deliverables
   - [] tested game code, reproducible training scripts, report with results