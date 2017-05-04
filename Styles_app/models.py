from django.db import models
from django.db import IntegrityError
from PIL import Image

# Create your models here.
class Details(models.Model):
	firstname = models.CharField(max_length=50,blank=False,default=None)
	lastname = models.CharField(max_length=50,blank=False,default=None)
	username = models.CharField(max_length=20, unique=True)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=20)
	mobilenumber = models.CharField(max_length=15, unique = True)
	address = models.CharField(max_length=500)
	registered = models.BooleanField(default = False)
	def __str__(self):
		return self.username

class Otp(models.Model):
	otp = models.CharField(max_length=20)
	mail = models.EmailField()



class Salon(models.Model):
	salonId = models.CharField(primary_key=True,max_length=20)
	name = models.CharField(max_length=50,blank=False,default=None)
	image = models.ImageField(upload_to='image')
	
	# branchId = models.ForeignKey(Branch, on_delete=models.CASCADE)	
	def __str__(self):
		return self.salonId

class SalonBranch_1(models.Model):
	branchId = models.CharField(max_length=100, unique=True, primary_key=True, blank=True)
	salonId = models.ForeignKey(Salon, on_delete=models.CASCADE)
	branchLocation = models.CharField(max_length=20, unique = False, default=None)
	address = models.CharField(max_length=50,blank=False,default=None)
	contactnumber = models.CharField(max_length=20, unique=True)
	servicetype = models.CharField(max_length=50)
	link = models.URLField(blank=False, null=True,max_length=500)

	def __str__( self ):
		return self.branchId

class SalonDetailsSingleDeals_1(models.Model):
	# salonId = models.ForeignKey(Salon, on_delete=models.CASCADE)
	branchId = models.ForeignKey(SalonBranch_1, on_delete=models.CASCADE)	
	Haircut = models.CharField(max_length=20, unique=False)
	Trimming = models.CharField(max_length=20, unique=False)
	Shave = models.CharField(max_length=20, unique=False)
	BodyMassage = models.CharField(max_length=20, unique=False)
	HeadMassage = models.CharField(max_length=20, unique=False)
	Bleach = models.CharField(max_length=20, unique=False)
	Facial = models.CharField(max_length=20, unique=False)

class SalonDetailsComboDeals_1(models.Model):
	# salonId = models.ForeignKey(Salon, on_delete=models.CASCADE)
	branchId = models.ForeignKey(SalonBranch_1, on_delete=models.CASCADE)	
	Haircut_and_more = models.CharField(max_length=20, unique=False)
	Facial_and_Detan = models.CharField(max_length=20, unique=False)
	Bridal_packages = models.CharField(max_length=20, unique=False)
	BodyMassage_and_steambath = models.CharField(max_length=20, unique=False)
	HeadMassage_and_conditioning = models.CharField(max_length=20, unique=False)

class Expert(models.Model):
    Name = models.CharField(max_length=30)
    Postedquery = models.CharField(max_length=400)
    User_email = models.EmailField()

class Reviews_rating(models.Model):
    Name = models.CharField(max_length=400)
    reviews = models.CharField(max_length=800)
    branchId = models.ForeignKey(SalonBranch_1, on_delete=models.CASCADE)

    



		

