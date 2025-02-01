# Generated by Django 5.1.5 on 2025-02-01 11:12

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'faqs',
            },
        ),
    ]
