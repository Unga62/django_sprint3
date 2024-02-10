from django.db import models


class PublishedModel(models.Model):
    """Абстрактная модель. Добавляет флаг is_published
    и метку создания записи created_at.
    """

    is_published = models.BooleanField(default=True,
                                       verbose_name='Опубликовано',
                                       help_text='Снимите галочку,'
                                       ' чтобы скрыть публикацию.')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Добавлено')

    class Meta:
        abstract = True


class TitleModel(models.Model):
    """Абстрактаная модель. Добавляет title - наименование заголовка"""

    title = models.CharField(max_length=256, verbose_name='Заголовок')

    class Meta:
        abstract = True
