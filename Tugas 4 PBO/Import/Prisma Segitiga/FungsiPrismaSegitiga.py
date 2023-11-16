def hitung_luas_selimut(s1, s2, s3, t_prisma):
    return round((s1 + s2 + s3) * t_prisma)

def hitung_luas_permukaan(s1, s2, s3, t_prisma, a, t_segitiga):
    return round((s1 + s2 + s3) * t_prisma + a * t_segitiga)

def hitung_volume(a, t_segitiga, t_prisma):
    return round((1/2) * a * t_segitiga * t_prisma)
