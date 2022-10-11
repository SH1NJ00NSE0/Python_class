marks =[90,25,67,45,80]
num=0

for mark in marks:
	num+=1
	print(mark)
	if mark>=60:
		print(f"{num}번 학생은 합격입니다.")
	else:
		print(f"{num}번 학생은 불합격입니다.")