try:
    with open('scores.txt', 'r') as file:
        sum_score = 0
        student_counts = 0
        lines = file.readlines()
        for line in lines:
            try:
                score = line.split(" ")[-1]
                sum_score += int(score)
                student_counts += 1
            except ValueError as value_err:
                print("Bad score value for {}, ignored".format(line.split(' ')[0]))
        with open('log.txt', 'w') as result:
            result.write("The class average is {} for {} students.".format(sum_score / student_counts, student_counts))
            print("\nThe class average is {} for {} students.".format(sum_score / student_counts, student_counts))
except IOError as err:
    print("IOError! Details: {}".format(err))