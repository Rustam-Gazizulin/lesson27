from courses.models import Course
from django.http import JsonResponse
from django.shortcuts import get_list_or_404


def courses(request):
    if request.method == 'GET':
        courses_list = Course.objects.all()
        response = []
        for course in courses_list:
            response.append(
                 {
                 "id": course.id,
                  "slug": course.slug,
                  "author": course.author,
                  "description": course.description,
                  "start_day": course.start_day,
                  "status": course.status,
                  "created": course.created,
                   }
                     )
        return JsonResponse(response, safe=False)


def new_courses(request):
    if request.method == 'GET':
        courses_list = Course.objects.filter(status__icontains='new')
        response = []
        for course in courses_list:
            response.append(
                {
                    "id": course.id,
                    "description": course.description,
                    "status": course.status,
                }
            )
        return JsonResponse(response, safe=False)

def get_course(request, slug):
    if request.method == 'GET':
        courses_list = get_list_or_404(Course, status=slug)
        response =[]
        for course in courses_list:
            response.append(
            {
                "id": course.id,
                "slug": course.slug,
                "author": course.author,
                "description": course.description,
                "start_day": course.start_day,
                "status": course.status,
                "created": course.created,
            })
        return JsonResponse(response, safe=False)


def search(request):
    courses = Course.objects.all()
    search_text = request.GET.get("author", None)
    if search_text:
        courses = courses.filter(author=search_text)

    response = []
    for course in courses:
        response.append(
            {
                "id": course.id,
                "slug": course.slug,
                "author": course.author,
                "description": course.description,
                "start_day": course.start_day,
                "status": course.status,
                "created": course.created,
            }
        )
    return JsonResponse(response, safe=False)
