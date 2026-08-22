import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project1.settings")
django.setup()

from project1.models import Lecturer, Course, Student

print("==================================================")
print("             1. CREATE (შექმნა)                   ")
print("==================================================")

# ძველი მონაცემების გასუფთავება ტესტირებისთვის
Student.objects.all().delete()
Course.objects.all().delete()
Lecturer.objects.all().delete()

# 1.1 შექმენით 3 ლექტორი
l1 = Lecturer.objects.create(first_name="გიორგი", last_name="ბერიძე", email="giorgi.b@step.ge", department="კომპიუტერული მეცნიერებები")
l2 = Lecturer.objects.create(first_name="დავით", last_name="კაპანაძე", email="davit.k@step.ge", department="ვებ დეველოპმენტი")
l3 = Lecturer.objects.create(first_name="ნინო", last_name="ჩხეიძე", email="nino.ch@step.ge", department="მონაცემთა ბაზები")
print("შექმნილია 3 ლექტორი.")

# 1.2 შექმენით 5 კურსი და თითოეულს მიუთითეთ ლექტორი
c1 = Course.objects.create(title="Python Basics", description="საბაზისო პითონი", credits=4, lecturer=l1)
c2 = Course.objects.create(title="Django Web Development", description="ვებ დეველოპმენტი Django-ზე", credits=6, lecturer=l2)
c3 = Course.objects.create(title="PostgreSQL & Databases", description="მონაცემთა ბაზების კურსი", credits=5, lecturer=l3)
c4 = Course.objects.create(title="Algorithms & Data Structures", description="ალგორითმები", credits=6, lecturer=l1)
c5 = Course.objects.create(title="Frontend with React", description="ფრონტენდ საფუძვლები", credits=4, lecturer=l2)
print("შექმნილია 5 კურსი.")

# 1.3 შექმენით 10 სტუდენტი და თითოეული ჩაწერეთ მინიმუმ ორ კურსზე
students_data = [
    ("ნიკა", "პაპასკირი", "nika@gmail.com", [c1, c2]),
    ("ლუკა", "მაისურაძე", "luka@gmail.com", [c2, c3]),
    ("მარიამ", "გელაშვილი", "mariam@gmail.com", [c1, c3, c4]),
    ("სალომე", "ჯაფარიძე", "salome@gmail.com", [c4, c5]),
    ("ირაკლი", "ლომიძე", "irakli@gmail.com", [c1, c5]),
    ("თამარ", "კვარაცხელია", "tamar@gmail.com", [c2, c4]),
    ("ზურა", "ნოზაძე", "zura@gmail.com", [c3, c5]),
    ("ანა", "წიკლაური", "ana@gmail.com", [c1, c2, c3]),
    ("ვახო", "შენგელია", "vakho@gmail.com", [c4, c5]),
    ("ნუცა", "ბიბილაშვილი", "nutsa@gmail.com", [c2, c3]),
]

for fname, lname, email, courses_list in students_data:
    st = Student.objects.create(first_name=fname, last_name=lname, email=email)
    st.courses.set(courses_list)

print("შექმნილია 10 სტუდენტი (თითოეული მინიმუმ 2 კურსზე).\n")


print("==================================================")
print("             2. READ (გამოტანა)                   ")
print("==================================================")

# 2.1 გამოიტანეთ ყველა სტუდენტი
print("--- 2.1 ყველა სტუდენტი ---")
for s in Student.objects.all():
    print(f"- {s}")

# 2.2 გამოიტანეთ ყველა კურსი
print("\n--- 2.2 ყველა კურსი ---")
for c in Course.objects.all():
    print(f"- {c.title} (კრედიტები: {c.credits}, ლექტორი: {c.lecturer})")

# 2.3 გამოიტანეთ ყველა ლექტორი
print("\n--- 2.3 ყველა ლექტორი ---")
for l in Lecturer.objects.all():
    print(f"- {l} | დეპარტამენტი: {l.department}")

# 2.4 იპოვეთ კონკრეტული სტუდენტი id-ის მიხედვით
first_student_id = Student.objects.first().id
student_by_id = Student.objects.get(id=first_student_id)
print(f"\n--- 2.4 სტუდენტი ID={first_student_id}-ით: {student_by_id} ---")

