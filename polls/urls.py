from django.urls import path
from rest_framework.routers import DefaultRouter
from .apiviews import PollViewSet, ChoiceList, CreateVote

router = DefaultRouter()
router.register('', PollViewSet, base_name='polls')

app_name = 'polls'
urlpatterns = [
    path("<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote")
]

urlpatterns += router.urls
