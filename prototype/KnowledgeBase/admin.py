from django.contrib import admin

# Register your models here.
from .models import Asset, Question, Answers, Advice, Department, Threat

admin.site.register(Asset)
admin.site.register(Question)
admin.site.register(Answers)
admin.site.register(Threat)
admin.site.register(Advice)
admin.site.register(Department)