def calculate_marks_required_to_pass(quiz1_marks, quiz2_marks, ga_marks):
  """Calculates the marks required to pass the course.

  Args:
    quiz1_marks: The marks scored in Quiz 1.
    quiz2_marks: The marks scored in Quiz 2.
    ga_marks: The marks scored in the average GA score.

  Returns:
    The marks required to pass the course.
  """

  total_marks_for_quiz1_and_quiz2 = 0.2 * quiz1_marks + 0.3 * quiz2_marks
  total_marks_for_ga = 0.1 * ga_marks

  if quiz1_marks is not None and quiz2_marks is not None:
    total_marks_required_to_pass = 40 - total_marks_for_quiz1_and_quiz2 - ga_marks
  else:
    total_marks_required_to_pass = 40 - 0.4 * quiz1_marks - total_marks_for_ga

  return total_marks_required_to_pass


if __name__ == "__main__":
  print("Thank you for using the required marks calculator developed by P.Sai Prasanth(Foundation Level")
  print("Please enter your Quiz1 Score below :")
  quiz1_marks = int(input())
  print("Please enter your Quiz2 Score below:")
  quiz2_marks = int(input())
  print("Please enter your Avg. GA Score below:")
  ga_marks = int(input())

  total_marks_required_to_pass = calculate_marks_required_to_pass(
      quiz1_marks, quiz2_marks, ga_marks)

  print("The marks required to pass the course is:", total_marks_required_to_pass)
  input("Thank you for using this tool. Good Luck!!")
