# Generated by Django 2.2.11 on 2020-07-07 04:25

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_fields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cont',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=90)),
                ('phone', models.CharField(max_length=13)),
                ('desc', models.TextField()),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(blank=True, null=True, upload_to='images\\')),
                ('subject', models.CharField(max_length=200)),
                ('videofile', models.FileField(blank=True, null=True, upload_to='videos/', verbose_name='videofile')),
                ('msg', models.TextField(blank=True, null=True)),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('first_name', models.CharField(blank=True, max_length=12)),
                ('last_name', models.CharField(blank=True, max_length=12)),
                ('email', models.EmailField(max_length=150)),
                ('age', models.IntegerField(default=18, validators=[django.core.validators.MinValueValidator(18)])),
                ('address', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('single', 'single'), ('married', 'married'), ('widow', 'widow'), ('seprated', 'seprated'), ('commited', 'commited')], default='single', max_length=20)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='female', max_length=20)),
                ('phone_no', models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator('^0?[5-9]{1}\\d{9}$')])),
                ('description', models.TextField(blank=True, null=True)),
                ('pic', django_fields.fields.DefaultStaticImageField(blank=True, default='Download/un.jpg', upload_to='Download\\')),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('signup_confirmation', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('liked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.MyProfile')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.MyPost')),
            ],
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.TextField()),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('flag', models.CharField(blank=True, choices=[('racist', 'racist'), ('abbusing', 'abbusing')], max_length=20, null=True)),
                ('commented_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.MyProfile')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.MyPost')),
            ],
        ),
        migrations.AddField(
            model_name='mypost',
            name='uploaded_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='social.MyProfile'),
        ),
        migrations.CreateModel(
            name='FollowUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed_by', to='social.MyProfile')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='social.MyProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('commented_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.MyProfile')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='social.Comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='social.MyPost')),
            ],
        ),
    ]