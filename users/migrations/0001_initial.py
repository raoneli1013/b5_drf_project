# Generated by Django 4.2.1 on 2023-05-14 13:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=255, unique=True, verbose_name="email address"
                    ),
                ),
                ("password", models.CharField(max_length=256, verbose_name="비밀번호")),
                (
                    "username",
                    models.CharField(max_length=100, unique=True, verbose_name="이름"),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female")],
                        max_length=1,
                        verbose_name="성별",
                    ),
                ),
                ("date_of_birth", models.DateField(null=True, verbose_name="생년월일")),
                (
                    "introduction",
                    models.TextField(blank=True, null=True, verbose_name="자기소개"),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, upload_to="profile/%Y/%m/", verbose_name="프로필 이미지"
                    ),
                ),
                (
                    "preference",
                    models.CharField(
                        blank=True, max_length=256, null=True, verbose_name="선호 음료"
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("is_admin", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "followings",
                    models.ManyToManyField(
                        blank=True,
                        related_name="followers",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]