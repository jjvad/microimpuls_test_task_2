from django.db import models


class Task(models.Model):
    STATUS_CHOICES = [
        ('added', 'Добавлена'),
        ('in_progress', 'В работе'),
        ('completed', 'Выполнена'),]

    name = models.CharField(max_length=255, verbose_name='Название задачи')
    description = models.TextField(blank=True, verbose_name='Описание задачи')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='added', verbose_name='Статус задачи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['created_at']
        db_table = 'scheduled_tasks'

    def __str__(self):
        return f'{self.name} ({self.get_status_display()})'
