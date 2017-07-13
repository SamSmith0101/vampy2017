f = open("Grades.txt","w")

name = input("What is your name?")

grade = 0
test_count = 0
test_sum = 0;

while grade != -1:
	grade = float(input("Enter your test grades:"))
	test_count = test_sum + 1
	test_sum = test_sum + grade

f.write(name+"\n==============\n Average: "+str(test_sum/test_count))
