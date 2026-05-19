from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('tshirts', 'T-Shirts'), ('trackpants', 'Track Pants'), ('shorts', 'Shorts'), ('hoodies', 'Hoodies'), ('babies', 'Born Babies Garments')], max_length=50)),
                ('image', models.CharField(max_length=255)),
                ('title', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('is_featured', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-uploaded_at'],
            },
        ),
    ]
