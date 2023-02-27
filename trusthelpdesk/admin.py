from django.contrib import admin
from .models import * 


class ChoiceRDBMS(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionRBDMS(admin.ModelAdmin):
    fieldsets = [(Question, {'fields': ['name', 'answer_method','other_method', 'other_title' ]}),]
    inlines = [ChoiceRDBMS]

class UserInfoRDBMS(admin.ModelAdmin):
    list_display = ('email','issues','more_issue', 'full_information_issue', 'phrase', 'date', 'update_date')


admin.site.register(Question, QuestionRBDMS)
admin.site.register(Choice)
admin.site.register(UsersInfo, UserInfoRDBMS)