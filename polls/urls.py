from django.urls import path
from .views import polls_list, polls_detail
from .apiviews import PollList, PollDetail

app_name = 'polls'
urlpatterns = [
    path("", PollList.as_view(), name="polls_list"),
    path("<int:pk>", PollDetail.as_view(), name="polls_detail")
]