# 2.5 იპოვეთ კონკრეტული კურსი სახელის მიხედვით
course_by_name = Course.objects.get(title="Python Basics")
print(f"\n--- 2.5 კურსი სახელის მიხედვით: {course_by_name.title} (ლექტორი: {course_by_name.lecturer}) ---")

# 2.6 გამოიტანეთ ყველა კურსი, რომელსაც კონკრეტული ლექტორი ასწავლის
print(f"\n--- 2.6 ლექტორ {l1}-ის კურსები ---")
for c in l1.courses.all():
    print(f"- {c.title}")

# 2.7 გამოიტანეთ ყველა სტუდენტი, რომელიც კონკრეტულ კურსზე სწავლობს
print(f"\n--- 2.7 კურს '{c1.title}'-ის სტუდენტები ---")
for s in c1.students.all():
    print(f"- {s}")

# 2.8 კონკრეტული სტუდენტისთვის გამოიტანეთ ყველა კურსი
target_student = Student.objects.get(email="nika@gmail.com")
print(f"\n--- 2.8 სტუდენტ {target_student}-ის ყველა კურსი ---")
for c in target_student.courses.all():
    print(f"- {c.title}")


print("\n==================================================")
print("             3. UPDATE (განახლება)                ")
print("==================================================")

# 3.1 კონკრეტულ სტუდენტს შეუცვალეთ სახელი
target_student.first_name = "ნიკოლოზ"
target_student.save()
print(f"3.1 სტუდენტის ახალი სახელი: {target_student.first_name}")

# 3.2 კონკრეტულ ლექტორს შეუცვალეთ გვარი
l1.last_name = "ბერიძე-გვარამია"
l1.save()
print(f"3.2 ლექტორის ახალი გვარი: {l1.last_name}")

# 3.3 კონკრეტულ კურსს შეუცვალეთ დასახელება
c1.title = "Advanced Python Programming"
c1.save()
print(f"3.3 კურსის ახალი დასახელება: {c1.title}")

# 3.4 სტუდენტს დაამატეთ კიდევ ერთი კურსი
target_student.courses.add(c3)
print(f"3.4 {target_student}-ს დაემატა კურსი: {c3.title}")

# 3.5 სტუდენტს წაუშალეთ ერთი კურსი
target_student.courses.remove(c2)
print(f"3.5 {target_student}-ს წაეშალა კურსი: {c2.title}")

# 3.6 სტუდენტი გადაიყვანეთ სხვა კურსზე (ერთი წაშალეთ და მეორე დაამატეთ)
target_student.courses.remove(c1)
target_student.courses.add(c5)
print(f"3.6 {target_student} გადავიდა {c1.title}-დან -> {c5.title}-ზე")

# 3.7 კონკრეტულ კურსს შეუცვალეთ ლექტორი
c2.lecturer = l3
c2.save()
print(f"3.7 კურს '{c2.title}'-ის ახალი ლექტორი: {c2.lecturer}")


print("\n==================================================")
print("             4. DELETE (წაშლა)                    ")
print("==================================================")

# 4.1 წაშალეთ კონკრეტული სტუდენტი
student_to_delete = Student.objects.last()
deleted_student_name = str(student_to_delete)
student_to_delete.delete()
print(f"4.1 წაიშალა სტუდენტი: {deleted_student_name}")

# 4.2 წაშალეთ კონკრეტული კურსი
course_to_delete = Course.objects.get(title="Frontend with React")
course_to_delete.delete()
print(f"4.2 წაიშალა კურსი: Frontend with React")

# 4.3 წაშალეთ კონკრეტული ლექტორი
lecturer_to_delete = Lecturer.objects.get(email="davit.k@step.ge")
deleted_lecturer_name = str(lecturer_to_delete)
lecturer_to_delete.delete()
print(f"4.3 წაიშალა ლექტორი: {deleted_lecturer_name}")

# 4.4 გაასუფთავეთ კონკრეტული სტუდენტის ყველა კურსი (clear())
target_student.courses.clear()
print(f"4.4 {target_student}-ის კურსები გასუფთავდა (დარჩენილი კურსები: {target_student.courses.count()})")
