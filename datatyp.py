class murid:
    def __init__ (self, nama, courses):
        self.nama = nama
        self.courses = courses

    def __repr__(self):
        return f"murid({self.nama})"
    
class course:
    def __init__ (self, nama, dosen, jumlah_class=1):
        self.nama = nama
        self.dosen = dosen if isinstance(dosen, list) else [dosen]
        self.jumlah_class = jumlah_class

class courseclass:
    def __init__ (self, course, section, dosen=None): 
        self.course = course
        self.section = section
        self.dosen = dosen 
        self.muridd = []

    def __repr__(self):   
            return f"{self.course.name}-{self.section} ({self.dosen})"
        
class room:
    def __init__ (self, nama, kapasitas, waktu_tersedia):
        self.nama = nama
        self.kapasitas = kapasitas
        self.waktu_tersedia = set(waktu_tersedia)

    def __repr__(self):
        return f"room({self.nama}, cap={self.kapasitas})"

class timeslot:
    def __init__ (self, slot_id, hari, waktu):
        self.slot_id = slot_id
        self.hari = hari
        self.waktu = waktu

    def __repr__(self):
        return f"timeslot({self.hari}-{self.waktu})"