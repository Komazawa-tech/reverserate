from django.urls import path
from .views import ClassDetailView, SearchResultView, IndexView

app_name = "forms"
urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('result/',SearchResultView.as_view(), name = 'searchresult'),
    path('result/<int:group_id>', SearchResultView.as_view(), name= 'group_searchresult'),
    path('class/<int:id>/', ClassDetailView.as_view(), name='class_detail'),
    path('class/<int:id>/<int:group_id>', ClassDetailView.as_view(), name='group_classform' ),

]
