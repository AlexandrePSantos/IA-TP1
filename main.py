from games.connect4.players.greedy import GreedyConnect4Player
from games.connect4.players.minimax import MinimaxConnect4Player
from games.connect4.players.random import RandomConnect4Player
from games.connect4.players.alphabeta import AlphaBetaConnect4Player
from games.connect4.simulator import Connect4Simulator
from games.game_simulator import GameSimulator



def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"----- {desc} -----")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

    print("Results for the game:")
    simulator.print_stats()


def main():
    print("ESTG IA Games Simulator")

    num_iterations = 10

    c4_simulations = [
        # uncomment to play as human
        {
            "name": "Connect4 - Human VS Random",
            "player1": AlphaBetaConnect4Player("AlphaBeta"),
            "player2": RandomConnect4Player("Random")
        },
        {
            "name": "Connect4 - Random VS Random",
            "player1": RandomConnect4Player("Random 1"),
            "player2": RandomConnect4Player("Random 2")
        },
        {
            "name": "Connect4 - Greedy VS Random",
            "player1": GreedyConnect4Player("Greedy"),
            "player2": RandomConnect4Player("Random")
        },
        {
            "name": "Minimax VS Random",
            "player1": MinimaxConnect4Player("Minimax"),
            "player2": RandomConnect4Player("Random")
        },
        {
            "name": "Minimax VS Greedy",
            "player1": MinimaxConnect4Player("Minimax"),
            "player2": GreedyConnect4Player("Greedy")
        }
    ]

    #Punct
    #.......

    for sim in c4_simulations:
        run_simulation(sim["name"], Connect4Simulator(sim["player1"], sim["player2"]), num_iterations)

    #for sim in c4_simulations:
     #   run_simulation(sim["name"], PunctSimulator(sim["player1"], sim["player2"]), num_iterations)


if __name__ == "__main__":
    main()
