from django.contrib import admin
from crawlfund.models import Question,Choice
# Register your models here.
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    list_display= ('question_text','pub_date')
    fields = ['pub_date','question_text']
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']
admin.site.register(Question,QuestionAdmin)
