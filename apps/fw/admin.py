from django.contrib import admin

from django.contrib.auth.models import Group
from apps.fw.models import FwUser

# Register your models here.
# Now register the new UserAdmin...
admin.site.register(FwUser)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
