from django.shortcuts import render, get_object_or_404, redirect
from .models import Cagur, Ranking, Kriteria, SubKriteria, NilaiProfil, PerhitunganGap, Gap, PerhitunganAkhir
from django.db.models import Sum
from django.core.paginator import Paginator
from django.http import HttpResponse

from itertools import groupby
from operator import attrgetter

def dashboard(request):
    # Ambil semua Gap
    gaps = Gap.objects.all()

    # Ambil 5 Ranking teratas berdasarkan 'rank'
    rank = Ranking.objects.order_by('rank')[:5]

    # Dapatkan ranking teratas
    top1 = rank[0] if len(rank) > 0 else None
    top2 = rank[1] if len(rank) > 1 else None
    top3 = rank[2] if len(rank) > 2 else None
    top4 = rank[3] if len(rank) > 3 else None
    top5 = rank[4] if len(rank) > 4 else None

    # Mengambil data kriteria pertama
    kriteria1 = Kriteria.objects.first()

    # Mengambil semua data kriteria kecuali yang pertama
    kriteria = Kriteria.objects.all()[1:]

    # Mengambil sub kriteria berdasarkan kriteria pertama
    sub_kriteria1 = SubKriteria.objects.filter(kriteria_id=kriteria1.id) if kriteria1 else None

    # Mengelompokkan sub kriteria berdasarkan kriteria_id
    all_sub_kriteria = SubKriteria.objects.all().order_by('kriteria_id')
    grouped_sub_kriteria = {
        kriteria_id: list(items)
        for kriteria_id, items in groupby(all_sub_kriteria, key=attrgetter('kriteria_id'))
    }

    # Mengirim data ke template
    context = {
        'gaps': gaps,
        'top1': top1,
        'top2': top2,
        'top3': top3,
        'top4': top4,
        'top5': top5,
        'kriteria1': kriteria1,
        'kriteria': kriteria,
        'sub_kriteria1': sub_kriteria1,
        'grouped_sub_kriteria': grouped_sub_kriteria,
    }

    return render(request, 'index.html', context)


def cagur_list(request):
    # Ambil semua data Cagur dan buat pagination (misalnya 5 item per halaman)
    cagurs = Cagur.objects.all()
    paginator = Paginator(cagurs, 5)  # Menentukan jumlah item per halaman
    page_number = request.GET.get('page')  # Ambil nomor halaman dari query parameter
    page_obj = paginator.get_page(page_number)

    # Ambil semua Kriteria
    kriteria = Kriteria.objects.all()
    sub_kriteria = SubKriteria.objects.all()

    # Mengelompokkan sub_kriteria berdasarkan id_k (relasi ke Kriteria)
    grouped_sub_kriteria = {}
    for sub in sub_kriteria:
        grouped_sub_kriteria.setdefault(sub.kriteria_id, []).append(sub)

    # Kirim data ke template
    return render(request, 'cagur.html', {
        'page_obj': page_obj,
        'kriteria': kriteria,
        'grouped_sub_kriteria': grouped_sub_kriteria
    })
    
def cagur_detail(request, id):
    cagur = get_object_or_404(Cagur, id=id)
    return HttpResponse(cagur)  # Anda bisa menampilkan data cagur sesuai keinginan

# Fungsi untuk menyimpan data cagur baru
def cagur_store(request):
    if request.method == 'POST':
        # Buat instance Cagur baru dengan data dari form
        cagur = Cagur.objects.create(
            nama=request.POST.get('nama'),
            telp=request.POST.get('telp'),
            Pendidikan=request.POST.get('Pendidikan'),
            IPK=request.POST.get('IPK'),
            Umur=request.POST.get('Umur'),
            Pengalaman_Mengajar=request.POST.get('Pengalaman_Mengajar'),
            Psikotes=request.POST.get('Psikotes'),
            Sertifikasi_Keahlian=request.POST.get('Sertifikasi_Keahlian')
        )

        # Ambil ID Cagur yang baru saja dibuat
        cagurId = cagur.id

        # Menyimpan ke tabel NilaiProfil
        kriteriaNames = ['Pendidikan', 'IPK', 'Umur', 'Psikotes', 'Pengalaman_Mengajar', 'Sertifikasi_Keahlian']
        for kriteriaName in kriteriaNames:
            desc = request.POST.get(kriteriaName)
            subKriteria = SubKriteria.objects.filter(desc=desc).first()

            if subKriteria:
                nilaiProfil = NilaiProfil()
                nilaiProfil.nilai_profil = subKriteria.nilai
                nilaiProfil.cagur_id = cagurId
                nilaiProfil.kriteria_id = subKriteria.kriteria.id
                nilaiProfil.sub_kriteria_id = subKriteria.id
                nilaiProfil.save()

        # Menyimpan ke tabel PerhitunganGap
        selectedSubKriterias = SubKriteria.objects.filter(selected=1)
        for selectedSubKriteria in selectedSubKriterias:
            desc = request.POST.get(selectedSubKriteria.kriteria.nama)
            subKriteria = SubKriteria.objects.filter(desc=desc).first()

            if subKriteria:
                perhitungan = PerhitunganGap()
                perhitungan.cagur_id = cagurId
                perhitungan.sub_kriteria_id = subKriteria.id
                perhitungan.ideal_profil = selectedSubKriteria.nilai

                nilaiProfilPelamar = NilaiProfil.objects.filter(cagur_id=cagurId, sub_kriteria_id=subKriteria.id).first()
                perhitungan.gap = nilaiProfilPelamar.nilai_profil - selectedSubKriteria.nilai

                gap = Gap.objects.filter(gap=perhitungan.gap).first()
                perhitungan.bobot_gap = gap.bobot_nilai
                perhitungan.save()

        return redirect('cagur_list')  # Redirect ke halaman cagur list
    return render(request, 'cagur.html') 

