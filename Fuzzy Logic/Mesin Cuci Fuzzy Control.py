import numpy as np
import skfuzzy as fuzz
from tkinter import *
from tkinter import messagebox

def test(berat_baju_value,kategori_kotoran_value,jenis_kain_value):
    #berat_baju_value = berat_baju_value/10
    #input
    berat_baju = np.arange(0,31,1)
    kategori_kotoran = np.arange(0,51,1)
    jenis_kain = np.arange(0,11,1)

    #output
    durasi_mencuci = np.arange(0,2.21,0.1)
    suhu = np.arange(0,61,1)
    RPM = np.arange(0,1200,100)
    waktu_mengeringkan = np.arange(0,16,1)
    kualitas_pencucian = np.arange(0,101,1)

    parameter_output =[durasi_mencuci, suhu, RPM, waktu_mengeringkan, kualitas_pencucian]


    #Berat baju
    berat_baju_dibawah_10Kg = fuzz.trimf(berat_baju,[0,5,10])
    berat_baju_10_sampai_20Kg = fuzz.trimf(berat_baju,[8,15,20])
    berat_baju_diatas_20Kg = fuzz.trimf(berat_baju,[17,23,30])

    #Kategori Kotoran
    kategori_sedikit_kotor = fuzz.trimf(kategori_kotoran,[0,7,15])
    kategori_kotoran_normal = fuzz.trimf(kategori_kotoran,[12,20,35])
    kategori_sangat_kotor = fuzz.trimf(kategori_kotoran,[27,38,50])

    #Jenis Kain
    jenis_kain_bahan_sutra = fuzz.trimf(jenis_kain,[0,2,4])
    jenis_kain_bahan_wol = fuzz.trimf(jenis_kain,[3,5,7])
    jenis_kain_bahan_katun = fuzz.trimf(jenis_kain,[6,8,10])

    #Durasi Mencuci
    durasi_mencuci_singkat = fuzz.trimf(durasi_mencuci,[0,0.25,0.5])
    durasi_mencuci_sedang = fuzz.trimf(durasi_mencuci,[0.4,1,1.5])
    durasi_mencuci_lama = fuzz.trimf(durasi_mencuci,[1.4,1.8,2.20])

    #Temperature
    suhu_dingin = fuzz.trimf(suhu,[0,15,30])
    suhu_hangat = fuzz.trimf(suhu,[27,33,40])
    suhu_panas = fuzz.trimf(suhu,[38,48,60])

    #RPM
    RPM_putaran_lambat = fuzz.trimf(RPM,[0,200,400])
    RPM_putaran_sedang = fuzz.trimf(RPM,[200,600,1000])
    RPM_putaran_cepat = fuzz.trimf(RPM,[600,1000,1200])

    #Waktu Mengeringkan
    waktu_mengeringkan_cepat = fuzz.trimf(waktu_mengeringkan,[0,3,5])
    waktu_mengeringkan_intermediate = fuzz.trimf(waktu_mengeringkan,[4,7,10])
    waktu_mengeringkan_sangat_lama = fuzz.trimf(waktu_mengeringkan,[8,12,15])

    #Kualitas Pencucian
    kualitas_pencucian_cukup = fuzz.trimf(kualitas_pencucian,[0,30,60])
    kualitas_pencucian_baik = fuzz.trimf(kualitas_pencucian,[55,65,75])
    kualitas_pencucian_sangat_baik= fuzz.trimf(kualitas_pencucian,[70,85,100])

    ## if-then rules
    ## Rule 1
    rule1_berat_baju = fuzz.interp_membership(berat_baju,  berat_baju_dibawah_10Kg , berat_baju_value)
    rule1_kategori_kotoran = fuzz.interp_membership(kategori_kotoran, kategori_sedikit_kotor, kategori_kotoran_value)
    rule1_jenis_kain = fuzz.interp_membership(jenis_kain, jenis_kain_bahan_sutra, jenis_kain_value)
    rule_1_antecedent = max(rule1_berat_baju,rule1_kategori_kotoran,rule1_jenis_kain,)

    rule_1_clip = []
    rule_1_clip.append(np.fmin(rule_1_antecedent, durasi_mencuci_singkat))
    rule_1_clip.append(np.fmin(rule_1_antecedent, suhu_dingin))
    rule_1_clip.append(np.fmin(rule_1_antecedent, RPM_putaran_lambat))
    rule_1_clip.append(np.fmin(rule_1_antecedent, waktu_mengeringkan_cepat))
    rule_1_clip.append(np.fmin(rule_1_antecedent, kualitas_pencucian_cukup))

    ## Rule 2
    rule2_berat_baju = fuzz.interp_membership(berat_baju,  berat_baju_10_sampai_20Kg , berat_baju_value)
    rule2_kategori_kotoran = fuzz.interp_membership(kategori_kotoran, kategori_sedikit_kotor, kategori_kotoran_value)
    rule2_jenis_kain = fuzz.interp_membership(jenis_kain, jenis_kain_bahan_sutra, jenis_kain_value)
    rule_2_antecedent = max(rule2_berat_baju,rule2_kategori_kotoran,rule2_jenis_kain,)

    rule_2_clip = []
    rule_2_clip.append(np.fmin(rule_2_antecedent, durasi_mencuci_sedang))
    rule_2_clip.append(np.fmin(rule_2_antecedent, suhu_dingin))
    rule_2_clip.append(np.fmin(rule_2_antecedent, RPM_putaran_sedang))
    rule_2_clip.append(np.fmin(rule_2_antecedent, waktu_mengeringkan_intermediate))
    rule_2_clip.append(np.fmin(rule_2_antecedent, kualitas_pencucian_cukup))

    ## Rule 3
    rule3_berat_baju = fuzz.interp_membership(berat_baju, berat_baju_diatas_20Kg , berat_baju_value)
    rule3_kategori_kotoran = fuzz.interp_membership(kategori_kotoran, kategori_sedikit_kotor, kategori_kotoran_value)
    rule3_jenis_kain = fuzz.interp_membership(jenis_kain, jenis_kain_bahan_sutra, jenis_kain_value)
    rule_3_antecedent = max(rule3_berat_baju,rule3_kategori_kotoran,rule3_jenis_kain,)

    rule_3_clip = []
    rule_3_clip.append(np.fmin(rule_3_antecedent, durasi_mencuci_singkat))
    rule_3_clip.append(np.fmin(rule_3_antecedent, suhu_hangat))
    rule_3_clip.append(np.fmin(rule_3_antecedent, RPM_putaran_sedang))
    rule_3_clip.append(np.fmin(rule_3_antecedent, waktu_mengeringkan_intermediate))
    rule_3_clip.append(np.fmin(rule_3_antecedent, kualitas_pencucian_sangat_baik))

    ## Rule 4
    rule4_berat_baju = fuzz.interp_membership(berat_baju,   berat_baju_dibawah_10Kg , berat_baju_value)
    rule4_kategori_kotoran = fuzz.interp_membership(kategori_kotoran, kategori_kotoran_normal, kategori_kotoran_value)
    rule4_jenis_kain = fuzz.interp_membership(jenis_kain, jenis_kain_bahan_sutra, jenis_kain_value)
    rule_4_antecedent = max(rule4_berat_baju,rule4_kategori_kotoran,rule4_jenis_kain,)

    rule_4_clip = []
    rule_4_clip.append(np.fmin(rule_4_antecedent, durasi_mencuci_singkat))
    rule_4_clip.append(np.fmin(rule_4_antecedent, suhu_dingin))
    rule_4_clip.append(np.fmin(rule_4_antecedent, RPM_putaran_lambat))
    rule_4_clip.append(np.fmin(rule_4_antecedent, waktu_mengeringkan_sangat_lama))
    rule_4_clip.append(np.fmin(rule_4_antecedent, kualitas_pencucian_baik))

    ## Rule 5
    rule5_berat_baju = fuzz.interp_membership(berat_baju, berat_baju_10_sampai_20Kg , berat_baju_value)
    rule5_kategori_kotoran = fuzz.interp_membership(kategori_kotoran, kategori_kotoran_normal, kategori_kotoran_value)
    rule5_jenis_kain = fuzz.interp_membership(jenis_kain, jenis_kain_bahan_sutra, jenis_kain_value)
    rule_5_antecedent = max(rule5_berat_baju,rule5_kategori_kotoran,rule5_jenis_kain,)

    rule_5_clip = []
    rule_5_clip.append(np.fmin(rule_5_antecedent, durasi_mencuci_sedang))
    rule_5_clip.append(np.fmin(rule_5_antecedent, suhu_dingin))
    rule_5_clip.append(np.fmin(rule_5_antecedent, RPM_putaran_sedang))
    rule_5_clip.append(np.fmin(rule_5_antecedent, waktu_mengeringkan_cepat))
    rule_5_clip.append(np.fmin(rule_5_antecedent, kualitas_pencucian_cukup))

    ## Rule 6
    rule6_berat_baju = fuzz.interp_membership(berat_baju,   berat_baju_diatas_20Kg , berat_baju_value)
    rule6_kategori_kotoran = fuzz.interp_membership(kategori_kotoran, kategori_kotoran_normal, kategori_kotoran_value)
    rule6_jenis_kain = fuzz.interp_membership(jenis_kain, jenis_kain_bahan_sutra, jenis_kain_value)
    rule_6_antecedent = max(rule6_berat_baju,rule6_kategori_kotoran,rule6_jenis_kain,)

    rule_6_clip = []
    rule_6_clip.append(np.fmin(rule_6_antecedent, durasi_mencuci_sedang))
    rule_6_clip.append(np.fmin(rule_6_antecedent, suhu_hangat))
    rule_6_clip.append(np.fmin(rule_6_antecedent, RPM_putaran_sedang))
    rule_6_clip.append(np.fmin(rule_6_antecedent, waktu_mengeringkan_sangat_lama))
    rule_6_clip.append(np.fmin(rule_6_antecedent, kualitas_pencucian_baik))

    ## Rule 7
    rule7_berat_baju = fuzz.interp_membership(berat_baju,   berat_baju_dibawah_10Kg , berat_baju_value)
    rule7_kategori_kotoran = fuzz.interp_membership(kategori_kotoran, kategori_sangat_kotor, kategori_kotoran_value)
    rule7_jenis_kain = fuzz.interp_membership(jenis_kain, jenis_kain_bahan_sutra, jenis_kain_value)
    rule_7_antecedent = max(rule7_berat_baju,rule7_kategori_kotoran,rule7_jenis_kain,)

    rule_7_clip = []
    rule_7_clip.append(np.fmin(rule_7_antecedent, durasi_mencuci_singkat))
    rule_7_clip.append(np.fmin(rule_7_antecedent, suhu_dingin))
    rule_7_clip.append(np.fmin(rule_7_antecedent, RPM_putaran_sedang))
    rule_7_clip.append(np.fmin(rule_7_antecedent, waktu_mengeringkan_intermediate))
    rule_7_clip.append(np.fmin(rule_7_antecedent, kualitas_pencucian_cukup))

    ## Rule 8
    rule8_berat_baju = fuzz.interp_membership(berat_baju,   berat_baju_10_sampai_20Kg , berat_baju_value)
    rule8_kategori_kotoran = fuzz.interp_membership(kategori_kotoran, kategori_sangat_kotor, kategori_kotoran_value)
    rule8_jenis_kain = fuzz.interp_membership(jenis_kain, jenis_kain_bahan_sutra, jenis_kain_value)
    rule_8_antecedent = max(rule8_berat_baju,rule8_kategori_kotoran,rule8_jenis_kain,)

    rule_8_clip = []
    rule_8_clip.append(np.fmin(rule_8_antecedent, durasi_mencuci_sedang))
    rule_8_clip.append(np.fmin(rule_8_antecedent, suhu_hangat))
    rule_8_clip.append(np.fmin(rule_8_antecedent, RPM_putaran_sedang))
    rule_8_clip.append(np.fmin(rule_8_antecedent, waktu_mengeringkan_cepat))
    rule_8_clip.append(np.fmin(rule_8_antecedent, kualitas_pencucian_sangat_baik))

    ## Rule 9
    rule9_berat_baju = fuzz.interp_membership(berat_baju,   berat_baju_diatas_20Kg , berat_baju_value)
    rule9_kategori_kotoran = fuzz.interp_membership(kategori_kotoran, kategori_sangat_kotor, kategori_kotoran_value)
    rule9_jenis_kain = fuzz.interp_membership(jenis_kain, jenis_kain_bahan_sutra, jenis_kain_value)
    rule_9_antecedent = max(rule9_berat_baju,rule9_kategori_kotoran,rule9_jenis_kain,)

    rule_9_clip = []
    rule_9_clip.append(np.fmin(rule_9_antecedent, durasi_mencuci_lama))
    rule_9_clip.append(np.fmin(rule_9_antecedent, suhu_hangat))
    rule_9_clip.append(np.fmin(rule_9_antecedent, RPM_putaran_sedang))
    rule_9_clip.append(np.fmin(rule_9_antecedent, waktu_mengeringkan_cepat))
    rule_9_clip.append(np.fmin(rule_9_antecedent, kualitas_pencucian_sangat_baik))


    #Woolen
    ## Rule 10
    rule10_berat_baju = fuzz.interp_membership(berat_baju,   berat_baju_dibawah_10Kg , berat_baju_value)
    rule10_kategori_kotoran = fuzz.interp_membership(kategori_kotoran, kategori_sedikit_kotor, kategori_kotoran_value)
    rule10_jenis_kain = fuzz.interp_membership(jenis_kain, jenis_kain_bahan_wol, jenis_kain_value)
    rule_10_antecedent = max(rule10_berat_baju,rule10_kategori_kotoran,rule10_jenis_kain,)

    rule_10_clip = []
    rule_10_clip.append(np.fmin(rule_10_antecedent, durasi_mencuci_singkat))
    rule_10_clip.append(np.fmin(rule_10_antecedent, suhu_hangat))
    rule_10_clip.append(np.fmin(rule_10_antecedent, RPM_putaran_sedang))
    rule_10_clip.append(np.fmin(rule_10_antecedent, waktu_mengeringkan_sangat_lama))
    rule_10_clip.append(np.fmin(rule_10_antecedent, kualitas_pencucian_baik))

    ## Rule 11
    rule11_berat_baju = fuzz.interp_membership(berat_baju,   berat_baju_10_sampai_20Kg , berat_baju_value)
    rule11_kategori_kotoran = fuzz.interp_membership(kategori_kotoran, kategori_sedikit_kotor, kategori_kotoran_value)
    rule11_jenis_kain = fuzz.interp_membership(jenis_kain, jenis_kain_bahan_wol, jenis_kain_value)
    rule_11_antecedent = max(rule11_berat_baju,rule11_kategori_kotoran,rule11_jenis_kain,)

    rule_11_clip = []
    rule_11_clip.append(np.fmin(rule_11_antecedent, durasi_mencuci_singkat))
    rule_11_clip.append(np.fmin(rule_11_antecedent, suhu_hangat))
    rule_11_clip.append(np.fmin(rule_11_antecedent, RPM_putaran_sedang))
    rule_11_clip.append(np.fmin(rule_11_antecedent, waktu_mengeringkan_intermediate))
    rule_11_clip.append(np.fmin(rule_11_antecedent, kualitas_pencucian_cukup))

    ## Rule 12
    rule12_berat_baju = fuzz.interp_membership(berat_baju,   berat_baju_diatas_20Kg , berat_baju_value)
    rule12_kategori_kotoran = fuzz.interp_membership(kategori_kotoran, kategori_sedikit_kotor, kategori_kotoran_value)
    rule12_jenis_kain = fuzz.interp_membership(jenis_kain, jenis_kain_bahan_wol, jenis_kain_value)
    rule_12_antecedent = max(rule12_berat_baju,rule12_kategori_kotoran,rule12_jenis_kain,)

    rule_12_clip = []
    rule_12_clip.append(np.fmin(rule_12_antecedent, durasi_mencuci_sedang))
    rule_12_clip.append(np.fmin(rule_12_antecedent, suhu_hangat))
    rule_12_clip.append(np.fmin(rule_12_antecedent, RPM_putaran_sedang))
    rule_12_clip.append(np.fmin(rule_12_antecedent, waktu_mengeringkan_cepat))
    rule_12_clip.append(np.fmin(rule_12_antecedent, kualitas_pencucian_cukup))

    ## Rule 13
    rule13_berat_baju = fuzz.interp_membership(berat_baju,   berat_baju_dibawah_10Kg , berat_baju_value)
    rule13_kategori_kotoran = fuzz.interp_membership(kategori_kotoran, kategori_kotoran_normal, kategori_kotoran_value)
    rule13_jenis_kain = fuzz.interp_membership(jenis_kain, jenis_kain_bahan_wol, jenis_kain_value)
    rule_13_antecedent = max(rule13_berat_baju,rule13_kategori_kotoran,rule13_jenis_kain,)

    rule_13_clip = []
    rule_13_clip.append(np.fmin(rule_13_antecedent, durasi_mencuci_singkat))
    rule_13_clip.append(np.fmin(rule_13_antecedent, suhu_hangat))
    rule_13_clip.append(np.fmin(rule_13_antecedent, RPM_putaran_sedang))
    rule_13_clip.append(np.fmin(rule_13_antecedent, waktu_mengeringkan_intermediate))
    rule_13_clip.append(np.fmin(rule_13_antecedent, kualitas_pencucian_baik))

    ## Rule 14
    rule14_berat_baju = fuzz.interp_membership(berat_baju,   berat_baju_10_sampai_20Kg , berat_baju_value)
    rule14_kategori_kotoran = fuzz.interp_membership(kategori_kotoran, kategori_kotoran_normal, kategori_kotoran_value)
    rule14_jenis_kain = fuzz.interp_membership(jenis_kain, jenis_kain_bahan_wol, jenis_kain_value)
    rule_14_antecedent = max(rule14_berat_baju,rule14_kategori_kotoran,rule14_jenis_kain,)

    rule_14_clip = []
    rule_14_clip.append(np.fmin(rule_14_antecedent, durasi_mencuci_singkat))
    rule_14_clip.append(np.fmin(rule_14_antecedent, suhu_hangat))
    rule_14_clip.append(np.fmin(rule_14_antecedent, RPM_putaran_sedang))
    rule_14_clip.append(np.fmin(rule_14_antecedent, waktu_mengeringkan_intermediate))
    rule_14_clip.append(np.fmin(rule_14_antecedent, kualitas_pencucian_baik))

    ## Rule 15
    rule15_berat_baju = fuzz.interp_membership(berat_baju,   berat_baju_diatas_20Kg , berat_baju_value)
    rule15_kategori_kotoran = fuzz.interp_membership(kategori_kotoran, kategori_kotoran_normal, kategori_kotoran_value)
    rule15_jenis_kain = fuzz.interp_membership(jenis_kain, jenis_kain_bahan_wol, jenis_kain_value)
    rule_15_antecedent = max(rule15_berat_baju,rule15_kategori_kotoran,rule15_jenis_kain,)

    rule_15_clip = []
    rule_15_clip.append(np.fmin(rule_15_antecedent, durasi_mencuci_sedang))
    rule_15_clip.append(np.fmin(rule_15_antecedent, suhu_hangat))
    rule_15_clip.append(np.fmin(rule_15_antecedent, RPM_putaran_sedang))
    rule_15_clip.append(np.fmin(rule_15_antecedent, waktu_mengeringkan_cepat))
    rule_15_clip.append(np.fmin(rule_15_antecedent, kualitas_pencucian_sangat_baik))

    ## Rule 16
    rule16_berat_baju = fuzz.interp_membership(berat_baju,   berat_baju_dibawah_10Kg , berat_baju_value)
    rule16_kategori_kotoran = fuzz.interp_membership(kategori_kotoran, kategori_sangat_kotor, kategori_kotoran_value)
    rule16_jenis_kain = fuzz.interp_membership(jenis_kain, jenis_kain_bahan_wol, jenis_kain_value)
    rule_16_antecedent = max(rule16_berat_baju,rule16_kategori_kotoran,rule16_jenis_kain,)

    rule_16_clip = []
    rule_16_clip.append(np.fmin(rule_16_antecedent, durasi_mencuci_sedang))
    rule_16_clip.append(np.fmin(rule_16_antecedent, suhu_panas))
    rule_16_clip.append(np.fmin(rule_16_antecedent, RPM_putaran_sedang))
    rule_16_clip.append(np.fmin(rule_16_antecedent, waktu_mengeringkan_cepat))
    rule_16_clip.append(np.fmin(rule_16_antecedent, kualitas_pencucian_sangat_baik))

    ## Rule 17
    rule17_berat_baju = fuzz.interp_membership(berat_baju,   berat_baju_10_sampai_20Kg , berat_baju_value)
    rule17_kategori_kotoran = fuzz.interp_membership(kategori_kotoran, kategori_sangat_kotor, kategori_kotoran_value)
    rule17_jenis_kain = fuzz.interp_membership(jenis_kain, jenis_kain_bahan_wol, jenis_kain_value)
    rule_17_antecedent = max(rule17_berat_baju,rule17_kategori_kotoran,rule17_jenis_kain,)

    rule_17_clip = []
    rule_17_clip.append(np.fmin(rule_17_antecedent, durasi_mencuci_sedang))
    rule_17_clip.append(np.fmin(rule_17_antecedent, suhu_hangat))
    rule_17_clip.append(np.fmin(rule_17_antecedent, RPM_putaran_cepat))
    rule_17_clip.append(np.fmin(rule_17_antecedent, waktu_mengeringkan_cepat))
    rule_17_clip.append(np.fmin(rule_17_antecedent, kualitas_pencucian_cukup))

    ## Rule 18
    rule18_berat_baju = fuzz.interp_membership(berat_baju,   berat_baju_diatas_20Kg , berat_baju_value)
    rule18_kategori_kotoran = fuzz.interp_membership(kategori_kotoran, kategori_sangat_kotor, kategori_kotoran_value)
    rule18_jenis_kain = fuzz.interp_membership(jenis_kain, jenis_kain_bahan_wol, jenis_kain_value)
    rule_18_antecedent = max(rule18_berat_baju,rule18_kategori_kotoran,rule18_jenis_kain,)

    rule_18_clip = []
    rule_18_clip.append(np.fmin(rule_18_antecedent, durasi_mencuci_lama))
    rule_18_clip.append(np.fmin(rule_18_antecedent, suhu_panas))
    rule_18_clip.append(np.fmin(rule_18_antecedent, RPM_putaran_cepat))
    rule_18_clip.append(np.fmin(rule_18_antecedent, waktu_mengeringkan_cepat))
    rule_18_clip.append(np.fmin(rule_18_antecedent, kualitas_pencucian_cukup))

    #Katun
    ## Rule 19
    rule19_berat_baju = fuzz.interp_membership(berat_baju,   berat_baju_dibawah_10Kg , berat_baju_value)
    rule19_kategori_kotoran = fuzz.interp_membership(kategori_kotoran, kategori_sedikit_kotor, kategori_kotoran_value)
    rule19_jenis_kain = fuzz.interp_membership(jenis_kain, jenis_kain_bahan_katun, jenis_kain_value)
    rule_19_antecedent = max(rule19_berat_baju,rule19_kategori_kotoran,rule19_jenis_kain,)

    rule_19_clip = []
    rule_19_clip.append(np.fmin(rule_19_antecedent, durasi_mencuci_singkat))
    rule_19_clip.append(np.fmin(rule_19_antecedent, suhu_hangat))
    rule_19_clip.append(np.fmin(rule_19_antecedent, RPM_putaran_lambat))
    rule_19_clip.append(np.fmin(rule_19_antecedent, waktu_mengeringkan_intermediate))
    rule_19_clip.append(np.fmin(rule_19_antecedent, kualitas_pencucian_cukup))

    ## Rule 20
    rule20_berat_baju = fuzz.interp_membership(berat_baju,   berat_baju_10_sampai_20Kg , berat_baju_value)
    rule20_kategori_kotoran = fuzz.interp_membership(kategori_kotoran, kategori_sedikit_kotor, kategori_kotoran_value)
    rule20_jenis_kain = fuzz.interp_membership(jenis_kain, jenis_kain_bahan_katun, jenis_kain_value)
    rule_20_antecedent = max(rule20_berat_baju,rule20_kategori_kotoran,rule20_jenis_kain,)

    rule_20_clip = []
    rule_20_clip.append(np.fmin(rule_20_antecedent, durasi_mencuci_singkat))
    rule_20_clip.append(np.fmin(rule_20_antecedent, suhu_hangat))
    rule_20_clip.append(np.fmin(rule_20_antecedent, RPM_putaran_sedang))
    rule_20_clip.append(np.fmin(rule_20_antecedent, waktu_mengeringkan_intermediate))
    rule_20_clip.append(np.fmin(rule_20_antecedent, kualitas_pencucian_cukup))

    ## Rule 21
    rule21_berat_baju = fuzz.interp_membership(berat_baju,   berat_baju_diatas_20Kg , berat_baju_value)
    rule21_kategori_kotoran = fuzz.interp_membership(kategori_kotoran, kategori_sedikit_kotor, kategori_kotoran_value)
    rule21_jenis_kain = fuzz.interp_membership(jenis_kain, jenis_kain_bahan_katun, jenis_kain_value)
    rule_21_antecedent = max(rule21_berat_baju,rule21_kategori_kotoran,rule21_jenis_kain,)

    rule_21_clip = []
    rule_21_clip.append(np.fmin(rule_21_antecedent, durasi_mencuci_sedang))
    rule_21_clip.append(np.fmin(rule_21_antecedent, suhu_hangat))
    rule_21_clip.append(np.fmin(rule_21_antecedent, RPM_putaran_cepat))
    rule_21_clip.append(np.fmin(rule_21_antecedent, waktu_mengeringkan_cepat))
    rule_21_clip.append(np.fmin(rule_21_antecedent, kualitas_pencucian_sangat_baik))

    ## Rule 22
    rule22_berat_baju = fuzz.interp_membership(berat_baju,   berat_baju_dibawah_10Kg , berat_baju_value)
    rule22_kategori_kotoran = fuzz.interp_membership(kategori_kotoran, kategori_kotoran_normal, kategori_kotoran_value)
    rule22_jenis_kain = fuzz.interp_membership(jenis_kain, jenis_kain_bahan_katun, jenis_kain_value)
    rule_22_antecedent = max(rule22_berat_baju,rule22_kategori_kotoran,rule22_jenis_kain,)

    rule_22_clip = []
    rule_22_clip.append(np.fmin(rule_22_antecedent, durasi_mencuci_singkat))
    rule_22_clip.append(np.fmin(rule_22_antecedent, suhu_hangat))
    rule_22_clip.append(np.fmin(rule_22_antecedent, RPM_putaran_sedang))
    rule_22_clip.append(np.fmin(rule_22_antecedent, waktu_mengeringkan_intermediate))
    rule_22_clip.append(np.fmin(rule_22_antecedent, kualitas_pencucian_sangat_baik))

    ## Rule 23
    rule23_berat_baju = fuzz.interp_membership(berat_baju,   berat_baju_10_sampai_20Kg , berat_baju_value)
    rule23_kategori_kotoran = fuzz.interp_membership(kategori_kotoran, kategori_kotoran_normal, kategori_kotoran_value)
    rule23_jenis_kain = fuzz.interp_membership(jenis_kain, jenis_kain_bahan_katun, jenis_kain_value)
    rule_23_antecedent = max(rule23_berat_baju,rule23_kategori_kotoran,rule23_jenis_kain,)

    rule_23_clip = []
    rule_23_clip.append(np.fmin(rule_23_antecedent, durasi_mencuci_sedang))
    rule_23_clip.append(np.fmin(rule_23_antecedent, suhu_hangat))
    rule_23_clip.append(np.fmin(rule_23_antecedent, RPM_putaran_sedang))
    rule_23_clip.append(np.fmin(rule_23_antecedent, waktu_mengeringkan_cepat))
    rule_23_clip.append(np.fmin(rule_23_antecedent, kualitas_pencucian_sangat_baik))

    ## Rule 24
    rule24_berat_baju = fuzz.interp_membership(berat_baju,   berat_baju_diatas_20Kg , berat_baju_value)
    rule24_kategori_kotoran = fuzz.interp_membership(kategori_kotoran, kategori_kotoran_normal, kategori_kotoran_value)
    rule24_jenis_kain = fuzz.interp_membership(jenis_kain, jenis_kain_bahan_katun, jenis_kain_value)
    rule_24_antecedent = max(rule24_berat_baju,rule24_kategori_kotoran,rule24_jenis_kain,)

    rule_24_clip = []
    rule_24_clip.append(np.fmin(rule_24_antecedent, durasi_mencuci_lama))
    rule_24_clip.append(np.fmin(rule_24_antecedent, suhu_hangat))
    rule_24_clip.append(np.fmin(rule_24_antecedent, RPM_putaran_cepat))
    rule_24_clip.append(np.fmin(rule_24_antecedent, waktu_mengeringkan_cepat))
    rule_24_clip.append(np.fmin(rule_24_antecedent, kualitas_pencucian_cukup))

    ## Rule 25
    rule25_berat_baju = fuzz.interp_membership(berat_baju,   berat_baju_dibawah_10Kg , berat_baju_value)
    rule25_kategori_kotoran = fuzz.interp_membership(kategori_kotoran, kategori_sangat_kotor, kategori_kotoran_value)
    rule25_jenis_kain = fuzz.interp_membership(jenis_kain, jenis_kain_bahan_katun, jenis_kain_value)
    rule_25_antecedent = max(rule25_berat_baju,rule25_kategori_kotoran,rule25_jenis_kain,)

    rule_25_clip = []
    rule_25_clip.append(np.fmin(rule_25_antecedent, durasi_mencuci_lama))
    rule_25_clip.append(np.fmin(rule_25_antecedent, suhu_panas))
    rule_25_clip.append(np.fmin(rule_25_antecedent, RPM_putaran_cepat))
    rule_25_clip.append(np.fmin(rule_25_antecedent, waktu_mengeringkan_intermediate))
    rule_25_clip.append(np.fmin(rule_25_antecedent, kualitas_pencucian_cukup))

    ## Rule 26
    rule26_berat_baju = fuzz.interp_membership(berat_baju,   berat_baju_10_sampai_20Kg , berat_baju_value)
    rule26_kategori_kotoran = fuzz.interp_membership(kategori_kotoran, kategori_sangat_kotor, kategori_kotoran_value)
    rule26_jenis_kain = fuzz.interp_membership(jenis_kain, jenis_kain_bahan_katun, jenis_kain_value)
    rule_26_antecedent = max(rule26_berat_baju,rule26_kategori_kotoran,rule26_jenis_kain,)

    rule_26_clip = []
    rule_26_clip.append(np.fmin(rule_26_antecedent, durasi_mencuci_sedang))
    rule_26_clip.append(np.fmin(rule_26_antecedent, suhu_panas))
    rule_26_clip.append(np.fmin(rule_26_antecedent, RPM_putaran_cepat))
    rule_26_clip.append(np.fmin(rule_26_antecedent, waktu_mengeringkan_sangat_lama))
    rule_26_clip.append(np.fmin(rule_26_antecedent, kualitas_pencucian_sangat_baik))
    
    ## Rule 27
    rule27_berat_baju = fuzz.interp_membership(berat_baju,   berat_baju_diatas_20Kg , berat_baju_value)
    rule27_kategori_kotoran = fuzz.interp_membership(kategori_kotoran, kategori_sangat_kotor, kategori_kotoran_value)
    rule27_jenis_kain = fuzz.interp_membership(jenis_kain, jenis_kain_bahan_katun, jenis_kain_value)
    rule_27_antecedent = max(rule27_berat_baju,rule27_kategori_kotoran,rule27_jenis_kain,)

    rule_27_clip = []
    rule_27_clip.append(np.fmin(rule_27_antecedent, durasi_mencuci_lama))
    rule_27_clip.append(np.fmin(rule_27_antecedent, suhu_panas))
    rule_27_clip.append(np.fmin(rule_27_antecedent, RPM_putaran_cepat))
    rule_27_clip.append(np.fmin(rule_27_antecedent, waktu_mengeringkan_sangat_lama))
    rule_27_clip.append(np.fmin(rule_27_antecedent, kualitas_pencucian_cukup))

    #kombinasi semua rule
    rule_list = [rule_1_clip, rule_2_clip, rule_3_clip, rule_4_clip, rule_5_clip, rule_6_clip, rule_7_clip, rule_8_clip, rule_9_clip,
                 rule_10_clip, rule_11_clip, rule_12_clip, rule_13_clip, rule_14_clip, rule_15_clip, rule_16_clip, rule_17_clip, rule_18_clip,
                 rule_19_clip, rule_20_clip, rule_21_clip, rule_22_clip, rule_23_clip, rule_24_clip, rule_25_clip, rule_26_clip, rule_27_clip]

    ans_list = []
    for output_idx,output in enumerate(parameter_output):
        x = rule_list[0]
        for rule_idx in range(1, len(rule_list)):
            if rule_idx==1:
                x = x[output_idx]
            y = rule_list[rule_idx]
            x = np.fmax(x,y[output_idx])
        ans = round(fuzz.defuzz(output, x, 'centroid'),2)
        ans_list.append(ans)
    return ans_list

