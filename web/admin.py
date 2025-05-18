from django.contrib import admin

from .models import Daily, Weekly, Monthly, Yearly, LongTerm


admin.site.register(Daily)
admin.site.register(Weekly)
admin.site.register(Monthly)
admin.site.register(Yearly)
admin.site.register(LongTerm)

