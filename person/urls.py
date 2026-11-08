from django.urls import path
from .views import PersonListView,PersonUpdateDeleteView
urlpatterns = [
    path('persons_list/',PersonListView.as_view(), name='persons_list'),
    path('persons_list/<int:pk>/',PersonUpdateDeleteView.as_view(), name='person-detail')
]
