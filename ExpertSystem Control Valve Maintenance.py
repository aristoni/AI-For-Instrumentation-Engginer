class ControlValveFailureAnalysis:
    def __init__(self):
        
        #Pendefinisian Rules / Aturan
        self.rules = {
            #Aturan Manually
            'Control Valve Manually Actuated': {
                'Penyebab': ['Terdapat Kotoran dalam dudukan valve', 'Pemakaian Berlebih', 'Lecet', 'Tekanan Berlebihan', 'Kerusakan Mekanik', 'Packed tidak sesuai', 'Packed Box Kendor', 'Packed terlalu kencang', 'Tuas Rusak', 'Stem Valve Lepas', 'Valve dibawah ukuran'],
                'Permasalahan': {
                    'Valve Fails To Open': ['Lecet', 'Tekanan Berlebihan', 'Kerusakan Mekanik', 'Packed terlalu kencang', 'Tuas Rusak', 'Stem Valve Lepas'],
                    'Valve Fails To Close': ['Terdapat Kotoran dalam dudukan valve', 'Pemakaian Berlebih', 'Lecet', 'Tekanan Berlebihan', 'Kerusakan Mekanik', 'Packed terlalu kencang', 'Tuas Rusak', 'Stem Valve Lepas'],
                    'Kebocoran Melalui Valve': ['Terdapat Kotoran dalam dudukan valve', 'Pemakaian Berlebih', 'Tekanan Berlebihan'],
                    'Kebocoran disekitar steam' : ['Tekanan Berlebihan','Packed tidak sesuai','Packed Box Kendor'],
                    'Pressure Drop berlebihan' : ['Tekanan Berlebihan','Valve dibawah ukuran'],
                    'Open/Close Terlalu Cepat' :[],
                    'Open/Close Terlalu Lambat' : ['Valve dibawah ukuran'],
                }
            },
            
            #Aturan Pilot
            'Control Valve Pilot Actuated': {
                'Penyebab': ['Terdapat Kotoran dalam valve seat', 'Lecet', 'Kerusakan Mekanik', 'Pilot Port Tersumbat', 'Tekanan Pada Pilot Berlebihan', 'Pilot Kehilangan Tekanan'],
                'Permasalahan': {
                    'Valve Fails To Open': ['Terdapat Kotoran dalam valve seat', 'Lecet', 'Kerusakan Mekanik', 'Pilot Port Tersumbat', 'Pilot Kehilangan Tekanan'],
                    'Valve Fails To Close': ['Terdapat Kotoran dalam valve seat', 'Lecet', 'Kerusakan Mekanik', 'Pilot Port Tersumbat', 'Tekanan Pada Pilot Berlebihan'],
                    'Kebocoran Melalui Valve': ['Terdapat Kotoran dalam valve seat', 'Kerusakan Mekanik', 'Pilot Port Tersumbat', 'Pilot Kehilangan Tekanan'],
                    'Kebocoran disekitar steam':[],
                    'Open/Close Terlalu Cepat' : ['Tekanan Pada Pilot Berlebihan'],
                    'Open/Close Terlalu Lambat' : ['Pilot Kehilangan Tekanan'],
                }
            },
            #Aturan Solenoid
            'Control Valve Solenoid Actuated': {
                'Penyebab': ['Korosi', 'Terdapat Kotoran dalam valve seat', 'Lecet', 'Tekanan Berlebihan', 'Kerusakan Mekanik', 'Kegagalan Solenoid', 'Pengkabelan Solenoid cacat', 'Type Valve Tidak Sesuai (NO, NC)'],
                'Permasalahan': {
                    'Valve Fails To Open': ['Korosi', 'Terdapat Kotoran dalam valve seat', 'Lecet', 'Tekanan Berlebihan', 'Kerusakan Mekanik', 'Kegagalan Solenoid', 'Pengkabelan Solenoid cacat', 'Type Valve Tidak Sesuai (NO, NC)'],
                    'Valve Fails To Close': ['Kegagalan Solenoid', 'Pengkabelan Solenoid cacat'],
                    'Kebocoran Melalui Valve': ['Korosi', 'Terdapat Kotoran dalam valve seat', 'Tekanan Berlebihan', 'Kerusakan Mekanik'],
                    'Kebocoran disekitar steam' : ['Tekanan Berlebihan'],
                    'Pressure Drop berlebihan' : [],
                    'Open/Close Terlalu Cepat' : [],
                    'Open/Closes To Slow' : ['Tekanan Berlebihan'],
                }
            }
        }
    #Mendefinisikan pertanyaan tipe valve
    def Pilihan_Jenis_ControlValve(self):
        print("####### Expert System Pada Maintenance Control Valve #######")
        print("------------------------------------------------------------")
        print(" Pilih Type Control Valve yang Ingin Anda Maintenance:")
        print("____________________________________________________________")
        print("1. Control Valve Manually Actuated")
        print("____________________________________________________________")
        print("2. Control Valve Pilot Actuated")
        print("____________________________________________________________")
        print("3. Control Valve Solenoid Actuated")
        print("____________________________________________________________")

        #Mendeklarasikan Input Pilihan
        Pilihan_Pengguna = input("Masukkan Nomor Control Valve Yang Di (1/2/3): ")
        return {
            '1': 'Control Valve Manually Actuated',
            '2': 'Control Valve Pilot Actuated',
            '3': 'Control Valve Solenoid Actuated'
        }.get(Pilihan_Pengguna, None)
        
    #Mendefinisikan pertanyaan gejala
    def Pertanyaan_Penyebab_UntukPengguna(self, valve_type):
        Penyebab = []
        print(f" Cek Kondisi {valve_type} ")
        for Penyebab in self.rules[valve_type]['Penyebab']:
            Tanggapan = input(f"Apakah {Penyebab} ? (Ya/Tidak): ").strip().lower()
            if Tanggapan == 'Ya':
                Penyebab.append(Penyebab)
        return Penyebab

    def Penentuan_Permasalahan(self, valve_type, Penyebab):
        for case, case_symptoms in self.rules[valve_type]['Permasalahan'].items():
            if all(Penyebab in Penyebab for Penyebab in case_symptoms):
                return case
        return "Unable to determine the Control Valve Problems."

# Menjalankan Sistem Pakar
Proses_Analisi_Kesalahan = ControlValveFailureAnalysis()

#Menampilkan
valve_type = Proses_Analisi_Kesalahan.Pilihan_Jenis_ControlValve()
if valve_type is not None:
    Penyebab = Proses_Analisi_Kesalahan.Pertanyaan_Penyebab_UntukPengguna(valve_type)
    Kemungkinan_Permasalahan = Proses_Analisi_Kesalahan.Penentuan_Permasalahan(valve_type, Penyebab)
    print("Kesalahan Yang Di Temukan Pada Control Valve Ini Adalah ....:", Kemungkinan_Permasalahan)
else:
    print("Tidak Di Temukan Pilihan, Coba Pilih Ulang")
