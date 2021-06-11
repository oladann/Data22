student_1 = {"name": "susan",
             "stream": "tech",
             "completed_lessons": 4,
             "completed_lesson_names": ["variables", "data_types", "set_up"]}


student_1["completed_lessons"] = 3
print(student_1["completed_lessons"])

student_1["completed_lesson_names"].remove("data_types")
print(student_1["completed_lesson_names"])

print(student_1.keys())
print(student_1.values())