# Generated by Django 2.0.7 on 2018-08-02 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20180801_0222'),
    ]

    operations = [
        migrations.CreateModel(
            name='SDCSsda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asd', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='text',
            field=models.CharField(max_length=200),
        ),
    ]
