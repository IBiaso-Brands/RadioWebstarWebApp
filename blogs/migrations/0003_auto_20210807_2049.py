# Generated by Django 3.2.6 on 2021-08-07 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20210807_2034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogsection',
            old_name='blog_id',
            new_name='blog',
        ),
        migrations.RenameField(
            model_name='blogsummary',
            old_name='blog_id',
            new_name='blog',
        ),
        migrations.RenameField(
            model_name='sectionparagraph',
            old_name='section_id',
            new_name='section',
        ),
        migrations.RenameField(
            model_name='summaryparagraph',
            old_name='summary_id',
            new_name='summary',
        ),
    ]