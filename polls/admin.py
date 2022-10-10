from django.contrib import admin

from .models import Choice, Question

#admin page property
admin.site.site_header = '質問管理サイト'
admin.site.enable_nav_sidebar = False

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    
    
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', 
         {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    #チェンジリスト(一覧)の表示項目
    list_display = ('question_text','pub_date',
                    'was_published_recently')
    list_filter = ['pub_date']

admin.site.register(Question, QuestionAdmin)


"""
adminサイトのプロパティ
https://speakerdeck.com/akiyoko/how-to-customize-admin-djangocon-jp-2021?slide=25

"""
