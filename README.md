# monte carlo tree search templates

A collection of mcts models to test on 2-player games.

## usage

The specifc game needs to be filled in in the ``game`` folder. A move is obtained through the ``search`` method of the MCTS models.

## basic

A Monte Carlo Tree Search generally involves 4 phases: selection, expansion, simulation and backpropogation.
    1. Children nodes are selected by highest UCT value until a leaf is reached.
    2. The leaf's child nodes are created and a random child is selected.
    3. The game is played out ('simulation', 'rollout') from this child's game state.
    4. The statistics of the rollout are backpropagated throughout all nodes taken during selection and expansion.

The solution selected by MCTS converges to the optimal solution of a minimax algorithm as the number of iterations goes to infinity, but in practice the process is limited by a certain number of iterations or a time limit.

## improvements

### tree reuse

The game tree is preserved after every iteration of MCTS. For general video game playing this has previously seen slight improvements (Soemers et al. 2016). Statistics from previous searches are preserved at every node, but it is also possible to weight them to not have too much influence on the current iteration.

### different rollouts

The simplest way of doing the rollout is to randomly play moves until a result is reached, but using domain specific knowledge the simulation can be modified to play out more realistic games. More generally, another improvement that could apply to all games is to play a winning move if it is available.

### progressive bias

Browne et al. suggest adding an extra term that incorporates domain knowledge to the UCT value of a node (2012). However, this requires some utility function that evaluates a game state.

### progressive history

Instead of using domain knowledge, multiplayer MCTS has seen some success with progressive history (Nijssen and Winands 2010). It functions similar to RAVE and assumes the value of one move is not influenced by other moves played in the game. Progressive history keeps track of how many times a certain move was played (regardless of state) and the times it lead to a win/loss. The result is taken into account in the selection phase.
