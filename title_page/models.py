from django.db import models


class Item(models.Model):
    '''List of elements'''
    text = models.TextField(default='')
