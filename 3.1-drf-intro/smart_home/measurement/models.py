from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length = 30, verbose_name = 'Название датчика')
    description = models.TextField(blank = True, verbose_name = 'Описание')
    
    def __str__(self):
        return '%s (%s)' % (self.name, self.description)

    class Meta:
        verbose_name='Датчик'
        verbose_name_plural='Датчики'
        ordering=['id']


class Measurement(models.Model):
     measure = models.FloatField(verbose_name = 'Температура')
     sensor_id = models.ForeignKey(Sensor, 
        on_delete = models.CASCADE, 
        related_name = 'measurements')
     stamp = models.DateTimeField(auto_now_add = True, verbose_name = 'Дата измерения')

     class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'
        #ordering = ['-date']