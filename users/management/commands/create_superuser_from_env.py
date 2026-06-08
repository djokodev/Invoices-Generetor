from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
import os


class Command(BaseCommand):
    help = "Create a superuser from environment variables if it does not already exist."

    def handle(self, *args, **options):
        User = get_user_model()
        email = os.getenv("DJANGO_SUPERUSER_EMAIL")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD")
        first_name = os.getenv("DJANGO_SUPERUSER_FIRST_NAME", "").strip()
        last_name = os.getenv("DJANGO_SUPERUSER_LAST_NAME", "").strip()

        if not email:
            raise CommandError("DJANGO_SUPERUSER_EMAIL is required.")

        if not password:
            raise CommandError("DJANGO_SUPERUSER_PASSWORD is required.")

        user, created = User.objects.get_or_create(
            email=email,
            defaults={
                "first_name": first_name,
                "last_name": last_name,
                "is_staff": True,
                "is_superuser": True,
            },
        )

        if created:
            user.set_password(password)
            user.is_staff = True
            user.is_superuser = True
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            self.stdout.write(self.style.SUCCESS(f"Superuser created for {email}."))
            return

        updated = False
        if first_name and user.first_name != first_name:
            user.first_name = first_name
            updated = True
        if last_name and user.last_name != last_name:
            user.last_name = last_name
            updated = True
        if not user.check_password(password):
            user.set_password(password)
            updated = True
        if not user.is_staff:
            user.is_staff = True
            updated = True
        if not user.is_superuser:
            user.is_superuser = True
            updated = True

        if updated:
            user.save()
            self.stdout.write(self.style.SUCCESS(f"Superuser updated for {email}."))
        else:
            self.stdout.write(self.style.SUCCESS(f"Superuser already exists for {email}."))
