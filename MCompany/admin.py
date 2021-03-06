
from django.contrib import admin

from MCompany.models import (
    Booking,
    Category,
    Company,
    Event,
    GymPlan,
    ImageAlbum,
    Service,
    SocialLink,
    Visitior,
)

# Register your models here.

admin.site.register(ImageAlbum)
admin.site.register(Booking)
admin.site.register(Service)
admin.site.register(Event)
admin.site.register(SocialLink)
admin.site.register(Visitior)
admin.site.register(Category)
admin.site.register(GymPlan)

class SuperCompanyModel(admin.ModelAdmin):
    list_display = (
        "name",
        'user',
        "thumbnail",
        "location",
        "opening_time",
        "closing_time",
        "category",
        'email',

    )



admin.site.register(Company, SuperCompanyModel) 

