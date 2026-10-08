totalscore = 0
scores = [72, 45, 90, 61, 38]
for score in scores:
    if score >= 80:
        print(f"Score: {score} - Grade: A")
    elif score >= 70:
        print(f"Score: {score} - Grade: B")
    elif score >= 50:
        print(f"Score: {score} - Grade: C")
    else:
        print(f"Score: {score} - Grade: F")
    totalscore = totalscore + score
average = totalscore / len(scores) if scores else 0
average = round(average, 1)

print(f"The average score is: {average} ")
passmarks = 50
pass_students = 0
for score in scores:
    if score >= passmarks:
       pass_students += 1
    fail_students = len(scores) - pass_students

print(f"{pass_students} passed exams")
print(f"{fail_students} failed exams")