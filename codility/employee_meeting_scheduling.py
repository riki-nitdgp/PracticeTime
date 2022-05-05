# A one-day-long training session will be conducted twice during the next 10 days. There are N employees
# (numbered 0 to N-1) willing to attend it. Each employee has provided a list of which of the next 10 days they are able
# to participate in the training. The employees preferences are represented as an array of strings. E[K] is a string
# representing the days the K-th employee is able to attend the training. The dates of the training are yet to be scheduled.
# What is the maximum number of employees that can attend during at least one of the two scheduled dates?

# Write a function that, given an array E consisting of N strings denoting the available days for each employee,
# will return the maximum number of employees that can attend during at least one of the two scheduled days.

# Examples:
#
# Given E = ["039", "4", "14", "32", "", "34", "7"],
# the answer is 5. It can be achieved for example by running training on days 3 and 4.
# This way employees number 0, 1, 2, 3 and 5 will attend the training.
#
# Given E = ["801234567", "180234567", "0", "189234567", "891234567", "98", "9"], the answer is 7.
# It can be achieved for example by running training on days 0 and 9. This way employees all will attend the training.
#
# Given E = ["5421", "245", "1452", "0345", "53", "345"], the answer is 6.
# It can be achieved for example by running training once on day 5. This way employees all will attend the training.

def solution(E):
    # write your code in Python 3.6


    modified_input = []
    days_map = {str(i): {"count": 0, "employee": []} for i in range(0, 10)}

    for e in E:
        temp = []
        for j in e:
            temp.append(j)
        modified_input.append(sorted(temp))

    for index, value in enumerate(modified_input):
        for days in value:
            days_map[days]["employee"].append(index)
            days_map[days]["count"] += 1

    employee = [i for i in range(len(E))]
    for i in range(0, 10):
        if set(employee) == set(days_map[str(i)].get("employee")):
            return len(employee)

    day_value = list(days_map.values())
    max_emp = 0
    for emp in range(len(day_value)):
        empl_1 = day_value[emp].get("employee")
        for _emp in range(1, len(day_value)):
            empl_2 = day_value[_emp].get("employee")
            all_emp = empl_1 + empl_2
            if len(set(all_emp)) > max_emp:
                max_emp = len(set(all_emp))

    return max_emp





if __name__ == '__main__':
    a = solution(["039", "4", "14", "32", "", "34", "7"])
    print("Ans")
    print(a)

