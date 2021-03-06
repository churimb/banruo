# Generated by Django 2.1.15 on 2020-01-06 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='nmapscan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
                ('scantime', models.DateTimeField(auto_now=True)),
                ('rate', models.CharField(max_length=100, null=True)),
                ('endtime', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='scan_ip_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('product', models.CharField(max_length=100)),
                ('cpe', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='scanIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='scanlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ips', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='scantask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ip', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('scantime', models.DateTimeField(auto_now=True)),
                ('endtime', models.DateTimeField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='scan_ip_info',
            name='ipfor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.scanIP'),
        ),
        migrations.AddField(
            model_name='nmapscan',
            name='taskid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.scantask'),
        ),
    ]
