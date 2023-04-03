from django.contrib.auth.base_user import BaseUserManager


class MyAccountManager(BaseUserManager):
    """
       Custom user model manager where email is the unique identifiers
       for authentication instead of usernames.
    """
    def create_user(self, email, firstname, lastname, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if not firstname:
            raise ValueError('Users must have a firstname')
        if not lastname:
            raise ValueError('Users must have a lastname')

        user = self.model(
            firstname=firstname,
            lastname=lastname,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, firstname, lastname, email, password=None):
        user = self.create_user(
            firstname=firstname,
            lastname=lastname,
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


