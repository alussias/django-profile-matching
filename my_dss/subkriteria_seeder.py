from datetime import timezone
from profile_matching.models import SubKriteria

data = [
    {'id_k': 1, 'desc': 'D3', 'nilai': 0, 'selected': False, 'created_at': timezone.now(), 'updated_at': timezone.now()},
    {'id_k': 1, 'desc': 'D4/S1', 'nilai': 2, 'selected': True, 'created_at': timezone.now(), 'updated_at': timezone.now()},
    {'id_k': 1, 'desc': 'S2', 'nilai': 3, 'selected': False, 'created_at': timezone.now(), 'updated_at': timezone.now()},
    {'id_k': 1, 'desc': 'S3', 'nilai': 4, 'selected': False, 'created_at': timezone.now(), 'updated_at': timezone.now()},
    {'id_k': 2, 'desc': '<2', 'nilai': 0, 'selected': False, 'created_at': timezone.now(), 'updated_at': timezone.now()},
    {'id_k': 2, 'desc': '>=2 dan <2.5', 'nilai': 1, 'selected': False, 'created_at': timezone.now(), 'updated_at': timezone.now()},
    {'id_k': 2, 'desc': '>2.5 dan <3', 'nilai': 2, 'selected': False, 'created_at': timezone.now(), 'updated_at': timezone.now()},
    {'id_k': 2, 'desc': '>3 dan <3.5', 'nilai': 3, 'selected': False, 'created_at': timezone.now(), 'updated_at': timezone.now()},
    {'id_k': 2, 'desc': '>=3.5', 'nilai': 4, 'selected': True, 'created_at': timezone.now(), 'updated_at': timezone.now()},
    {'id_k': 3, 'desc': '<2 Tahun', 'nilai': 1, 'selected': False, 'created_at': timezone.now(), 'updated_at': timezone.now()},
    {'id_k': 3, 'desc': '>=2 dan <3 Tahun', 'nilai': 2, 'selected': True, 'created_at': timezone.now(), 'updated_at': timezone.now()},
    {'id_k': 3, 'desc': '>=3 dan <4 Tahun', 'nilai': 3, 'selected': False, 'created_at': timezone.now(), 'updated_at': timezone.now()},
    {'id_k': 3, 'desc': '>=4 Tahun', 'nilai': 4, 'selected': False, 'created_at': timezone.now(), 'updated_at': timezone.now()},
    {'id_k': 4, 'desc': '<25 Tahun', 'nilai': 0, 'selected': False, 'created_at': timezone.now(), 'updated_at': timezone.now()},
    {'id_k': 4, 'desc': '25-28 Tahun', 'nilai': 1, 'selected': True, 'created_at': timezone.now(), 'updated_at': timezone.now()},
    {'id_k': 4, 'desc': '29-32 Tahun', 'nilai': 2, 'selected': False, 'created_at': timezone.now(), 'updated_at': timezone.now()},
    {'id_k': 4, 'desc': '32-35 Tahun', 'nilai': 3, 'selected': False, 'created_at': timezone.now(), 'updated_at': timezone.now()},
    {'id_k': 4, 'desc': '>32 Tahun', 'nilai': 4, 'selected': False, 'created_at': timezone.now(), 'updated_at': timezone.now()},
    {'id_k': 5, 'desc': '0-40', 'nilai': 0, 'selected': False, 'created_at': timezone.now(), 'updated_at': timezone.now()},
    {'id_k': 5, 'desc': '41-60', 'nilai': 1, 'selected': True, 'created_at': timezone.now(), 'updated_at': timezone.now()},
    {'id_k': 5, 'desc': '61-80', 'nilai': 3, 'selected': False, 'created_at': timezone.now(), 'updated_at': timezone.now()},
    {'id_k': 5, 'desc': '80-100', 'nilai': 4, 'selected': False, 'created_at': timezone.now(), 'updated_at': timezone.now()},
    {'id_k': 6, 'desc': '1 Bidang', 'nilai': 1, 'selected': False, 'created_at': timezone.now(), 'updated_at': timezone.now()},
    {'id_k': 6, 'desc': '2 Bidang', 'nilai': 2, 'selected': True, 'created_at': timezone.now(), 'updated_at': timezone.now()},
    {'id_k': 6, 'desc': '3 Bidang', 'nilai': 3, 'selected': False, 'created_at': timezone.now(), 'updated_at': timezone.now()},
    {'id_k': 6, 'desc': '>=4 Bidang', 'nilai': 4, 'selected': False, 'created_at': timezone.now(), 'updated_at': timezone.now()},
]

for item in data:
    SubKriteria.objects.create(**item)
