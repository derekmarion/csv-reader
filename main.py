import csv

def adopt():
    running = True
    while running == True:
        selection = input("\nWhat type of animal would you like to adopt?:\n1.Dogs\n2.Cats\nq to quit\n\n")
        match selection:
            case "1":
                with open("./data/dogs.csv", mode='r') as csv_file: #note that with statement closes the resource after executing the code block, so you don't have to manually close it
                    csv_reader = csv.DictReader(csv_file)
                    for row in csv_reader:
                        print(f"{row['name'].title()} is a {row['age']} year old {row['breed'].title()}") # note that automatic column names are whitespace sensitive, be aware of whitespace in your input file, or specifically define key names         
            case "2":
                with open("./data/cats.csv", mode='r') as csv_file:
                    csv_reader = csv.DictReader(csv_file, fieldnames=["name", "age", "breed"]) #when you specify the key names explicitly, note that the for loop will read the first column. If they are implicit, it will skip them
                    for row in csv_reader:
                        print(f"{row['name'].title()} is a {row['age']} year old {row['breed'].title()}")
            case "q":
                running = False
            case _:
                print("\nPlease make a selection")
adopt()