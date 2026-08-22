from django.db import models


# 1. ლექტორების მოდელი
class Lecturer(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="სახელი")
    last_name = models.CharField(max_length=50, verbose_name="გვარი")
    email = models.EmailField(unique=True, verbose_name="ელ-ფოსტა")
    department = models.CharField(max_length=100, verbose_name="დეპარტამენტი")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# 2. კურსების მოდელი (Many-to-One ლექტორებთან)
class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name="კურსის დასახელება")
    description = models.TextField(blank=True, verbose_name="აღწერა")
    credits = models.PositiveIntegerField(default=3, verbose_name="კრედიტები")
    # ბევრი კურსი - ერთ ლექტორზე
    lecturer = models.ForeignKey(
        Lecturer,
        on_delete=models.CASCADE,
        related_name="courses",
        verbose_name="ლექტორი"
    )

    def __str__(self):
        return self.title


# 3. სტუდენტების მოდელი (Many-to-Many კურსებთან)
class Student(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="სახელი")
    last_name = models.CharField(max_length=50, verbose_name="გვარი")
    email = models.EmailField(unique=True, verbose_name="ელ-ფოსტა")
    enrollment_date = models.DateField(auto_now_add=True, verbose_name="რეგისტრაციის თარიღი")
    # ბევრი სტუდენტი - ბევრ კურსზე
    courses = models.ManyToManyField(
        Course,
        related_name="students",
        blank=True,
        verbose_name="კურსები"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
