from django.shortcuts import render
from .models import Course, CourseSession, CourseCategory


def courses(request):
    courses_categories = CourseCategory.objects.all()
    return render(request, "courses/courses.html", context={"courses_categories": courses_categories})

def category_detail(request, category_id):
    category = CourseCategory.objects.get(id=category_id)
    return render(request, "courses/category_detail.html", context={"category": category})

def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, "courses/course_detail.html", context={"course": course})