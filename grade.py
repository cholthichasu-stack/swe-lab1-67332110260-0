def calculate_grade(scores):
    # 1. ตรวจสอบก่อนว่าลิสต์ว่างหรือไม่ เพื่อป้องกัน ZeroDivisionError
    if not scores:
        return "N/A", 0  # หรือจะ return None ก็ได้

    # 2. ใช้ฟังก์ชัน sum() แทนการเขียน loop เพื่อความกระชับและรวดเร็ว
    total = sum(scores)
    
    # คำนวณค่าเฉลี่ย
    average = total / len(scores)

    # 3. การตัดเกรด (Logic เดิมถูกต้องแล้ว แต่จัดรูปแบบให้ดูง่ายขึ้น)
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    return grade, average

# การทดสอบ
scores_list = [85, 92, 78, 88, 95]
grade, avg = calculate_grade(scores_list)
print(f"Average: {avg:.2f}, Grade: {grade}")

# ทดสอบกรณีลิสต์ว่าง (เพื่อเช็คว่า bug หายไปหรือยัง)
empty_scores = []
print(f"Empty case: {calculate_grade(empty_scores)}")
print(calculate_grade([]))
