from django.contrib import admin
from .models import Details
from .models import Otp
from .models import Salon
from .models import SalonDetailsSingleDeals_1
from .models import SalonDetailsComboDeals_1
from .models import SalonBranch_1
from .models import Expert
from .models import Reviews_rating

# Register your models here.
class DetailsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': ['firstname']}),
        ('lastname', {'fields': ['lastname'],'classes': ['collapse']}),
        ('email', {'fields': ['email'],'classes': ['collapse']}),
        ('username', {'fields': ['username'],'classes': ['collapse']}),
        ('password', {'fields': ['password'],'classes': ['collapse']}),
        ('mobilenumber', {'fields': ['mobilenumber'],'classes': ['collapse']}),
        ('address', {'fields': ['address'],'classes': ['collapse']}),
        ('registered', {'fields': ['registered'],'classes': ['collapse']}),
    ]
    list_display = ('firstname','lastname','email','username','password','mobilenumber','address','registered')

class OtpAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': ['otp']}),
        ('mail', {'fields': ['mail'],'classes': ['collapse']}),
    ]
    list_display = ('otp','mail')


class SalonBranch_1Admin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': ['branchId']}),
        ('salonId', {'fields': ['salonId'],'classes': ['collapse']}),
        ('address', {'fields': ['address'],'classes': ['collapse']}),
        ('contactnumber', {'fields': ['contactnumber'],'classes': ['collapse']}),
        ('servicetype', {'fields': ['servicetype'],'classes': ['collapse']}),
        ('branchLocation', {'fields': ['branchLocation'],'classes': ['collapse']}),
        ('link', {'fields': ['link'],'classes': ['collapse']}),

    ]
    list_display = ('branchId','contactnumber','servicetype','branchLocation','address','salonId','link')


class SalonAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': ['salonId']}),
        ('name', {'fields': ['name'],'classes': ['name']}),
        ('image', {'fields': ['image'],'classes': ['collapse']}),
        # ('directionslink', {'fields': ['directionslink'],'classes': ['collapse']}),
    ]
    list_display = ('name','image','salonId')

class SalonDetailsSingleDealsAdmin_1(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': ['branchId']}),
        # ('branchId', {'fields': ['branchId'],'classes': ['collapse']}),
        ('Haircut', {'fields': ['Haircut'],'classes': ['collapse']}),
        ('Trimming', {'fields': ['Trimming'],'classes': ['collapse']}),
        ('Shave', {'fields': ['Shave'],'classes': ['collapse']}),
        ('BodyMassage', {'fields': ['BodyMassage'],'classes': ['collapse']}),
        ('HeadMassage', {'fields': ['HeadMassage'],'classes': ['collapse']}),
        ('Bleach', {'fields': ['Bleach'],'classes': ['collapse']}),
        ('Facial', {'fields': ['Facial'],'classes': ['collapse']}),
    ]
    list_display = ('branchId','Haircut','Trimming','Shave','BodyMassage','HeadMassage','Bleach','Facial')

class SalonDetailsComboDealsAdmin_1(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': ['branchId']}),
        # ('branchId', {'fields': ['branchId'],'classes': ['collapse']}),
        ('Haircut_and_more', {'fields': ['Haircut_and_more'],'classes': ['collapse']}),
        ('Facial_and_Detan', {'fields': ['Facial_and_Detan'],'classes': ['collapse']}),
        ('Bridal_packages', {'fields': ['Bridal_packages'],'classes': ['collapse']}),
        ('BodyMassage_and_steambath', {'fields': ['BodyMassage_and_steambath'],'classes': ['collapse']}),
        ('HeadMassage_and_conditioning', {'fields': ['HeadMassage_and_conditioning'],'classes': ['collapse']}),
        ]
    list_display = ('branchId','Haircut_and_more','Facial_and_Detan','Bridal_packages','BodyMassage_and_steambath','HeadMassage_and_conditioning')

class ExpertAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': ['Name']}),
        ('User_email', {'fields': ['User_email'],'classes': ['collapse']}),
        ('Postedquery', {'fields': ['Query'],'classes': ['collapse']}),
        ]
    list_display = ('Name','User_email','Postedquery')

class Reviews_ratingsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': ['Name']}),
        ('reviews', {'fields': ['reviews'],'classes': ['collapse']}),
        ('branchId', {'fields': ['branchId'],'classes': ['collapse']}),
        ]
    list_display = ('Name','reviews','branchId')

admin.site.register(Details, DetailsAdmin)
admin.site.register(Otp, OtpAdmin)
admin.site.register(Salon, SalonAdmin)
admin.site.register(SalonDetailsSingleDeals_1, SalonDetailsSingleDealsAdmin_1)
admin.site.register(SalonDetailsComboDeals_1, SalonDetailsComboDealsAdmin_1)
admin.site.register(SalonBranch_1, SalonBranch_1Admin)
admin.site.register(Expert, ExpertAdmin)
admin.site.register(Reviews_rating, Reviews_ratingsAdmin)



