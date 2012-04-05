"""enable control models via admin interface
"""

from contact.models import Contact
from django.contrib import admin

admin.site.register(Contact)