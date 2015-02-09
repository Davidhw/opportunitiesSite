from django.contrib import admin
from addOpportunity.models import Posting

#https://docs.djangoproject.com/en/1.7/ref/contrib/admin/actions/#adding-actions-to-the-modeladmin
def makeVisible(modeladmin,request,queryset):
    queryset.update(visible=True)
makeVisible.short_description = "Make selected posts visible"

def hide(modeladmin,request,queryset):
    queryset.update(visible=False)
hide.short_description = "Make selected posts not visible"


class PostingAdmin(admin.ModelAdmin):
    list_display = ['name','organization','visible']
    ordering = ['-date']
    actions = [hide,makeVisible]

admin.site.register(Posting,PostingAdmin)

