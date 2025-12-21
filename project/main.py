import random

yourDic = {"s": 1, "w": -1, "g": 0}
reverseDic = {1: "Snake", -1: "Water", 0: "Gun"}

computer = random.choice(list(reverseDic.keys()))
yourStr = input("Enter your choice (s, w, g): ").lower()

if yourStr not in yourDic:
    print("Invalid choice!")
    exit()

you = yourDic[yourStr]

print(f"You choose: {reverseDic[you]}")
print(f"Computer choose: {reverseDic[computer]}")

if computer == you:
    print("Game Draw!")
elif (computer - you) in (-1, 2):
    print("You Win!")
else:
    print("You Lose!")
