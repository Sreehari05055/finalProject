from django.contrib import admin

from service.models import ChatHistory, CVStructure, CoverLetterStructure


# Register your models here.
class ChatHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'sender', 'timestamp')  # Columns to display in the list view
    list_filter = ('sender', 'timestamp')  # Filter options in the right sidebar
    search_fields = ('user__username', 'message')  # Search bar to search by username or message
    ordering = ('-timestamp',)  # Order by most recent first


# Register the model and custom admin class
admin.site.register(ChatHistory, ChatHistoryAdmin)


@admin.register(CVStructure)
class CVStructureAdmin(admin.ModelAdmin):
    list_display = ('section_name', 'order', 'is_mandatory')  # Display these fields in the list view
    list_editable = ('order', 'is_mandatory')  # Allow editing of 'order' and 'is_mandatory' directly in the list view
    search_fields = ('section_name',)  # Enable search by 'section_name'
    ordering = ('order',)  # Default ordering by 'order'
    list_filter = ('is_mandatory',)


@admin.register(CoverLetterStructure)
class CoverLetterStructureAdmin(admin.ModelAdmin):
    list_display = ('section_name', 'order', 'is_mandatory')
    list_editable = ('order', 'is_mandatory')
    search_fields = ('section_name',)
    ordering = ('order',)
    list_filter = ('is_mandatory',)
