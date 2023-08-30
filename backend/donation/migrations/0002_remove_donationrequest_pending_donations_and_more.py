# Generated by Django 4.2.4 on 2023-08-30 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donationrequest',
            name='pending_donations',
        ),
        migrations.RemoveField(
            model_name='donationrequest',
            name='verified_donations',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='donation_history',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='donation_targets',
        ),
        migrations.AddField(
            model_name='donationrequest',
            name='pending_donations',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pending_requests', to='donation.donation'),
        ),
        migrations.AddField(
            model_name='donationrequest',
            name='verified_donations',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='verified_requests', to='donation.donation'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='donation_history',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='donation.donation'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='donation_targets',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_profiles', to='donation.donationtarget'),
        ),
    ]