from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import TahunAkademik, MataKuliah, Jadwal, KRS
# Register your models here.
@admin.register(TahunAkademik)
class TahunAkademikAdmin(admin.ModelAdmin):
    list_display = ('tahun', 'semester')
    search_fields = ('tahun', 'semester')


@admin.register(MataKuliah)
class MataKuliahAdmin(admin.ModelAdmin):
    list_display = ('kode', 'nama', 'prodi', 'sks')
    search_fields = ('kode', 'nama', 'prodi')
    list_filter = ('prodi',)


@admin.register(Jadwal)
class JadwalAdmin(admin.ModelAdmin):
    list_display = ('mata_kuliah', 'dosen', 'hari_pembelajaran', 'jam_mulai', 'jam_selesai', 'tahun_akademik', 'ruangan', 'kuota')
    search_fields = ('dosen', 'mata_kuliah__nama', 'ruangan')
    list_filter = ('hari_pembelajaran', 'tahun_akademik')
    autocomplete_fields = ('mata_kuliah', 'tahun_akademik')


@admin.register(KRS)
class KRSAdmin(admin.ModelAdmin):
    list_display = ('mahasiswa', 'tahun_akademik')
    search_fields = ('mahasiswa',)
    list_filter = ('tahun_akademik',)
    filter_horizontal = ('jadwal',)