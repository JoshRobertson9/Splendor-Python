# My Modules
import player_class as PC

def winner_calc(player_list):
    
    print("\nThe results are in!")

    final_scores = []

    for player in player_list:
        print(player.name, f"had {player.points}.")
        final_scores.append(player.points)

    #print(final_scores)
    #print(max(final_scores))
    win_dex = (final_scores.index(max(final_scores)))
    #print(win_dex)

    print("\nThe winner is: " + player_list[win_dex].name + "!!!")
    print("___________________________________\n")