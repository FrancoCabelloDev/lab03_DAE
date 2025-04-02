from django.urls import path
from .views import exam_list, exam_detail, exam_create, question_create, question_edit, question_delete , quiz_play

urlpatterns = [
    path('', exam_list, name='exam_list'),
    path('exam/<int:exam_id>/', exam_detail, name='exam_detail'),
    path('exam/create/', exam_create, name='exam_create'),
    path('exam/<int:exam_id>/question/add/', question_create, name='question_create'),
    path('question/edit/<int:question_id>/', question_edit, name='question_edit'),  
    path('question/delete/<int:question_id>/', question_delete, name='question_delete'),
    path('exam/<int:exam_id>/play/', quiz_play, name='quiz_play'),

]
