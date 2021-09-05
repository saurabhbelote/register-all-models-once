from django.contrib import admin
import django.apps
from django.db import models
import leads
# here we can register all models with ease 
models = django.apps.apps.get_models()
print(models)

for model in models :
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

# here we can unregister model we don't want to use
admin.site.unregister(leads.models.Founder) 

# here you can get only field you want to user from models
'''
class LeadAdmin(admin.ModelAdmin):
    fields = ['first_name','last_name']

admin.site.register(post,LeadAdmin)

'''
