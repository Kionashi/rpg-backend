# Generated by Django 4.2.1 on 2023-06-09 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0002_skill_duration_skill_side_effect_skill_id_skill_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='exp',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='character',
            name='image',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='npc',
            name='image',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]