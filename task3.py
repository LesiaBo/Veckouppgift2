goals_Tottenham = input("Hur många mål gjorde Tottenham?: ")
goals_Tottenham = int(goals_Tottenham)

goals_Liverpool = input("Hur många mål gjorde Liverpool?: ")
goals_Liverpool = int(goals_Liverpool)

if goals_Tottenham > goals_Liverpool:
    print(f"Tottenham vann med {goals_Tottenham - goals_Liverpool} mål!")
elif goals_Tottenham < goals_Liverpool:
    print(f"Liverpool vann med {goals_Liverpool - goals_Tottenham}  mål!")
else: # game draw
    print(f"Oavgjord match: {goals_Liverpool}:{goals_Tottenham}!")


# Testfall:
# test 1:
# goals_Tottenham = 7, goals_Liverpool = 5 -> Tottenham vann med 2 mål
# test 2:
# goals_Tottenham = 3, goals_Liverpool = 0 -> Tottenham vann med 3 mål
# test 3:
# goals_Tottenham = 2, goals_Liverpool = 2 -> Oavgjord match: 2:2