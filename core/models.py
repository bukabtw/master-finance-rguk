from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class Application(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='applications', 
        verbose_name=_("Пользователь")
    )
    name = models.CharField(_("Имя"), max_length=100)
    phone = models.CharField(_("Телефон"), max_length=20)
    email = models.EmailField(_("Email"), blank=True, null=True)
    message = models.TextField(_("Сообщение"), blank=True)
    created_at = models.DateTimeField(_("Дата создания"), auto_now_add=True)

    class Meta:
        verbose_name = _("Заявка")
        verbose_name_plural = _("Заявки")
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"

class PageContent(models.Model):
    key = models.CharField(_("Ключ"), max_length=50, unique=True, help_text=_("Уникальный идентификатор блока"))
    title = models.CharField(_("Заголовок"), max_length=200, blank=True)
    content = models.TextField(_("Содержимое"), blank=True)
    image = models.ImageField(_("Изображение"), upload_to='content/', blank=True, null=True)

    class Meta:
        verbose_name = _("Контент страницы")
        verbose_name_plural = _("Контент страниц")

    def __str__(self):
        return self.key
