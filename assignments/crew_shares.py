#IC 1st Crew Shares


#calculate how much the amount earned were
amount_earned = int(input("How much money did the crew earn?"))
amount_crew = int(input("How many crew members are there? (not including the captain and first mate): "))

#calculate the value of each share
share_value = int(amount_earned / amount_crew + 10)
captain_share = int(share_value * 7)
first_mate = int(share_value * 3)
crew_value = int(share_value - 500)

#print the total results
print(f"Each member of the crew needs ${crew_value} on top of their $500. The Captain needs ${captain_share} and the First Mate needs ${first_mate}.")