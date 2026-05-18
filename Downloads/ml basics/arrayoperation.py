import numpy as np
marks = np.array([85, 90, 78, 92, 88])
added_marks = marks + 10
print("After adding 10 marks:", added_marks)
multiplied_marks = marks * 2
print("After multiplying by 2:", multiplied_marks)
above_80 = marks[marks > 80]
print("Students scoring above 80:", above_80)