class MyWindow:
    def __init__(self, win):
        self.intro=Label(win, text = "Input Data", font='Helvetica 10 bold').place(x=125, y=10)
        self.intro=Label(win, text = "Referensi Input", font='Helvetica 10 bold').place(x=350, y=10)
        
        self.lbl1=Label(win, text='Berat Baju').place(x=50, y=50)
        self.lbl2=Label(win, text='Kategori Kotoran').place(x=50, y=85)
        self.lbl3=Label(win, text='Jenis Kain').place(x=50, y=120)
        self.lblA1=Label(win, text='Durasi Pencucian').place(x=50, y=300)
        self.lblA2=Label(win, text='Suhu').place(x=50, y=335)
        self.lblA3=Label(win, text='RPM').place(x=50, y=370)
        self.lblA4=Label(win, text='Waktu Pengeringan').place(x=50, y=405)
        self.lblA5=Label(win, text='Kualitas Cucian').place(x=50, y=440)
        
        self.t1=Entry(bd=3)
        self.t2=Entry(bd=3)
        self.t3=Entry(bd=3)
        self.tA1=Entry(bd=3)
        self.tA2=Entry(bd=3)
        self.tA3=Entry(bd=3)
        self.tA4=Entry(bd=3)
        self.tA5=Entry(bd=3)
        
        self.t1.place(x=160, y=50)
        self.t2.place(x=160, y=85)
        self.t3.place(x=160, y=120)
        self.tA1.place(x=160, y=300)
        self.tA2.place(x=160, y=335)
        self.tA3.place(x=160, y=370)
        self.tA4.place(x=160, y=405)
        self.tA5.place(x=160, y=440)
        
        self.info1=Label(win, text='Range 0 - 30').place(x=300, y=50)
        self.info1=Label(win, text='Sedikit kotor(0-15) kotor normal(16-35) sangat kotor(36-50)').place(x=300, y=85)
        self.info1=Label(win, text='Sutra(0-4), Wol(5-7), Katun(8-10)').place(x=300, y=120)
        self.info1=Label(win, text='Jam').place(x=300, y=300)
        self.info1=Label(win, text='°C').place(x=300, y=335)
        self.info1=Label(win, text='Revolutions per Minute(rpm)').place(x=300, y=370)
        self.info1=Label(win, text='Menit').place(x=300, y=405)
        self.info1=Label(win, text='Cukup(0-60), Baik(61-75), Sangat Baik(76-100)').place(x=300, y=440)
        
        self.btn1 = Button(win, text='Predict')
        self.b1=Button(win, text='MULAI MENCUCI', command=self.predict, height = 1, width = 30)
        self.b1.place(x=190, y=250)
        

    def predict(self):
        self.tA1.delete(0, END)
        self.tA2.delete(0, END)
        self.tA3.delete(0, END)
        self.tA4.delete(0, END)
        self.tA5.delete(0, END)
        try:
            results = test(float(self.t1.get()),
                            float(self.t2.get()),
                            float(self.t3.get()))
            
            self.tA1.insert(END, str(results[0]))
            self.tA2.insert(END, str(results[1]))
            self.tA3.insert(END, str(results[2]))
            self.tA4.insert(END, str(results[3]))
            self.tA5.insert(END, str(results[4]))
        except Exception as e:
            messagebox.showerror("Terjadi Kesalahan", "Silahkan Coba Lagi!\n Catatan: Periksa SEMUA spasi/input diisi dengan ANGKA sesuai REFERENSI INPUT")
window=Tk()
mywin=MyWindow(window)
window.title('Fuzzy Logic Control System Pada Mesin Cuci')
window.geometry("600x500")
window.mainloop()









