#IC 1st period CP2 movie recommender

#A main function that runs the program and shows a persistent menu.
#A parser function to load and normalize the provided movie list (CSV) into structured records.
#Separate filter functions for: genre, director, actor(s), and length.
#A function that combines selected filters (AND logic by default) and returns matching movies.
#A function to pretty-print results and a function to print the full movie list.
#Input validation and helpful error messages; handle missing or malformed movie records gracefully.
#Allow interactive entry of filter values and length ranges (min/max or comparator).
#HINTS:
#Normalize text to lower-case and trim whitespace for case-insensitive matching.
#Store multi-valued fields (genres, actors) as lists and match if any element contains the query term.
#Implement length filtering with min and/or max values (support <, > comparators optionally).
#If zero matches, suggest relaxing or removing one filter.
#Provide a small sample movies file in the repo and include unit tests for filter logic.
#FILTER RULES CLARIFICATIONS:
#Matching is case-insensitive.
#For genres and actors, match if any element contains the query substring (trim whitespace).
#Length filter accepts min and/or max (integers). If only one provided, use it as bound.
#Combine multiple filters using logical AND (movie must satisfy every selected filter).
#If a movie is missing a field, it does not match a filter for that field.

import csv
#welcome to the program. This is so you can pick movies. perchance.
#while true
    #def func main_menu()
        #Welcome to the movie recommender main menu. What would you like to do?
        #menu_action=(
        #1. Search / Get recommendations
        #2. Print full movie list
        #3. Exit)
        #If menu_action is 1
            #Search / movie recommendations
            #display What do you want to search for? Choose filters to apply (enter numbers separated by commas, e.g., 1,3):
            #chosen_filters=(
            #1. Genre
            #2. Director
            #3. Actors
            #4. Length (min/max))
        #elif 2
            #print movies_list.csv
        #elif 3
            #exit()
        #else:
            #input invalid. please try again
            #main_menu
    #return chosen_filters
    #def use_filters
    #match chosen_filters
        #case genre if 1 in chosen_filters
            #remove("1")
            #Enter genre (e.g., "Science Fiction"): 
        #case director if 2 in chosen_filters
            #remove("2")
            #Enter director (e.g., "Michael Bay"):
        #case actors if 3 in chosen_filters
            #remove("3")
            #Enter actors (e.g., "Michael J. Fox"):
        #case length if 4 in chosen filters
            #remove("4")
            #Enter minimum length in minutes (or leave blank e.g., 90): 
            #Enter maximum length in minutes (or leave blank e.g., 170):
    
        
            
    