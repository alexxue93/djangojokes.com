# Generated by Django 5.0.3 on 2024-03-30 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0006_alter_category_options_joke_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['category'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='joke',
            name='slug',
            field=models.SlugField(default=1, editable=False, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='joke',
            name='tags',
            field=models.ManyToManyField(blank=True, to='jokes.tag'),
        ),
    ]
