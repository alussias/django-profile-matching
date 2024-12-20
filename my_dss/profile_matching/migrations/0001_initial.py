# Generated by Django 4.1.2 on 2024-11-28 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cagur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('telp', models.CharField(max_length=255)),
                ('Pendidikan', models.CharField(max_length=255)),
                ('IPK', models.CharField(max_length=255)),
                ('Umur', models.CharField(max_length=255)),
                ('Psikotes', models.CharField(max_length=255)),
                ('Pengalaman_Mengajar', models.CharField(max_length=255)),
                ('Sertifikasi_Keahlian', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Gap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gap', models.IntegerField()),
                ('bobot_nilai', models.DecimalField(decimal_places=1, max_digits=8)),
                ('keterangan', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Kriteria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('jenis', models.CharField(choices=[('Core Factor', 'Core Factor'), ('Secondary Factor', 'Secondary Factor')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('cagur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='profile_matching.cagur')),
                ('total_nilai', models.DecimalField(decimal_places=4, max_digits=8)),
                ('rank', models.SmallIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubKriteria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=255)),
                ('nilai', models.SmallIntegerField()),
                ('selected', models.BooleanField()),
                ('kriteria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_kriteria', to='profile_matching.kriteria')),
            ],
        ),
        migrations.CreateModel(
            name='PerhitunganGap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ideal_profil', models.IntegerField()),
                ('gap', models.IntegerField()),
                ('bobot_gap', models.DecimalField(decimal_places=1, max_digits=8)),
                ('cagur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_matching.cagur')),
                ('sub_kriteria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_matching.subkriteria')),
            ],
            options={
                'unique_together': {('cagur', 'sub_kriteria')},
            },
        ),
        migrations.CreateModel(
            name='PerhitunganAkhir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jumlah_nilai', models.DecimalField(decimal_places=1, max_digits=8)),
                ('rata_rata', models.DecimalField(decimal_places=4, max_digits=8)),
                ('total_rata_rata', models.DecimalField(decimal_places=4, max_digits=8)),
                ('cagur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_matching.cagur')),
                ('sub_kriteria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_matching.subkriteria')),
            ],
            options={
                'unique_together': {('cagur', 'sub_kriteria')},
            },
        ),
        migrations.CreateModel(
            name='NilaiProfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nilai_profil', models.PositiveIntegerField()),
                ('cagur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_matching.cagur')),
                ('kriteria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_matching.kriteria')),
                ('sub_kriteria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_matching.subkriteria')),
            ],
            options={
                'unique_together': {('cagur', 'kriteria', 'sub_kriteria')},
            },
        ),
        migrations.CreateModel(
            name='IdealProfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nilai_ideal', models.PositiveIntegerField()),
                ('kriteria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_matching.kriteria')),
                ('sub_kriteria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_matching.subkriteria')),
            ],
            options={
                'unique_together': {('kriteria', 'sub_kriteria')},
            },
        ),
    ]
