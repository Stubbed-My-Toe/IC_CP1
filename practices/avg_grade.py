#IC 1st avg grade

first_prd = float(input("What is your grade percentage in your first period?"))
second_prd = float(input("What is your grade percentage in your second period?"))
third_prd = float(input("What is your grade percentage in your third period?"))
fourth_prd = float(input("What is your grade percentage in your fourth period?"))
fifth_prd = float(input("What is your grade percentage in your fifth period?"))
sixth_prd = float(input("What is your grade percentage in your sixth period?"))
seventh_period = float(input("What is your grade percentage in your seventh period?"))
eighth_period = float(input("What is your grade percentage in your eighth period?"))

grade_total = float(first_prd+second_prd+third_prd+fourth_prd+fifth_prd+sixth_prd+seventh_period+eighth_period)
not_average_grade = (grade_total /8)
average_grade = (not_average_grade,2)

print("Here is your average grade!",average_grade)