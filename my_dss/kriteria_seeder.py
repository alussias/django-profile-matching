from datetime import timezone
from profile_matching.models import Kriteria

data = [
    {
            'nama': 'Pendidikan',
            'jenis': 'Core Factor',
            'created_at': timezone.now(),
            'updated_at': timezone.now(),
        },
        {
            'nama': 'IPK',
            'jenis': 'Core Factor',
            'created_at': timezone.now(),
            'updated_at': timezone.now(),
        },
        {
            'nama': 'Pengalaman_Mengajar',
            'jenis': 'Core Factor',
            'created_at': timezone.now(),
            'updated_at': timezone.now(),
        },
        {
            'nama': 'Umur',
            'jenis': 'Secondary Factor',
            'created_at': timezone.now(),
            'updated_at': timezone.now(),
        },
        {
            'nama': 'Psikotes',
            'jenis': 'Secondary Factor',
            'created_at': timezone.now(),
            'updated_at': timezone.now(),
        },
        {
            'nama': 'Sertifikasi_Keahlian',
            'jenis': 'Secondary Factor',
            'created_at': timezone.now(),
            'updated_at': timezone.now(),
        },
]

for item in data:
    Kriteria.objects.create(**item)
