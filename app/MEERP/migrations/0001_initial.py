# Generated by Django 3.2.6 on 2021-10-12 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerformanceReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UserStudent',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('SL', models.CharField(default='', max_length=50)),
                ('DNID', models.CharField(default='student', max_length=50)),
                ('DATE_OF_AD', models.CharField(default='', max_length=50)),
                ('COLLAGE_ID', models.CharField(default='', max_length=50)),
                ('BORD_ROLL', models.CharField(default='', max_length=50)),
                ('REGISTRATION_NUMBER', models.CharField(default='', max_length=50)),
                ('MOBILE_NO_STUDENT', models.CharField(default='', max_length=50)),
                ('FATHERS_NAME', models.CharField(default='', max_length=50)),
                ('MOTHERS_NAME', models.CharField(default='', max_length=50)),
                ('FATHER_MOBILE', models.CharField(default='', max_length=50)),
                ('MOTHERS_MOBILE', models.CharField(default='', max_length=50)),
                ('ADDRESS_PARMANENT', models.CharField(default='', max_length=50)),
                ('ADDRESS_LOCAL', models.CharField(default='', max_length=50)),
                ('SSC_YEAR', models.CharField(default='', max_length=50)),
                ('GROUP', models.CharField(default='', max_length=50)),
                ('BORD', models.CharField(default='', max_length=50)),
                ('GPA', models.CharField(default='', max_length=50)),
                ('SCAND_COPY_OF_MARK_SHEET', models.FileField(default='static/logo/logo.png', upload_to='static/student/SCAND_COPY_OF_MARK_SHEET')),
                ('SCAND_COPY_OF_TESTMONIAL', models.FileField(default='static/logo/logo.png', upload_to='static/student/SCAND_COPY_OF_TESTMONIAL')),
                ('DATE_OF_BIRTH', models.CharField(default='', max_length=50)),
                ('RELIGION', models.CharField(default='', max_length=50)),
                ('GENDER', models.CharField(default='', max_length=50)),
                ('District', models.CharField(default='', max_length=50)),
                ('Upazila_OR_Thana', models.CharField(default='', max_length=50)),
                ('SCHOOL', models.CharField(default='', max_length=50)),
                ('ADMITION_FEE', models.CharField(default='', max_length=50)),
                ('TUTION_FEE', models.CharField(default='', max_length=50)),
                ('SEMISTER_FEE', models.CharField(default='', max_length=50)),
                ('TOTAL_CONCRACT', models.CharField(default='', max_length=50)),
                ('PICTURE_STUDENT', models.FileField(default='static/logo/logo.png', upload_to='static/student/PICTURE_STUDENT')),
                ('Refferred_By', models.CharField(default='', max_length=50)),
                ('Refferrer_Number', models.CharField(default='', max_length=20)),
                ('Gurdian_Name', models.CharField(default='', max_length=50)),
                ('Gurdian_Relation', models.CharField(default='', max_length=50)),
                ('Father_NID', models.CharField(default='', max_length=50)),
                ('Mother_NID', models.CharField(default='', max_length=50)),
                ('Student_NID_or_Birth_Crtificate', models.CharField(default='', max_length=50)),
                ('Confirm', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserTeacher',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('NAME', models.CharField(default='', max_length=50)),
                ('DESIGNATION', models.CharField(default='', max_length=100)),
                ('DEPARTMENT', models.CharField(default='', max_length=100)),
                ('DATE_OF_JOINING', models.CharField(default='', max_length=50)),
                ('ACADEMIC_QUALIFICATION', models.CharField(default='', max_length=50)),
                ('EXPERIENCE', models.CharField(default='', max_length=50)),
                ('DNID', models.CharField(default='teacher', max_length=50)),
                ('GENDER', models.CharField(default='', max_length=50)),
                ('VOTER_ID_SMART', models.CharField(default='', max_length=50)),
                ('DATE_OF_BIRTH', models.CharField(default='', max_length=50)),
                ('ADDRESS', models.CharField(default='', max_length=200)),
                ('MOBILE_NO_OFFICE', models.CharField(default='', max_length=50)),
                ('MOBILE_NO_PERSINAL', models.CharField(default='', max_length=50)),
                ('EMAIL', models.CharField(default='', max_length=50)),
                ('BIO_DATA', models.CharField(default='', max_length=50)),
                ('IMAGE_1ST', models.FileField(default='static/logo/logo.png', upload_to='static/techerprode/IMAGE_1ST')),
                ('IMAGE_2ND', models.FileField(default='static/logo/logo.png', upload_to='static/techerprode/IMAGE_2ND')),
                ('SCAND_COPY_OF_NID', models.FileField(default='static/logo/logo.png', upload_to='static/techerprode/SCAND_COPY_OF_NIDstatic/')),
                ('ALL_OF_YOUR_CERTIFICATE', models.FileField(default='static/logo/logo.png', upload_to='static/techerprode/ALL_OF_YOUR_CERTIFICATE')),
            ],
        ),
        migrations.CreateModel(
            name='Wellwisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Phone_Number', models.CharField(max_length=50)),
                ('Profation', models.CharField(max_length=50)),
                ('Designation', models.CharField(max_length=50)),
                ('Admit_Student', models.CharField(max_length=50)),
                ('Paid', models.CharField(max_length=50)),
                ('Comment', models.TextField()),
                ('Last_talk', models.CharField(max_length=50)),
                ('Zila', models.CharField(max_length=50)),
                ('Thana_or_Upozila', models.CharField(max_length=50)),
            ],
        ),
    ]
