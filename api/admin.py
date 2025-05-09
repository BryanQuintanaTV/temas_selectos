from django.contrib import admin

# Register your models here.
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('date', 'dataset_version', 'message_send', 'is_resolved')
    search_fields = ('message_send', 'message_report', 'dataset_version')
    actions = None

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.is_resolved:
            # 🔒 Si ya está resuelto, todos los campos se vuelven solo lectura
            return [f.name for f in self.model._meta.fields]
        # 🟢 Si no está resuelto, se puede editar is_resolved
        return ('message_send', 'message_receive', 'date', 'dataset_version', 'message_report')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
