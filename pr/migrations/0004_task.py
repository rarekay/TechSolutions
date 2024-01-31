# Generated by Django 4.2.7 on 2023-11-27 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pr', '0003_alter_fruit_created_at_alter_fruit_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('completed', models.BooleanField(default=False)),
                ('created_at', models.DateField(default='YY-MM-DD')),
            ],
        ),
    ]