#IC CP2 Write To notes

"""with open("notes_pt2\\reading.txt", 'r+') as file:
    content = file.read()
    file.write('\nHi')
    
    
print('code end')"""

import csv

with open("notes_pt2/sample.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['username', 'Orange'])

print("code is done")