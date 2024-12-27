from django.urls import path
from .views import courses, category_detail, course_detail

app_name = "courses"

urlpatterns = [
    path("courses", courses, name="courses"),
    path("category_detail/<int:category_id>", category_detail, name="category_detail"),
    path("course_detail/<int:course_id>", course_detail, name="course_detail"),
]
