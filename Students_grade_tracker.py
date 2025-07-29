attendance = int(input("Enter attendance"))
no_of_subjects = int(input("Enter number of subjects"))

print("Enter your id:")
id = int(input())
print("Enter your name:")
name = input()

total_score = 0
count = 0
for i in range(1,100):
    print(f"Enter score for student[{i}]:")
    score = int(input())
    total_score += score
    count += 1
    print("Do you want to enter another score? (yes/no): ")
    q = input()
    if q == "yes":
        continue
    else:
        break
avg = total_score / count
if avg >=85:
    performance = "Excellent"
    print(performance)
elif(70 <= avg <=84):
    performance = "Good"
    print(performance)
elif(50 <= avg <=69):
    performance = "Average"
    print(performance)
else:
    performance = "Needs Improvement"
    print(performance)
if attendance < 75:
    a = "Warning - low attendance"
else:
    a = "OK Attendance Satisfied"



print("======= Student Details ========")
print("Student id: ",id)
print("Student name: ",name)
print("Student Attendance: ",attendance)
print("Total score: ",total_score)
print("Average score: ",avg)
print("performance:",performance)
print("Attendance:",a)
print("================================")