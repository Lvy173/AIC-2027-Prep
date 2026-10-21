
students = [{"name": "张三","score": 85,"subject": "视觉"},
           {"name": "李四","score": 92,"subject": "优化"},
           {"name": "王五","score": 78,"subject": "视觉"}
           ]

def filter_low_scores(student):
    low_scores = []
    for stu in student:
        if stu["score"] < 80:
            low_scores.append(stu["name"])
    return low_scores

result = filter_low_scores(students)
print("低分学生名单" ,result)