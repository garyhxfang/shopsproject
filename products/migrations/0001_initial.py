# Generated by Django 3.2 on 2021-05-07 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SKU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('original_price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('for_sale', models.BooleanField(default=True)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('link', models.URLField()),
                ('main_pic', models.ImageField(blank=True, upload_to='image')),
                ('list_pic', models.ImageField(blank=True, upload_to='image')),
                ('detail_pic', models.ImageField(blank=True, upload_to='image')),
                ('back_topic', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SpecName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='SPU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('bg_pic', models.ImageField(blank=True, upload_to='image')),
                ('sort_weight', models.IntegerField()),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='TopicSKU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_weight', models.IntegerField()),
                ('sku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.sku')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.topic')),
            ],
        ),
        migrations.CreateModel(
            name='SpecOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=100)),
                ('spec_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.specname')),
                ('spu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.spu')),
            ],
        ),
        migrations.AddField(
            model_name='specname',
            name='spu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.spu'),
        ),
        migrations.CreateModel(
            name='SKUSpec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.specoption')),
                ('sku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.sku')),
                ('spec', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.specname')),
            ],
        ),
        migrations.AddField(
            model_name='sku',
            name='spu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='skus', to='products.spu'),
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_type', models.IntegerField(choices=[(1, 'product'), (2, 'topic')])),
                ('banner_pic', models.ImageField(blank=True, upload_to='image')),
                ('sort_weight', models.IntegerField()),
                ('sku', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='products.sku')),
                ('topic', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='products.topic')),
            ],
        ),
    ]
