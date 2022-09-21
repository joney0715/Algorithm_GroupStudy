number_of_switchs = int(input())
switch_status = list(map(int, input().split()))
number_of_students = int(input())
students = []
for i in range(number_of_students):
    student_status = list(map(int, input().split()))
    students.append(student_status)

#남자인 경우
def man_switch(number, switch_status):
    for i in range(number-1, number_of_switchs, number):
        switch_status[i] = abs(switch_status[i] - 1)
    return switch_status

#여자인 경우
def woman_switch(number, switch_status):
    number -= 1
    switch_status[number] = abs(switch_status[number] -1)
    for i in range(1, number_of_switchs):
        if number-i >= 0 and number+i <= number_of_switchs:
            if switch_status[number-i] == switch_status[number+i]:
                switch_status[number-i] = abs(switch_status[number-i] -1)
                switch_status[number+i] = abs(switch_status[number+i] -1)
            else:
                break
        else:
            break       
    return switch_status

for student in students:
    if student[0] == 1:
        man_switch(student[1], switch_status)
    else:
        woman_switch(student[1], switch_status)

#1 0 0 0 1 1 0 1
for i in range(1, number_of_switchs+1):
    if i % 20 == 0:
        print(switch_status[i-1])
    else:
        print(switch_status[i-1], end = ' ')
