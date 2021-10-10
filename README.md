# monte carlo tree search templates

A collection of mcts models to test on 2-player games.

## basic

A Monte Carlo Tree Search generally involves 4 phases: selection, expansion, simulation and backpropogation.
    1. Children nodes are selected by highest UCT value until a leaf is reached.
    2. The leaf's child nodes are created and a random child is selected.
    3. The game is played out ('simulation', 'rollout') from this child's game state.
    4. The statistics of the rollout are back.


## tree reuse