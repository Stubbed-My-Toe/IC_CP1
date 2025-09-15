#IC 1st Crew Shares


#calculate how much the amount earned were
amount_earned = float(input("How much money did the crew earn?"))
amount_crew = int(input("How many crew members are there? (not including the captain and first mate): "))

#calculate the value of each share
share_value = float(amount_earned / amount_crew + 10)
captain_share = float(share_value * 7)
round_cap_share = round(captain_share, 2)
first_mate = float(share_value * 3)
round_first_mate = round(first_mate, 2)
crew_value = float(share_value - 500)
round_crew = round(crew_value, 2)

#print the total results
print(f"Each member of the crew needs ${round_crew} on top of their $500. The Captain gets ${round_cap_share} and the First Mate gets ${round_first_mate}.")