# Fungsi untuk memperbarui data cagur
def cagur_update(request, id):
    cagur = get_object_or_404(Cagur, id=id)

    if request.method == 'POST':
        cagur.update(**request.POST)

        return redirect('cagur_list')  # Redirect ke halaman cagur list

# Fungsi untuk menghapus data cagur
def cagur_delete(request, id):
    cagur = get_object_or_404(Cagur, id=id)

    if request.method == 'POST':
        cagur.delete()

        return redirect('cagur_list')  # Redirect ke halaman cagur list
    
def result_index(request):
    cagurs = Cagur.objects.all()
    nilaiProfils = NilaiProfil.objects.all()
    subKriteria = SubKriteria.objects.filter(selected=1)
    
    # Paginate results
    perhitunganGaps = PerhitunganGap.objects.all()
    perhitunganAkhirs = PerhitunganAkhir.objects.all()
    rankings = Ranking.objects.all().order_by('rank')
    
    # Apply pagination
    cagur_paginator = Paginator(cagurs, 12)
    nilaiProfil_paginator = Paginator(nilaiProfils, 12)
    perhitungan_gap_paginator = Paginator(perhitunganGaps, 12)
    perhitungan_akhir_paginator = Paginator(perhitunganAkhirs, 4)
    ranking_paginator = Paginator(rankings, 5)
    
    cagur_page = cagur_paginator.get_page(request.GET.get('page'))
    nilaiProfil_page = nilaiProfil_paginator.get_page(request.GET.get('page'))
    perhitungan_gap_page = perhitungan_gap_paginator.get_page(request.GET.get('page'))
    perhitungan_akhir_page = perhitungan_akhir_paginator.get_page(request.GET.get('page'))
    ranking_page = ranking_paginator.get_page(request.GET.get('page'))

    return render(request, 'result.html', {
        'cagurs': cagur_page,
        'nilaiProfils': nilaiProfil_page,
        'subKriteria': subKriteria,
        'perhitunganGaps': perhitungan_gap_page,
        'perhitunganAkhirs': perhitungan_akhir_page,
        'rankings': ranking_page
    })


def result_store(request):
    if request.method == "POST":
        cagurs = Cagur.objects.filter(perhitunganakhir__isnull=True)
        for cagur in cagurs:
            cagurId = cagur.id

            sub_kriteria_core = SubKriteria.objects.filter(selected=1, kriteria__jenis='Core Factor').select_related('kriteria').first()
            sub_kriteria_secondary = SubKriteria.objects.filter(selected=1, kriteria__jenis='Secondary Factor').select_related('kriteria').first()

            perhitungan_core = PerhitunganGap.objects.filter(cagur_id=cagurId, sub_kriteria_id__kriteria__jenis='Core Factor').select_related('sub_kriteria_id__kriteria')
            perhitungan_secondary = PerhitunganGap.objects.filter(cagur_id=cagurId, sub_kriteria_id__kriteria__jenis='Secondary Factor').select_related('sub_kriteria_id__kriteria')

            sum_core = float(perhitungan_core.aggregate(Sum('bobot_gap'))['bobot_gap__sum'] or 0)
            sum_secondary = float(perhitungan_secondary.aggregate(Sum('bobot_gap'))['bobot_gap__sum'] or 0)

            for jenis_kriteria, sub_kriteria, sum_nilai in [('Core Factor', sub_kriteria_core, sum_core), ('Secondary Factor', sub_kriteria_secondary, sum_secondary)]:
                perhitungan_akhir = PerhitunganAkhir()
                perhitungan_akhir.cagur_id = cagurId
                perhitungan_akhir.sub_kriteria_id = sub_kriteria.id
                perhitungan_akhir.jumlah_nilai = sum_nilai
                perhitungan_akhir.rata_rata = sum_nilai / 3
                if jenis_kriteria == 'Core Factor':
                    perhitungan_akhir.total_rata_rata = perhitungan_akhir.rata_rata * 0.7
                else:
                    perhitungan_akhir.total_rata_rata = perhitungan_akhir.rata_rata * 0.3
                perhitungan_akhir.save()

        return redirect('result')
    return redirect('result')


def result_store_rank(request):
    cagurs = Cagur.objects.filter(ranking__isnull=True)
    for cagur in cagurs:
        cagurId = cagur.id

        # Calculate total_nilai for cagur
        total_nilai = PerhitunganAkhir.objects.filter(cagur_id=cagurId).aggregate(Sum('total_rata_rata'))['total_rata_rata__sum']

        # Save to ranking table
        ranking = Ranking()
        ranking.cagur_id = cagurId
        ranking.total_nilai = total_nilai
        ranking.save()

        # Recalculate ranks based on total_nilai
        ranks = Ranking.objects.all().order_by('-total_nilai')
        rank = 1
        for ranked_item in ranks:
            ranked_item.rank = rank
            ranked_item.save()
            rank += 1

    return redirect('result')