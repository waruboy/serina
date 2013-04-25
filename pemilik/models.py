from django.db import models
from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser
)

class PemilikManager(BaseUserManager):
	def create_user(self, email, password=None):
		if not email:
			raise ValueError('Pemilik harus punya alamat email')

		user = self.model(
			email = PemilikManager.normalize_email(email),
			)
		
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password):
		user = self.create_user(email,
			password=password
		)
		user.is_admin = True
		return user

class Pemilik(AbstractBaseUser):
	email =  models.EmailField(
		verbose_name = 'alamat_email',
		max_length=255,
		unique=True,
		db_index=True,
	)
	tanggal_lahir = models.DateField(null=True, blank=True)
	nama = models.CharField(
		blank=True,
		max_length=255,
	)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	objects = PemilikManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	def get_full_name(self):
		if self.nama:
			return self.nama
		else:
			return self.email

	def get_short_name(self):
		if self.nama:
			return self.nama
		else:
			return self.email

	def __unicode__(self):
		if self.nama:
			return self.nama
		else:
			return self.email

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	@property 
	def is_staff(self):
		return self.is_admin


