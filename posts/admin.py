# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

#Lets import the models

from .models import Post

admin.site.register(Post)


