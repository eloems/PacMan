from game import GUIGame

def main():
    game = GUIGame()   
    game.init_pygame()
    
    #run until the end of the game to get the next ticks
    game.next_tick()
    
    #end the screen
    game.end_game()
    game.cleanup_pygame()
    

if __name__ == "__main__":
    main()
