# Generated by Django 2.2 on 2020-06-24 04:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tsunami',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('have_water_bodies', models.BooleanField()),
                ('house_kind', models.CharField(blank=True, max_length=16)),
                ('have_alarm_system', models.BooleanField()),
                ('have_elevated_area', models.BooleanField()),
                ('have_maps', models.BooleanField()),
                ('have_learnt_signs', models.BooleanField()),
                ('have_shelters', models.BooleanField()),
                ('have_contact', models.BooleanField()),
                ('have_health', models.BooleanField()),
                ('have_specials', models.BooleanField()),
                ('have_latest_prescriptions', models.BooleanField()),
                ('near_home', models.TextField(blank=True, default='NA')),
                ('have_higher_ground', models.TextField(blank=True, default='NA')),
                ('provide_reg_contact', models.TextField(blank=True, default='NA')),
                ('provide_phy_contact', models.TextField(blank=True, default='NA')),
                ('have_car_insu_up', models.BooleanField()),
                ('response', models.TextField(default='')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Terrorism',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.TextField(blank=True)),
                ('dist', models.TextField(blank=True)),
                ('loc', models.TextField(blank=True)),
                ('count_people', models.IntegerField()),
                ('have_infant', models.BooleanField()),
                ('have_school_kids', models.BooleanField()),
                ('have_specials', models.BooleanField()),
                ('specify_specials', models.TextField(blank=True)),
                ('have_emerg', models.BooleanField()),
                ('three_emg_name_num', models.TextField(blank=True)),
                ('have_shelter', models.BooleanField()),
                ('have_inventory', models.BooleanField()),
                ('have_emg_kits', models.BooleanField()),
                ('have_add_kits', models.TextField(blank=True)),
                ('docs', models.TextField(blank=True)),
                ('have_plan_school', models.BooleanField()),
                ('have_evac_plans', models.BooleanField()),
                ('response', models.TextField()),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Riot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_family_members', models.IntegerField(default=5)),
                ('have_infants', models.BooleanField(default=False)),
                ('have_senior_citizens', models.BooleanField(default=False)),
                ('have_existing_medical_conditions', models.BooleanField(default=False)),
                ('backpack', models.BooleanField(default=False)),
                ('sunglasses', models.BooleanField(default=False)),
                ('pepper_spray', models.BooleanField(default=False)),
                ('flash_light', models.BooleanField(default=False)),
                ('cash', models.BooleanField(default=False)),
                ('mylar_blanket', models.BooleanField(default=False)),
                ('radio_app', models.BooleanField(default=False)),
                ('survival_manuals', models.BooleanField(default=False)),
                ('bandana', models.BooleanField(default=False)),
                ('have_disability', models.BooleanField(default=False)),
                ('disability_description', models.TextField(blank=True)),
                ('have_prescriptions', models.BooleanField(default=False)),
                ('have_dependable_medium', models.BooleanField(default=False)),
                ('knows_to_drive', models.BooleanField(default=False)),
                ('another_location', models.BooleanField(default=False)),
                ('have_emergency_helpline', models.BooleanField(default=False)),
                ('children_remember', models.BooleanField(default=False)),
                ('medical_supplies', models.BooleanField(default=False)),
                ('life_insurance', models.BooleanField(default=False)),
                ('mock_drills', models.BooleanField(default=False)),
                ('response', models.TextField(default='')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Flood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('near_water_bodies', models.BooleanField()),
                ('house_kind', models.CharField(max_length=30)),
                ('emergency_evac', models.TextField(blank=True)),
                ('have_higher_ground', models.BooleanField()),
                ('flood_risk', models.BooleanField()),
                ('have_signed', models.BooleanField()),
                ('provide_reg_contact', models.TextField(blank=True)),
                ('provide_phy_contact', models.TextField(blank=True)),
                ('have_health', models.BooleanField()),
                ('have_car_insu_up', models.BooleanField()),
                ('have_evac_routes', models.BooleanField()),
                ('have_kits', models.BooleanField()),
                ('have_safe_doc', models.BooleanField()),
                ('have_flood', models.BooleanField()),
                ('have_elv_shelters', models.BooleanField()),
                ('have_specials', models.BooleanField()),
                ('to_drive', models.BooleanField()),
                ('clean_gutter', models.BooleanField()),
                ('have_comm_plan', models.BooleanField()),
                ('kids_know', models.BooleanField()),
                ('response', models.TextField()),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Earthquake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house', models.CharField(blank=True, max_length=16)),
                ('structure', models.CharField(blank=True, max_length=16)),
                ('field', models.CharField(blank=True, max_length=16)),
                ('furniture', models.CharField(blank=True, max_length=16)),
                ('disaster_plan', models.CharField(blank=True, max_length=16)),
                ('place', models.CharField(blank=True, max_length=16)),
                ('cracks', models.CharField(blank=True, max_length=16)),
                ('combustible', models.TextField(blank=True)),
                ('safe_places', models.CharField(blank=True, max_length=16)),
                ('contact', models.TextField(blank=True)),
                ('fire_extin', models.BooleanField(default=False)),
                ('first_aid', models.BooleanField(default=False)),
                ('flashlight', models.BooleanField(default=False)),
                ('documents', models.CharField(blank=True, max_length=16)),
                ('cash', models.CharField(blank=True, max_length=16)),
                ('safe', models.CharField(blank=True, max_length=16)),
                ('health_policies', models.CharField(blank=True, max_length=16)),
                ('physician', models.TextField(blank=True)),
                ('disability', models.TextField(blank=True)),
                ('infants_and_senior_citizens', models.CharField(blank=True, max_length=16)),
                ('gas', models.CharField(blank=True, max_length=16)),
                ('emergency_numbers', models.CharField(blank=True, max_length=16)),
                ('parked', models.CharField(blank=True, max_length=16)),
                ('car_insurance', models.CharField(blank=True, max_length=16)),
                ('pets', models.CharField(blank=True, max_length=16)),
                ('basement', models.CharField(blank=True, max_length=16)),
                ('ammo', models.CharField(blank=True, max_length=16)),
                ('repairs', models.CharField(blank=True, max_length=16)),
                ('blueprint', models.CharField(blank=True, max_length=16)),
                ('response', models.TextField(default='')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CyberCrime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('at_work', models.BooleanField()),
                ('at_home', models.BooleanField()),
                ('have_secure_connections', models.BooleanField()),
                ('have_action_plan', models.BooleanField()),
                ('how_to_know_risk', models.BooleanField()),
                ('have_shared_card', models.BooleanField()),
                ('identify_phishing', models.BooleanField()),
                ('third_party', models.TextField(blank=True)),
                ('security_policies', models.BooleanField()),
                ('have_recovery_plan', models.BooleanField()),
                ('have_redun', models.BooleanField()),
                ('perform_bgcheck', models.BooleanField()),
                ('perform_audit', models.BooleanField()),
                ('have_cyber_insu', models.BooleanField()),
                ('have_sec_plan', models.BooleanField()),
                ('have_trained', models.BooleanField()),
                ('have_IRP', models.BooleanField()),
                ('response', models.TextField(default='')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
