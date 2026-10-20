
students = [{"name":"张三","score":85,"subject":"视觉"},
            {"name":"李四","score":92,"subject":"优化"},
            {"name":"王五","score":78,"subject":"视觉"}
            ]

def filter_high_scores(student_list):
    high_scores = []
    for stu in student_list:
        if stu["score"]>80:
         high_scores.append(stu["name"])
    return high_scores

result = filter_high_scores(students)
print("高分学生名单",result)