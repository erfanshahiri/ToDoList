from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=48, unique=True)

class Daily(models.Model):
    title = models.CharField(_('title'), max_length=50, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(_('description'), blank=True)
    time_todo = models.DateTimeField(_('time_todo'), null=True, blank=True)
    time_needed = models.CharField(_('time_needed'), max_length=50, blank=True, null=True)
    created_time = models.DateTimeField(_('created_time'), auto_now_add=True, blank=True, null=True)
    is_done = models.BooleanField(_('is_done'), default=False)

    def __str__(self):
        return self.title


class Weekly(models.Model):
    title = models.CharField(_('title'), max_length=50, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(_('description'), blank=True)
    time_todo = models.DateTimeField(_('time_todo'), null=True, blank=True)
    time_needed = models.CharField(_('time_needed'), max_length=50, blank=True, null=True)
    created_time = models.DateTimeField(_('created_time'), auto_now_add=True, blank=True, null=True)
    is_done = models.BooleanField(_('is_done'), default=False)

    def __str__(self):
        return self.title


class Monthly(models.Model):
    title = models.CharField(_('title'), max_length=50, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(_('description'), blank=True)
    time_todo = models.DateTimeField(_('time_todo'), null=True, blank=True)
    time_needed = models.CharField(_('time_needed'), max_length=50, blank=True, null=True)
    created_time = models.DateTimeField(_('created_time'), auto_now_add=True, null=True, blank=True)
    is_done = models.BooleanField(_('is_done'), default=False)

    def __str__(self):
        return self.title


class Yearly(models.Model):
    title = models.CharField(_('title'), max_length=50, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(_('description'), blank=True)
    time_todo = models.DateTimeField(_('time_todo'), null=True, blank=True)
    time_needed = models.CharField(_('time_needed'), max_length=50, blank=True, null=True)
    created_time = models.DateTimeField(_('created_time'), auto_now_add=True, null=True, blank=True)
    is_done = models.BooleanField(_('is_done'), default=False)

    def __str__(self):
        return self.title


class LongTerm(models.Model):
    title = models.CharField(_('title'), max_length=50, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(_('description'), blank=True)
    time_todo = models.DateTimeField(_('time_todo'), null=True)
    time_needed = models.CharField(_('time_needed'), max_length=50, blank=True, null=True)
    created_time = models.DateTimeField(_('created_time'), auto_now_add=True, null=True, blank=True)
    is_done = models.BooleanField(_('is_done'), default=False)

    def __str__(self):
        return self.title