from django.contrib import admin
from .models import Student, Faculty, Course, Department, Assignment, Announcement

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('formatted_faculty_id', 'name', 'email')  # Add other fields as needed

    @admin.display(description='Faculty ID')
    def formatted_faculty_id(self, obj):
        return obj.faculty_id.zfill(4)

# Register other models as usual
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Assignment)
admin.site.register(Announcement)
