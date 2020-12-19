# Generated by Django 3.1.4 on 2020-12-19 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=64)),
                ('price', models.IntegerField()),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_id', to='appadmin.foodcategory')),
            ],
            options={
                'verbose_name_plural': 'Food Details',
            },
        ),
    ]