# Generated by Django 2.2 on 2020-06-26 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('disaster', '0003_auto_20200626_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='NuclearWar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.TextField(blank=True, default='NA')),
                ('dist', models.TextField(blank=True, default='NA')),
                ('loc', models.TextField(blank=True, default='NA')),
                ('count_people', models.CharField(blank=True, max_length=16)),
                ('have_infant', models.BooleanField()),
                ('have_specials', models.TextField(blank=True, default='NA')),
                ('have_policies', models.BooleanField()),
                ('have_hard_cpy', models.BooleanField()),
                ('have_base', models.BooleanField()),
                ('have_brick_shelter', models.BooleanField()),
                ('have_media', models.BooleanField()),
                ('Water', models.BooleanField()),
                ('Food', models.BooleanField()),
                ('radio', models.BooleanField()),
                ('Flashlight', models.BooleanField()),
                ('First_aid_kit', models.BooleanField()),
                ('Extra_batteries', models.BooleanField()),
                ('Whistle', models.BooleanField()),
                ('Dust_mask', models.BooleanField()),
                ('Plastic_sheeting', models.BooleanField()),
                ('Moist_towelettes', models.BooleanField()),
                ('Wrench', models.BooleanField()),
                ('Manual_can_opener', models.BooleanField()),
                ('Local_maps', models.BooleanField()),
                ('Cell_phone', models.BooleanField()),
                ('have_add_kits', models.BooleanField()),
                ('have_switch_board', models.BooleanField()),
                ('have_school_base', models.BooleanField()),
                ('have_schl_brick', models.BooleanField()),
                ('have_conduct_drill', models.BooleanField()),
                ('have_shelter_plan', models.BooleanField()),
                ('have_nuclear_kit', models.BooleanField()),
                ('response', models.TextField(default='')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('have_esc_plan', models.BooleanField()),
                ('have_seniors', models.BooleanField()),
                ('have_smoke_det', models.BooleanField()),
                ('have_smoke_det_out_bed', models.BooleanField()),
                ('have_discuss_out', models.BooleanField()),
                ('count_exits', models.CharField(blank=True, max_length=16)),
                ('have_fire_extin', models.BooleanField()),
                ('have_maint_check', models.BooleanField()),
                ('have_pets', models.BooleanField()),
                ('have_policy', models.BooleanField()),
                ('have_kit', models.BooleanField()),
                ('response', models.TextField(default='')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]