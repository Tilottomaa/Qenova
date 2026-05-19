from django.contrib import admin
from .models import User,OrganizationUser,Admin

admin.site.register(User)
admin.site.register(OrganizationUser)
admin.site.register(Admin)

# Register your models here.
