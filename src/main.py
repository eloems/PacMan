import argparse
from game import GUIGame

def main():
    parser = argparse.ArgumentParser(description="Pacman game.")
    group_play = parser.add_mutually_exclusive_group(required=False)
    group_play.add_argument(
        "-p",
        "--player",
        action="store_true",
        help="Player mode: the player controls the game",
    )
    group_play.add_argument(
        "-x",
        "--ai",
        action="store_true",
        help="AI mode: the AI controls the game (requires an 'algorithm' argument)",
    )
    group_algorithm = parser.add_mutually_exclusive_group(required=False)
    group_algorithm.add_argument(
        "-b",
        "--bfs",
        help="Breadth First algorithm: plays a move based of A_star with BFS",
    )
    

    args = parser.parse_args()
    game = GUIGame()   
    game.init_pygame()

    agent = None
    if args.ai :
        agent = "AI"
    #run until the end of the game to get the next ticks
        
    game.next_tick(agent)
    
    #end the screen
    game.cleanup_pygame()
    

if __name__ == "__main__":
    main()
