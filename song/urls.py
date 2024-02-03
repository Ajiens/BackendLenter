from django.urls import path
from .views import SongData

urlpatterns = [
    # ... other URL patterns ...
    path('', SongData.as_view(), name='song_data'),
    path('audio/<int:id>/', SongData.as_view(), name='song_detail'),
]
