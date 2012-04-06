""" enable HttpRequestEntry model in admin interface
"""

from django.contrib import admin
from utils42cc.models import HttpRequestEntry

admin.site.register(HttpRequestEntry)
