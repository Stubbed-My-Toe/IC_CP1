import csv
while True:
    try:
        with open("notes_pt2/readable_file", "r") as file:
            content = file.read()
            print(content.upper())
    except:
        print("File is not found")
    else:
        print("Code is workable")
        break

try:
    with open("notes_pt2\Batman.csv", mode="r") as csv_file:
        content = csv.reader(csv_file)
        headers = next(content)
        rows =[]
        for line in content:
            rows.append({headers[0]: line[0], headers[1]: line[1] })
except:
    print("Can't find the CSV")

else:
    for line in rows:
        print(line)