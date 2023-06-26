# Generated by Django 4.2.1 on 2023-06-09 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='duration',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='skill',
            name='side_effect_skill_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rpg.skill'),
        ),
        migrations.AddField(
            model_name='skill',
            name='type',
            field=models.CharField(choices=[('damage', 'Damage'), ('heal', 'Heal'), ('buff', 'Buff'), ('debuff', 'Debuff')], default='damage', max_length=6),
        ),
        migrations.AlterField(
            model_name='race',
            name='dex_growth',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='race',
            name='hp_growth',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='race',
            name='int_growth',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='race',
            name='mp_growth',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='race',
            name='str_growth',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='skill',
            name='level_required',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]