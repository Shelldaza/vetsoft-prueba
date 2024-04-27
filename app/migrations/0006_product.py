from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [   ('app', '0005_medicine_provider')
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('price', models.FloatField()),
            ],
        ),
    ]