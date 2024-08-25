from django.urls import path
from .views import CourseListCreate, CourseRetrieveDestroy, CourseInstanceListCreate, CourseInstanceRetrieveDestroy
from . import views
urlpatterns = [
    # path('courses/', CourseListCreate.as_view()),
    path('api/courses/', views.CourseListCreate.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseRetrieveDestroy.as_view()),
    path('instances/', CourseInstanceListCreate.as_view()),
    path('instances/<int:pk>/', CourseInstanceRetrieveDestroy.as_view()),
]
