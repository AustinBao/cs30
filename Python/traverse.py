def countSurvey(file):
    file = list(open(f'Python/traverse-data-start-main/{file}', 'r'))
    # Read each line in the file
    results = {"Yes":0, "No":0, "Maybe":0}
    for line in file:
        # .strip() removes leading and trailing whitespaces
        match line.strip():
            case "Yes":
                results["Yes"] += 1
            case "Maybe":
                results["Maybe"] += 1
            case "No":
                results["No"] += 1
 
    return f"Yes ({results['Yes']}), No ({results['No']}), Maybe ({results['Maybe']})"


def countAge(file):
    file = list(open(f'Python/traverse-data-start-main/{file}', 'r'))
    ages = {"Under 18":0, "18 to 35":0, "36 to 65":0, "Above 65":0, }
    for line in file:
        num = int(line.strip())
        if num < 18:
            ages["Under 18"] += 1
        elif num >= 18 and num <= 35:
            ages["18 to 35"] += 1
        elif num >= 36 and num <= 65:
            ages["36 to 65"] += 1
        else:
            ages["Above 65"] += 1

    return f"Under 18 ({ages['Under 18']}), 18 to 35 ({ages['18 to 35']}), 36 to 65 ({ages['36 to 65']}), Above 65 ({ages['Above 65']}"


def countOddorEven(file):
    file = list(open(f'Python/traverse-data-start-main/{file}', 'r'))
    even, odd = 0, 0
    for line in file: 
        if int(line.strip()) % 2 == 0:
            even += 1
        else: 
            odd += 1

    return f"Even ({even}), Odd ({odd})"



print(countSurvey("survey-results.txt"))

print(countAge("age-data.txt"))

print(countOddorEven("number-data.txt"))