# Generated by Django 2.0.3 on 2018-03-28 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hwam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='softwareasset',
            name='domain_name',
            field=models.CharField(blank=True, max_length=48, null=True),
        ),
        migrations.AddField(
            model_name='softwareasset',
            name='hostname',
            field=models.CharField(blank=True, max_length=48, null=True),
        ),
        migrations.AddField(
            model_name='softwareasset',
            name='ip4_address_1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='softwareasset',
            name='ip4_address_2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='softwareasset',
            name='ip4_address_3',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='softwareasset',
            name='ip4_address_4',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='softwareasset',
            name='ip6_address_1',
            field=models.CharField(blank=True, max_length=42, null=True),
        ),
        migrations.AddField(
            model_name='softwareasset',
            name='ip6_address_2',
            field=models.CharField(blank=True, max_length=42, null=True),
        ),
        migrations.AddField(
            model_name='softwareasset',
            name='ip6_address_3',
            field=models.CharField(blank=True, max_length=42, null=True),
        ),
        migrations.AddField(
            model_name='softwareasset',
            name='ip6_address_4',
            field=models.CharField(blank=True, max_length=42, null=True),
        ),
        migrations.AlterField(
            model_name='softwareasset',
            name='package_name',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
