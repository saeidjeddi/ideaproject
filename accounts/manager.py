from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email,username,phone, password=None):

        if not email:
            raise ValueError("Users must have an email address")
        
        if not username:
            raise ValueError("Users must have an username")
        
        if not phone:
            raise ValueError("Users must have an Phone")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username, phone, password=None):

        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            phone=phone,
            password=password,

        )
        user.is_admin = True
        user.save(using=self._db)
        return user

