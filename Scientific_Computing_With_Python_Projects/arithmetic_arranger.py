def arithmetic_arranger(problems, show = False):
    # Lenght of list error:
    if len(problems) > 5:
        return "Error: Too many problems."
    else:
        # Assign variable to each line
        first_line = ""
        second_line = ""
        dash_line = ""
        answer_line = ""
        # Iterate through the operation on the list:
        for i in problems:
            # Split the operation using whitespaces as separators and saving each value
            # on a different variable 
            items = i.split()
            operand_1 = items[0]
            operand_2 = items[-1]
            symbol = items[1]
            # Expected max width in each operation:
            width = max(len(operand_1), len(operand_2)) + 2
            
            # Digit only error:
            if not operand_1.isdigit() or not operand_2.isdigit():
                return "Error: Numbers must only contain digits."
            # Symbol specific error:
            else:
                if symbol == "+":
                    answer = int(operand_1) + int(operand_2)
                elif symbol == "-":
                    answer = int(operand_1) - int(operand_2)
                else:
                    return "Error: Operator must be '+' or '-'."
                
                # Max length of digits error
                if len(operand_1) > 4 or len(operand_2) > 4:
                    return "Error: Numbers cannot be more than four digits."
                
                # Add to each line its value in order, adjusting width to align them to the right
                first_line += str(operand_1).rjust(width)
                second_line += symbol +str(operand_2).rjust(width - 1)
                dash_line += "-" * width
                answer_line += str(answer).rjust(width)
                
                # In case of more than one operation, add 4 whitespaces before adding
                # the next set of numbers
                if len(problems) > 1:
                    first_line += "    "
                    second_line += "    "
                    dash_line += "    "
                    answer_line += "    "
                
                # Write in a new variable all the lines, defined with newlines to match correctly
                # If second value of function set to true, it displays the answers
                # Added a .rstrip() to eliminate trailing spaces after the last operation
                if show == True:
                    problem_arranged = (first_line.rstrip() + "\n" + second_line.rstrip() 
                                        + "\n" + dash_line.rstrip() + "\n" + answer_line.rstrip())
                else:
                    problem_arranged = (first_line.rstrip() + "\n" + second_line.rstrip() 
                                        + "\n" + dash_line.rstrip())
        
        
        return problem_arranged
