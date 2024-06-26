# Generated by Django 5.0.4 on 2024-05-01 19:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                ("profile_id", models.AutoField(primary_key=True, serialize=False)),
                ("phone_number", models.CharField(max_length=16)),
                ("address", models.CharField(max_length=255)),
                (
                    "social_media",
                    models.CharField(
                        choices=[
                            ("X", "X"),
                            ("Facebook", "Facebook"),
                            ("Instagram", "Instagram"),
                            ("LinkedIn", "LinkedIn"),
                            ("Others", "Others"),
                        ],
                        max_length=90,
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("Male", "Male"),
                            ("Female", "Female"),
                            ("I had rather not say", "I had rather not say"),
                            ("LGBTQ", "LGBTQ"),
                            ("Others", "Others"),
                        ],
                        max_length=250,
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        choices=[
                            ("Angola", "Angola"),
                            ("Canada", "Canada"),
                            ("Kamataj", "Kamataj"),
                            ("Nigeria", "Nigeria"),
                            ("United Kingdom", "United Kingdom"),
                            ("United States of America", "United States of America"),
                            ("Others", "Others"),
                        ],
                        max_length=60,
                    ),
                ),
                (
                    "followers",
                    models.CharField(
                        choices=[
                            ("0001-4999", "0001-4999"),
                            ("5000-9999", "5000-9999"),
                            ("10_000-50_000", "10_000-50_000"),
                            ("50k Above", "50k Above"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "profile_view",
                    models.ImageField(null=True, upload_to="Profile_view_images/"),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
