# Generated by Django 2.1.2 on 2018-11-16 03:44

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('demographics', '0001_initial'),
        ('diseases', '0001_initial'),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('row_create_ts', model_utils.fields.AutoCreatedField(db_column='row_create_ts', default=django.utils.timezone.now, editable=False)),
                ('row_lup_ts', model_utils.fields.AutoLastModifiedField(db_column='row_lup_ts', default=django.utils.timezone.now, editable=False)),
                ('row_end_ts', models.DateTimeField(db_column='row_end_ts', default='9999-12-31 00:00:00.00000-00')),
                ('row_ef', models.BooleanField(db_column='row_ef', default=True)),
                ('row_create_usr_id', models.CharField(db_column='row_create_usr_id', default="'docker'", max_length=20)),
                ('row_lup_usr_id', models.CharField(db_column='row_lup_usr_id', default="'docker'", max_length=20)),
                ('activity_level', models.ForeignKey(db_column='activity_level_id', on_delete='PROTECT', to='demographics.ActivityLevel')),
                ('age_level', models.ForeignKey(db_column='age_level_id', on_delete='PROTECT', to='demographics.AgeLevel')),
                ('alcohol_status', models.ForeignKey(db_column='alcohol_status_id', on_delete='PROTECT', to='demographics.AlcoholStatus')),
                ('complication', models.ForeignKey(db_column='complication_id', on_delete='PROTECT', to='diseases.Complication')),
                ('disease', models.ForeignKey(db_column='disease_id', on_delete='PROTECT', to='diseases.Disease')),
                ('gender', models.ForeignKey(db_column='gender_id', on_delete='PROTECT', to='demographics.Gender')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('race', models.ForeignKey(db_column='race_id', on_delete='PROTECT', to='demographics.Race')),
                ('reading_level', models.ForeignKey(db_column='reading_level_id', on_delete='PROTECT', to='demographics.ReadingLevel')),
                ('smoking_status', models.ForeignKey(db_column='smoking_status_id', on_delete='PROTECT', to='demographics.SmokingStatus')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
