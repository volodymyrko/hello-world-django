""" enable HttpRequestEntry model in admin interface
"""

from django.contrib import admin
from utils42cc.models import HttpRequestEntry, ModelActionLog

admin.site.register(HttpRequestEntry)
admin.site.register(ModelActionLog)
