import time
import os

chat_tree = {
    "Start": {
        "text": "Hai, Devi... Masih ingat aku nggak? Dulu kita pernah satu seminar bareng, yang bahas 'Future of AI' itu loh...",
        "Choice": {
            "[Kirim Sekarang]": "respon_1",
            "[Jangan Kirim]": "respon_2"
        }
    },
    "respon_1": {
        "text": "Hai! Hmm... Future of AI... Oh! Kamu yang duduk di barisan kedua waktu itu, kan? Yang tanya tentang etika AI? Aku ingat! 😄",
        "Choice": {
            "Iya, itu aku! Wah, senang banget kamu masih ingat detailnya! 😊": "respon_3",
            "Hah, kamu ingat! Aku jadi deg-degan nih 😅 Kirain udah lupa.": "respon_4"
        }
    },
    "respon_2": {
        "text": "Dennis menghapus pesan itu. Mungkin belum waktunya. Tapi di dalam hati, Dennis tahu akan menyesal jika tak pernah mencoba... 😔",
        "Choice": None
    },
    # Jalur 1A
    "respon_3": {
        "text": "Hehe, tentu dong! Pertanyaanmu menarik waktu itu. Jadi, gimana kabarmu, Dennis? Makin sibuk sama AI juga nih? 😉",
        "Choice": {
            "Baik, makin sibuk sama kuliah, Devi. Kamu sendiri gimana kabarnya?": "respon_5", #Ke Jalur 2A
            "Kangen seminar kemarin. Seru banget ya! Obrolannya nempel di kepala.": "respon_6" #Ke Jalur 2B
        }
    },
    #Jalur 1B
    "respon_4": {
        "text": "Hahaha, santai aja kali. Emang kenapa deg-degan gitu? Takut aku tagih utang budi? 😂",
        "Choice": {
            "Karena aku suka kamu dari dulu 😳 Entah kenapa, langsung jatuh hati di seminar itu.": "ending_1",
            "Ah, soalnya baru pertama kali nyapa kamu lagi setelah sekian lama. Agak canggung gitu.": "respon_7" #Ke Jalur 2A
        }
    },
    "respon_7": {
        "text": "Hehe iya ya, baru sekarang ngobrol lagi. Tapi aku seneng kok kamu nyapa duluan. Jadi, gimana kabarmu, Dennis? Udah nggak deg-degan lagi kan? 😉",
        "Choice": {
            "Aku baik, walaupun kuliah lagi padet banget hehe. Kamu gimana? Ikut organisasi juga nggak?": "respon_12",
            "Masih waras sih, meskipun tugas udah mulai numpuk 🙃 Kamu sendiri gimana? Aman terkendali?": "respon_13"
        }
    },
    "respon_12": {
        "text": "Wahh sama dong! Aku juga lagi dikejar tugas, rasanya pengen nangis di pojokan kampus 🙃",
        "Choice": {
            "Mau bareng nugas nggak? Biar lebih ringan, bisa call atau ketemu sekalian, biar ada temen struggling-nya.": "respon_14",
            "Hehe, semangat ya. Kalau capek, boleh curhat ke aku kok :) Aku siap jadi pendengar setia.": "respon_15"
        }
    },
    "respon_14": {
        "text": "Hmm... bisa juga tuh idenya! Aku kadang lebih semangat kalau nugas bareng orang lain. Call dulu aja kali ya? Siapa tau malah seru, terus tugasnya kelar. 😄",
        "Choice": {
            "Oke, aku chat kamu malam ini ya, Devi. Kita tentuin bareng enaknya kapan.": "ending_5",
            "Siap! Tapi kamu jangan kaget ya kalo aku banyak ngeluh dan tiba-tiba nyanyi di tengah nugas 😅": "ending_6"
        }
    },
    "respon_15": {
        "text": "Hehe makasih yaa, Dennis. Kamu baik banget deh 🥹 Tapi aku orangnya suka cerita panjang lho, takutnya kamu bosen dengerin keluh kesahku 😅",
        "Choice": {
            "Justru aku suka dengerin. Gak apa-apa cerita panjang juga, aku siap mendengarkan kok.": "ending_3",
            "Curhat sambil ngopi bareng enak kali ya? :) Biar lebih santai dan fokus.": "respon_16"
        }
    },
    "respon_16": {
        "text": "Hihi bisa juga tuh! Tapi kamu yang traktir ya, aku maunya yang ada latte art-nya! 😆",
        "Choice": {
            "Deal! Yang penting kamu senang dan bisa curhat dengan nyaman.": "ending_2",
            "Oke deh, asal kamu cerita yang jujur semua, dari A sampai Z, gak ada yang ditutup-tutupin yaa 😜": "ending_6"
        }
    },
    "respon_13": {
        "text": "Hahaha, aku juga masih 'aman terkendali' sih, tapi kadang suka mikir ini hidup atau kejar tayang deadline ya 🫠 Kamu kuliah juga, kan? Gimana rasanya jadi mahasiswa akhir? 😫",
        "Choice": {
            "Sama! Ini fase terberat kayaknya. Mau ngopi bareng nggak, biar bisa saling menguatkan?": "respon_14",
            "Yang penting masih bernapas, Devi. Hehe. Kalau capek, istirahat dulu ya. Jangan dipaksain.": "respon_15"
        }
    },
    # jalur 2A
    "respon_5": {
        "text": "Aku juga baik, walaupun tugas lagi numpuk banget hehe. Rasanya pengen teleportasi aja ke pantai! 🏝️",
        "Choice": {
            "Mau bareng ngerjain tugas nggak? Biar lebih ringan dan mungkin bisa lebih cepat selesai.": "respon_8", #Ke Jalur 3A
            "Wah, semangat ya! Kalau capek, jangan lupa istirahat. Kesehatan nomor satu loh.": "respon_9" #Ke Jalur 3B
        }
    },
    # jalur 2B
    "respon_6": {
        "text": "Iyaaa! Asik banget kan. Obrolannya juga berkualitas. Aku seneng banget bisa kenalan sama kamu dan ngobrol bareng di sana.",
        "Choice": {
            "Aku juga. Gimana kalau kita ngopi bareng weekend ini? Bisa lanjutin obrolan seru kemarin.": "respon_10", #Ke Jalur 3A
            "Aku masih simpen fotonya loh, waktu kita selfie di depan panggung. Mau aku kirim?": "respon_11" #Ke jalur 3B
        }
    },
    "respon_8": {
        "text": "Hmm... ide bagus! Kadang aku lebih semangat kalau nugas bareng 😄 Kita call aja dulu atau langsung ketemu di kafe kampus?",
        "Choice": {
            "Call dulu aja kali ya, biar nggak canggung pas ketemu. Kita kenalan lebih dalam dulu.": "ending_5",
            "Ketemu langsung aja, sekalian cari suasana baru biar nggak suntuk di kosan terus :)": "ending_2"
        }
    },
    "respon_9": {
        "text": "Hehe makasih! Kamu perhatian banget deh, Dennis. Tapi jangan cuma nyemangatin dong 😅 Ada yang lain nggak? Hihi.",
        "Choice": {
            "Maksudnya...? 😳 Jangan bikin aku salah paham dong, Devi.": "respon_17",
            "Hehe iya, lain kali aku traktir deh biar makin semangat, gimana? Mau makan apa? 😄": "respon_16"
        }
    },
    # Jalur 3A
    "respon_10": {
        "text": "Hmm… boleh sih, kayaknya seru! Aku suka banget kopi. Chat aku lagi nanti ya, kita atur waktunya yang pas :)",
        "Choice": {
            "Siap, nanti aku kabari ya. Seneng banget kamu mau. Aku udah nggak sabar! 😊": "ending_2"
        }
    },
    # Jalur 3B
    "respon_11": {
        "text": "Oh, kamu masih simpan? Wah, makasih banyak ya Dennis. Kamu baik banget. Jujur aku seneng bisa kenal kamu. Tapi aku lagi nggak fokus buat kenalan lebih deket sekarang, lagi banyak banget yang harus dipikirin 😅",
        "Choice": {
            "Gpp kok. Kalau kamu butuh teman cerita atau sekadar dengerin, aku ada kok. Kapan pun itu.": "ending_3",
            "Oke, aku ngerti kok. Semoga semua lancar ya buat kamu. Semangat!": "ending_4"
        }
    },
    "respon_17": {
        "text": "Hahaha maksudku, ayo dong ngobrol lagi kayak dulu. Aku suka cara kamu cerita, lucu aja gitu. Jadi, mau cerita apa lagi nih?",
        "Choice": {
            "Aku juga suka ngobrol sama kamu, Devi. Gimana kalau kita call nanti malem aja? Biar lebih santai.": "ending_5",
            "Makasih ya... aku jadi makin semangat karena kamu. Kamu juga harus semangat ya!": "ending_3"
        }
    },

    # Ending
    "ending_1": {
        "text": "Oh… ehm… Dennis, kita belum terlalu kenal secara personal. Tapi makasih udah jujur ya. Untuk sekarang, kita temenan dulu aja ya :) Aku menghargai kejujuranmu. [💔 Friendzone Ending]",
        "Choice": None
    },
    "ending_2": {
        "text": "(Dennis dan Devi mulai sering chatting, bertukar cerita, dan akhirnya bertemu untuk pertama kalinya di kedai kopi kecil dekat kampus. Hari itu, obrolan mereka mengalir begitu saja, seolah sudah kenal lama. Ini baru permulaan...) [💕 Happy Ending]",
        "Choice": None
    },
    "ending_3": {
        "text": "(Dennis dan Devi tetap saling follow di media sosial, kadang bertukar pesan ringan. Dennis sering menawarkan diri untuk mendengar, tapi Devi selalu menjaga jarak tak kasat mata. Mereka berteman, tapi Dennis tahu, itu bukan yang ia inginkan.) [🙂 Friendzone Ending]",
        "Choice": None
    },
    "ending_4": {
        "text": "(Devi menghargai Dennis sebagai teman, dan Dennis pun menerimanya dengan tulus. Ia tahu, memaksakan perasaan hanya akan memperburuk. Siapa tahu, waktu akan mengubah banyak hal. Tapi untuk sekarang, hati itu belum tercipta untuk Dennis.) [🌤️ Ending Teman Saja]",
        "Choice": None
    },
    "ending_5": {
        "text": "(Dennis dan Devi mulai sering ngobrol lewat chat dan call. Ternyata, mereka nyambung banget, dari nugas bareng, ngobrol soal musik, sampai bahas masa depan. Setiap malam, call mereka bisa berjam-jam, diisi tawa dan cerita. Sebuah ikatan baru perlahan terjalin...) [💕 Happy Ending]",
        "Choice": None
    },
    "ending_6": {
        "text": "(Percakapan berlanjut dengan tawa dan canda. Dennis dan Devi menemukan banyak kesamaan, dan obrolan mereka tak pernah terasa membosankan. Ini bukan lagi tentang seminar. Ini awal yang baru untuk mereka berdua.) [💕 Happy Ending]",
        "Choice": None
    }
}

