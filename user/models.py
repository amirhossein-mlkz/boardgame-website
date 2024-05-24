from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser



class userManager(BaseUserManager):
    def create_user(self, phone_number, firstname, lastname, password=None):
        """
        Creates and saves a User with the given phone numbe, date of
        birth and password.
        """
        if not phone_number:
            raise ValueError("Users must have n phone number address")

        self.model = User

        user = self.model(
            phone_number=phone_number,
            firstname = firstname,
            lastname= lastname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, firstname, lastname, password=None):
        """
        Creates and saves a superuser with the given phone,
        """
        user = self.create_user(
            phone_number,
            firstname=firstname,
            lastname= lastname
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    firstname = models.CharField( max_length=50)
    lastname = models.CharField( max_length=50)
    phone_number = models.CharField( max_length=50, unique=True)
    last_login = models.DateTimeField(auto_now=True)
    joinied_date = models.DateTimeField(auto_now_add=True)
    bio = models.CharField(max_length=500, blank = True, null=True)

    #Show account is active or not. it is better deactive instead of delete beacuse of foriegin key
    is_active = models.BooleanField(default=True)
    #show this user can access to admin panel
    is_staff = models.BooleanField(default=False)
    #treats this user as having all permissions 
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['firstname', 'lastname',]

    objects = userManager()

    def __str__(self):
        return self.firstname + ' ' + self.lastname

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin