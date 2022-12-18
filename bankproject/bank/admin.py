from django.contrib import admin
from . models import Bank
from . models import About
from . models import login
from . models import Register
from . models import img


# Register your models here.
admin.site.register(Bank)
admin.site.register(About)
admin.site.register(login)
admin.site.register(Register)
admin.site.register(img)

