from django.urls import path
from .views import login_view, home_view, issue_book_view, return_book_view
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('issue-book/', issue_book_view, name='issue_book'),
    path('return-book/', return_book_view, name='return_book'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
