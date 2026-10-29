loss_count = 0
win_count = 0
total_of_time_played = 0

for i in range(5):
    game = input("Type the match results, W for win and L for loss: ").upper().strip()
    if game == "W":
        win_count += 1
    if game == "L":
        loss_count += 1
    time = int(input("Type the time played: "))
    total_of_time_played += time

win_rate = (win_count / 5) * 100

print(f"{"=" * 15} {"MATCH SUMMARY":^15} {"=" * 15}")
print(f"You won a total of {win_count} matches, and lost {loss_count} matches. the  winn rate was {win_rate:.1f}%, the total time played was {total_of_time_played} min and average time of every round were {total_of_time_played / 5:.1f} min")

