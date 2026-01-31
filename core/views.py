from rest_framework import generics, permissions
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Application, PageContent
from .serializers import ApplicationSerializer, PageContentSerializer
from .forms import ApplicationForm

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ApplicationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        application = form.save(commit=False)
        if self.request.user.is_authenticated:
            application.user = self.request.user
        application.save()
        messages.success(self.request, 'Ваша заявка успешно отправлена!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Пожалуйста, исправьте ошибки в форме.')
        return super().form_invalid(form)

class ApplicationCreateView(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = (permissions.AllowAny,)

class ApplicationListView(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Application.objects.filter(user=self.request.user)

class PageContentListView(generics.ListAPIView):
    queryset = PageContent.objects.all()
    serializer_class = PageContentSerializer
    permission_classes = (permissions.AllowAny,)
