from django.contrib import admin
from .models import Class, field, semester, day_of_week, period, code

# Register your models here.

admin.site.register(Class)
admin.site.register(field)
admin.site.register(semester)
admin.site.register(day_of_week)
admin.site.register(period)
admin.site.register(code)
