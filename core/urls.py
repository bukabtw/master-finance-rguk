from django.urls import path
from .views import ApplicationCreateView, ApplicationListView, PageContentListView

urlpatterns = [
    path('applications/', ApplicationCreateView.as_view(), name='application-create'),
    path('my-applications/', ApplicationListView.as_view(), name='my-applications'),
    path('content/', PageContentListView.as_view(), name='page-content'),
]
