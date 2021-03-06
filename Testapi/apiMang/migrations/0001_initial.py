# Generated by Django 2.0.3 on 2019-12-25 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_name', models.CharField(max_length=20)),
                ('request', models.CharField(max_length=10)),
                ('url', models.CharField(max_length=100)),
                ('parameter', models.CharField(max_length=1000)),
                ('u_member', models.CharField(max_length=10)),
                ('expect_result', models.CharField(max_length=100)),
                ('reality_result', models.CharField(max_length=1000)),
                ('result', models.CharField(max_length=10)),
                ('status', models.IntegerField(max_length=10)),
                ('ctime', models.DateTimeField()),
                ('utime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=20)),
                ('sex', models.IntegerField(max_length=10)),
                ('status', models.IntegerField(max_length=10)),
                ('phone', models.IntegerField(max_length=100)),
                ('power', models.CharField(max_length=20)),
                ('e_mail', models.CharField(max_length=20)),
                ('ctime', models.DateTimeField()),
                ('utime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=20)),
                ('version', models.IntegerField(max_length=10)),
                ('ctime', models.DateTimeField()),
                ('utime', models.DateTimeField()),
                ('status', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='project_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('op_time', models.DateTimeField()),
                ('op_type', models.CharField(max_length=10)),
                ('op_member', models.CharField(max_length=10)),
                ('op_show', models.CharField(max_length=10)),
                ('status', models.IntegerField(max_length=10)),
                ('op_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiMang.project')),
            ],
        ),
        migrations.CreateModel(
            name='test_report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pass_num', models.IntegerField(max_length=5)),
                ('fail_num', models.IntegerField(max_length=5)),
                ('error_num', models.IntegerField(max_length=5)),
                ('test_time', models.DateTimeField()),
                ('ctime', models.DateTimeField()),
                ('status', models.IntegerField(max_length=10)),
                ('op_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiMang.project')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiMang.project'),
        ),
        migrations.AddField(
            model_name='case',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiMang.project'),
        ),
    ]
