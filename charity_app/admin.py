from django.contrib import admin
from .models import Institution
# Register your models here.

class InstitutionAdmin(admin.ModelAdmin):
    class Meta:
        def __str__(self):
            return "name:{}  description:{} type:{} category:".format(self.name, self.description, self.type, self.category)


admin.site.register(Institution, InstitutionAdmin)