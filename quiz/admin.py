from django.contrib import admin

# Register your models here.
from quiz.models import Choice, Question


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4  # 一個問題有四的選項


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text')
    fieldsets = [(None, {'fields': ['question_text']}),
                 ]

    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
