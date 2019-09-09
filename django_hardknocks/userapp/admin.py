from django.contrib import admin
from .models import Hduser,EmailVerifyRecord
# Register your models here.
admin.site.register(Hduser)
admin.site.register(EmailVerifyRecord)