from datatyp import murid #angkatan 24 ke bawah belum di ubah
def angkatan25():
    akt25 = []
    for i in range (1,10): 
         akt25.append(murid(f"1125100{i}", ["matematika diskrit", 
                                            "pengantar informatika", 
                                            "sistem digital"]))

    for i in range (10,99):
         akt25.append(murid(f"112510{i}", ["matematika diskrit", 
                                            "pengantar informatika", 
                                            "sistem digital"]))
    return akt25

def angkatan24():
    akt24 = []
    for i in range (1,10): 
         akt24.append(murid(f"1124100{i}", ["aljabar linier dan geometri", 
                                            "arsitektur komputer", 
                                            "desain web",
                                            "interaksi manusia dan komputer",
                                            "pengantar kecerdasan artifisial",
                                            "sisten operasi",
                                            "struktur data " ]))

    for i in range (10,40):
         akt24.append(murid(f"112410{i}",  ["aljabar linier dan geometri", 
                                            "arsitektur komputer", 
                                            "pengantar kecerdasan artifisial", 
                                            "sistem operasi",  
                                            "struktur data"]))
    for i in range (40,70):
         akt24.append(murid(f"112410{i}",  ["aljabar linier dan geometri",                   
                                            "arsitektur komputer",                               
                                            "pengantar kecerdasan artifisial",               
                                            "sistem operasi",  
                                            "struktur data"]))
         
    for i in range (70,99):
         akt24.append(murid(f"112410{i}", ["aljabar Linier dan Geometri", 
                                            "Arsitektur Komputer", 
                                            "pengantar kecerdasan artifisial", 
                                            "sistem operasi", "struktur data", 
                                            "keprofesian informatika"])) 
    return akt24

def angkatan23():
    akt23 = []
    for i in range (0,10): 
         akt23.append(murid(f"1123100{i}", ["Implementasi dan Pengujian Perangkat Lunak", 
                                            "Interaksi Manusia dan Komputer", 
                                            "Manajemen Basis Data", 
                                            "Pengolahan Citra Digital",
                                            "Desain Web",
                                            "Pemrograman Fungsional",
                                            "Pengembangan Aplikasi Perangkat Bergerak"]))

    for i in range (10,40):
         akt23.append(murid(f"112310{i}",  ["Implementasi dan Pengujian Perangkat Lunak", 
                                            "pengantar kecerdasan artifisial", 
                                            "Manajemen Basis Data", 
                                            "Pemrograman Fungsional",]))

    for i in range (40,70):
         akt23.append(murid(f"112310{i}",  ["Interaksi Manusia dan Komputer",                   
                                            "Manajemen Basis Data",                               
                                            "Pengolahan Citra Digital",               
                                            "Desain Web",  
                                            "Pemrograman Fungsional"]))
    return akt23
