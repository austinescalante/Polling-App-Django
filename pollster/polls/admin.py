from django.contrib import admin
#Add admin functionality

from .models import Question,Choice

admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Welcome to the Pollster admin area"

#Want choices within question admin screen

class ChoiceInLine(admin.TabularInline):
    model = Choice
    #extra lines
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    #tuple
    fieldsets = [(None, {'fields': ['question_text']}), ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),]

    inlines =[ChoiceInLine]




# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question,QuestionAdmin)

# Register your models here.
