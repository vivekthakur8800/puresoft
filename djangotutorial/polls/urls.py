from django.urls import path
from .views import index,detail,vote,results

app_name="polls"
urlpatterns=[
    path("",index,name='index'),
    path("<int:question_id>/",detail,name="detail"),
    path("<int:pk>/results/",results,name="results"),
    path("<int:question_id>/vote/",vote,name="vote"),
]

# from .views import vote,IndexView,DetailView,ResultsView
# urlpatterns=[
#     path("",IndexView.as_view(),name='index'),
#     path("<int:question_id>/",DetailView.as_view(),name="detail"),
#     path("<int:pk>/results/",ResultsView.as_view(),name="results"),
#     path("<int:question_id>/vote/",vote,name="vote"),
# ]