def clear_screen():
    # Periksa sistem operasi untuk perintah clear screen yang tepat
    os.system('cls' if os.name == 'nt' else 'clear')

def jalankan_chat(tree):
    node = "Start"
    while True:
        current = tree[node]
        clear_screen() # Bersihkan layar setiap kali dialog baru muncul

        print("\nDevi:") # Indikator siapa yang bicara
        for char in current["text"]:
            print(char, end='', flush=True) # Efek mengetik
            time.sleep(0.02) # Jeda kecil antar huruf
        print("\n")

        if not current.get("Choice"):
            print("\n[Chat selesai.]")
            break

        choices = list(current["Choice"].keys())
        for i, choice in enumerate(choices):
            print(f"{i + 1}. {choice}")

        while True:
            try:
                user_input = input("\nPilih opsi (angka): ") # Input di sini agar tidak tercampur efek mengetik
                user_input = int(user_input)
                if 1 <= user_input <= len(choices):
                    break
                else:
                    print("Pilihan tidak valid. Silakan masukkan angka yang benar.")
            except ValueError:
                print("Masukan tidak valid. Harap masukkan angka.")

        selected_choice = choices[user_input - 1]
        node = current["Choice"][selected_choice]

    # Opsi untuk bermain lagi setelah ending
    while True:
        main_lagi = input("Apakah kamu ingin bermain lagi? (ya/tidak): ").lower()
        if main_lagi == "ya":
            jalankan_chat(tree) # Rekursif untuk memulai ulang
            break # Keluar dari loop setelah selesai bermain lagi
        elif main_lagi == "tidak":
            print("Terima kasih sudah bermain! Sampai jumpa.")
            break
        else:
            print("Input tidak valid. Silakan ketik 'ya' atau 'tidak'.")

# Jalankan:
jalankan_chat(chat_tree)