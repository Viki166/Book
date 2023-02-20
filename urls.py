from django.urls import path
from chat.views import BookListView

urlpatterns = [
    path("",BookListView.as_view(), name = 'home'),
    # path("<str:room_name>/",views.room_view, name = "chat-room"),
    
]
