def survey(file):
    file = list(open(f'traverse-data-start-main/{file}', 'r'))

    # Read each line in the file
    results = {"Yes":0, "No":0, "Maybe":0}
    for line in file:
        # .strip() removes leading and trailing whitespaces
        if line.strip() == "Yes":
            results["Yes"] += 1
        elif line.strip() == "Maybe":
            results["Maybe"] += 1
        else:
            results["No"] += 1   

    return f"Yes ({results['Yes']}), No ({results['No']}), Maybe ({results['Maybe']})"


print(survey("survey-results.txt"))

