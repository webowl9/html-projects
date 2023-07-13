# Author: Ruben Martinez
# GitHub username: webowl9
# Date: 07/13/2023
# Description: A program that prompts user to guess and input a number in the system. Then the player will have
# guess what the number is by inputting it in the program. If the number is too high or too low, than the
# will display if the number is too high or too low. Once the player has guessed the number, the program will
# let the player know how many tries it took to get the right number.

print("Enter a number for the player to guess.")
user_num = int(input())
print("Guess the User's number")
player_num = int(input())
if user_num == player_num:
    print("Correct! you've guessed in 1 try.")
count = 1
while user_num != player_num:
    count += 1
    if player_num > user_num:
        print("The number is too high. Please try again.")
    if player_num < user_num:
        print("The number is too low please try again.")
    player_num = int(input())
    if user_num == player_num:
        print("Correct! You've guessed it in", count, "tries.")
