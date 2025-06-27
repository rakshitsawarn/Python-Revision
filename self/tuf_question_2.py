# If student marks are given, print the grade of the student.
# Grade A: 90 and above
# Grade B: 70 to 89
# Grade C: 50 to 69
# Grade D: 35 to 49
# Fail: Below 35
# Example: If marks are 90, print "Grade A"

class Solution:
    def studentGrade(self,marks):
        if marks >= 90:
            print("Grade A")
        elif marks >= 70:
            print("Grade B")
        elif marks >= 50:
            print("Grade C")
        elif marks >= 35:
            print("Grade D")
        else:
            print("Fail")

grade = Solution()
grade.studentGrade(90)
