
import PlayerClass as PC


def winner_calc(player_list):
    
    print("\nThe results are in!")


    final_scores = []

    for n in range(len(player_list)):
        print(player_list[n].name, f"had {player_list[n].points}.")
        final_scores.append(player_list[n].points)

    win_dex = player_list.index(max(final_scores))

    print("\nThe winner is: ", player_list[win_dex].name, "!!!")
    

