from django.contrib import admin
from .models import User, Model, Role, Prompt, Avaliacao

admin.site.register(User)
admin.site.register(Model)
admin.site.register(Role)
admin.site.register(Prompt)
admin.site.register(Avaliacao)
