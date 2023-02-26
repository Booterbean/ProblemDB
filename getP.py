pathdb = "/ProblemDB"

import pyperclip

selection = input("Enter problem key: ").split("-")

pathlinks = {
    
        "A" : "/Algebra",
        "NT" : "/NumberTheory",
        "C" : "/Combinatorics",
        "G" : "/Geometry",
        "CA" : "/CalculusAnalysis",

        "1" : "/Difficulty_1of5",
        "2" : "/Difficulty_2of5",
        "3" : "/Difficulty_3of5",
        "4" : "/Difficulty_4of5",
        "5" : "/Difficulty_5of5",
    }

problem_path = ""
for i in selection[:-1]:
    problem_path += pathlinks[i]
problem_path = pathdb + problem_path + "/" + selection[-1] + "/problem"
pyperclip.copy(problem_path)
print("Path copied to clipboard")
