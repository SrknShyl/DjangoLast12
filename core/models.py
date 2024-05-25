from django.db import models

# C

class GeneralSetting(models.Model):
    name = models.CharField(
        default= '',
        max_length= 254,
        blank=True,
        verbose_name='Name',
        help_text = 'This is variable of the setting'
    )
    description = models.CharField(
        default= '',
        max_length=254,
        blank=True,
        verbose_name='Description',
        help_text = ''
    )
    parameter = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Parameter',
        help_text = ''
    )
    update_date = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name='Update Date'
    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name='Created Date'
    )

    def __str__(self):
        return f'General Setting: {self.name}'

    class Meta:
        verbose_name = 'GeneralSetting'
        verbose_name_plural = 'GeneralSetting'
        ordering = ('name',)