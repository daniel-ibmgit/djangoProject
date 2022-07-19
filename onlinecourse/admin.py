from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice
from nested_admin import NestedModelAdmin, NestedTabularInline

# <HINT> Register QuestionInline and ChoiceInline classes here
class ChoiceInline(NestedTabularInline):
    model = Choice
    extra = 2

class QuestionInline(NestedTabularInline):
    model = Question
    extra = 1
    inlines = [ChoiceInline]

class LessonInline(NestedTabularInline):
    model = Lesson
    extra = 5


# Register your models here.
class CourseAdmin(NestedModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# <HINT> Register Question and Choice models here
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text']

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice_text']

admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
