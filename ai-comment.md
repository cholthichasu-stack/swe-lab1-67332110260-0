นี่คือโค้ดที่ได้รับการแก้ไข Bug และปรับปรุงให้มีความรัดกุม (Robust) มากขึ้นครับ

### โค้ดที่แก้ไขแล้ว:

```python
def calculate_grade(scores):
    # แก้ Bug: ตรวจสอบว่า scores เป็นลิสต์ว่างหรือไม่ เพื่อป้องกัน ZeroDivisionError
    if not scores:
        return "No scores provided", 0

    # ปรับปรุง: ใช้ฟังก์ชัน sum() แทนการใช้ loop เพื่อความรวดเร็วและอ่านง่าย
    total = sum(scores)
    
    # คำนวณค่าเฉลี่ย
    average = total / len(scores)
    
    # การตัดสินเกรด (ส่วนนี้เดิมถูกต้องอยู่แล้ว)
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

# --- ส่วนทดสอบ ---
# 1. กรณีมีข้อมูลปกติ
scores1 = [85, 92, 78, 88, 95]
print(f"Normal case: {calculate_grade(scores1)}")

# 2. กรณีลิสต์ว่าง (จุดที่เคยเป็น Bug)
scores2 = []
print(f"Empty list case: {calculate_grade(scores2)}")
```

### สรุปจุดที่แก้ไข:

1.  **ป้องกันการหารด้วยศูนย์ (Division by Zero):** เพิ่มเงื่อนไข `if not scores:` เพื่อเช็คว่าถ้าไม่มีข้อมูลในลิสต์ ให้รีเทิร์นค่าออกไปทันที (เช่น "No scores provided") แทนที่จะปล่อยให้โปรแกรมคำนวณต่อจน Error
2.  **ใช้ `sum(scores)`:** เปลี่ยนจากการเขียน Loop บวกเลขทีละตัว มาใช้ฟังก์ชันมาตรฐานของ Python ซึ่งมีประสิทธิภาพสูงกว่าและลดโอกาสเขียนตรรกะผิดพลาด
3.  **การจัดการข้อมูล:** โค้ดใหม่จะมีความยืดหยุ่นมากขึ้น ไม่พังหากมีคนส่งลิสต์ว่างเข้ามาในระบบครับ
