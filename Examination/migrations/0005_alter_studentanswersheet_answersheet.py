# Generated by Django 3.2.10 on 2022-04-11 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Examination', '0004_invigilagtor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentanswersheet',
            name='answersheet',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Examination.answersheet'),
        ),
    ]
