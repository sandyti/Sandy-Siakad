from django.db import models


class TahunAkademik(models.Model):
    # tahun
    # semester
    tahun = models.CharField(max_length=9) 
    semester = models.CharField(max_length=6, choices=[('Ganjil', 'Ganjil'), ('Genap', 'Genap')])
    pass

class MataKuliah(models.Model):
    # nama
    # kode
    # prodi
    # sks
    nama = models.CharField(max_length=100)
    kode = models.CharField(max_length=10, unique=True)
    prodi = models.CharField(max_length=100)  
    sks = models.PositiveSmallIntegerField()  
    def __str__(self):
        return f"{self.kode} - {self.nama}"
    pass


class Jadwal(models.Model):
    # dosen
    # mata kuliah
    # hari pembelajaran 
    # jam_mulai
    # jam_selesai
    # tahun akademik
    # ruangan
    # peserta/kuota
    dosen = models.CharField(max_length=100)
    mata_kuliah = models.ForeignKey(MataKuliah, on_delete=models.CASCADE, related_name="jadwal")
    hari_pembelajaran = models.CharField(max_length=9, choices=[
        ('Senin', 'Senin'),
        ('Selasa', 'Selasa'),
        ('Rabu', 'Rabu'),
        ('Kamis', 'Kamis'),
        ('Jumat', 'Jumat'),
        ('Sabtu', 'Sabtu'),
        ('Minggu', 'Minggu')
    ])
    jam_mulai = models.TimeField()
    jam_selesai = models.TimeField()
    tahun_akademik = models.ForeignKey(TahunAkademik, on_delete=models.CASCADE, related_name="jadwal")
    ruangan = models.CharField(max_length=50)
    kuota = models.PositiveIntegerField()
    def __str__(self):
        return f"{self.mata_kuliah.nama} - {self.hari_pembelajaran} - {self.jam_mulai}-{self.jam_selesai}"
    pass


class KRS(models.Model):
    # tahun_akademik
    # mahasiswa
    # jadwal
    tahun_akademik = models.ForeignKey(TahunAkademik, on_delete=models.CASCADE, related_name="krs")
    mahasiswa = models.CharField(max_length=100) 
    jadwal = models.ManyToManyField(Jadwal, related_name="krs")

    def __str__(self):
        return f"KRS {self.mahasiswa} - {self.tahun_akademik}"
    pass
