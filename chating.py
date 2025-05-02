chat_tree = {
    "Start": {
        "text": "Hai, Devi... Masih ingat aku nggak?",
        "Choice": {
            "[Kirim Sekarang]": "respon_1",
            "[Jangan Kirim]": "respon_2"
        }
    },
    "respon_1": {
        "text": "Hai! Hmm... Kamu yang duduk di barisan kedua waktu seminar, kan? :)",
        "Choice": {
            "Iya, itu aku! Senang kamu masih ingat :)": "respon_3",
            "Hah, kamu ingat! Aku jadi deg-degan nih 😅": "respon_4"
        }
    },
    "respon_2": {
        "text": "Dennis menghapus pesan itu. Mungkin belum waktunya. Tapi di dalam hati, Dennis tahu akan menyesal jika tak pernah mencoba...",
        "Choice": None
    },
    # Jalur 1A
    "respon_3": {
        "text": "Hehe, tentu dong. Jadi, gimana kabarmu, Dennis?",
        "Choice": {
            "Baik, makin sibuk sama kuliah. Kamu sendiri?": "respon_5", #Ke Jalur 2A
            "Kangen seminar kemarin. Seru banget ya!": "respon_6" #Ke Jalur 2B
        }
    },
    #Jalur 1B
    "respon_4": {
        "text": "Hehe, santai aja. Emang kenapa deg-degan? 😄",
        "Choice": {
            "Karena aku suka kamu dari dulu 😳": "ending_1",
            "Ah, soalnya baru pertama kali nyapa kamu lagi.": "respon_7" #Ke Jalur 2A
        }
    },
    "respon_7": {
        "text": "Hehe iya ya, baru sekarang ngobrol lagi. Tapi aku seneng kamu nyapa duluan. Jadi, gimana kabarmu, Dennis?",
        "Choice": {
            "Aku baik, walaupun kuliah lagi padet banget hehe. Kamu gimana?": "respon_12",
            "Masih waras sih, meskipun tugas udah mulai numpuk 🙃 Kamu sendiri?": "respon_13"
        }
    },
    "respon_12": {
        "text": "Wahh sama dong! Aku juga lagi dikejar tugas 🙃",
        "Choice": {
            "Mau bareng nugas nggak? Biar lebih ringan, bisa call atau ketemu sekalian.": "respon_14",
            "Hehe, semangat ya. Kalau capek, boleh curhat ke aku kok :)": "respon_15"
        }
    },
    "respon_14": {
        "text": "Hmm... bisa juga tuh. Aku kadang lebih semangat kalau nugas bareng orang. Call dulu aja kali ya? Siapa tau seru 😄",
        "Choice": {
            "Oke, aku chat kamu malam ini ya. Kita tentuin bareng.": "ending_5",
            "Siap! Tapi kamu jangan kaget ya kalo aku banyak ngeluh 😅": "ending_6"
        }
    },
    "respon_15": {
    "text": "Hehe makasih yaa. Kamu baik banget 🥹 Tapi aku orangnya suka cerita panjang lho, jangan bosen ya 😅",
    "Choice": {
        "Justru aku suka dengerin. Gak apa-apa cerita panjang juga.": "ending_3",  
        "Curhat sambil ngopi bareng enak kali ya? :)": "respon_16"
        }
    },
    "respon_16": {
    "text": "Hihi bisa juga tuh. Tapi kamu yang traktir ya 😆",
    "Choice": {
        "Deal! Yang penting kamu senang.": "ending_2",
        "Oke deh, asal kamu cerita yang jujur semua 😜": "ending_6"
    }
},
    # jalur 2A
    "respon_5": {
        "text": "Aku juga baik, walaupun tugas lagi numpuk banget hehe.",
        "Choice": {
            "Mau bareng ngerjain tugas nggak? Biar lebih ringan.": "respon_8", #Ke Jalur 3A
            "Wah, semangat ya! Kalau capek, jangan lupa istirahat.": "respon_9" #Ke Jalur 3B
        }
    },
    # jalur 2B
    "respon_6": {
        "text": "Iyaaa! Asik banget. Kita bisa sharing bareng. Aku seneng ngobrol sama kamu.",
        "Choice": {
            "Aku juga. Gimana kalau kita ngopi bareng weekend ini?": "respon_10", #Ke Jalur 3A
            "Aku masih simpen fotonya loh. Mau aku kirim?": "respon_11" #Ke jalur 3B
        }
    },
    "respon_8": {
    "text": "Hmm... ide bagus! Kadang aku lebih semangat kalau nugas bareng 😄 Kita call atau ketemu aja?",
    "Choice": {
        "Call dulu aja kali ya, biar nggak canggung pas ketemu.": "ending_5",
        "Ketemu langsung aja, sekalian cari suasana baru :)": "ending_2"
    }
},
    "respon_9": {
    "text": "Hehe makasih! Kamu perhatian banget. Tapi jangan cuma nyemangatin dong 😅",
    "Choice": {
        "Maksudnya...? 😳": "respon_17",
        "Hehe iya, lain kali aku traktir deh biar makin semangat 😄": "respon_16"
    }
},
    # Jalur 3A
    "respon_10": {
        "text": "Hmm… boleh sih, kayaknya seru! Chat aku lagi nanti ya, kita atur waktunya :)",
        "Choice": {
            "Siap, nanti aku kabari ya. Seneng banget kamu mau.": "ending_2"
        }
    },
    # Jalur 3B
    "respon_11": {
        "text": "Kamu baik banget, Dennis. Senang bisa kenal kamu. Tapi aku lagi nggak fokus buat kenalan lebih deket sekarang 😅",
        "Choice": {
            "Gpp kok. Kalau kamu butuh teman cerita, aku ada.": "ending_3",
            "Oke. Semoga semua lancar ya buat kamu.": "ending_4"
        }
    },
    "respon_17": {
    "text": "Haha maksudku, ayo dong ngobrol lagi kayak dulu. Aku suka cara kamu cerita.",
    "Choice": {
        "Aku juga suka ngobrol sama kamu. Kita call nanti malem, yuk?": "ending_5",
        "Makasih ya... aku jadi makin semangat karena kamu.": "ending_3"
    }
},

    # Ending
    "ending_1": {
        "text": "Oh… ehm… Dennis, kita belum terlalu kenal, tapi makasih udah jujur ya. Kita temenan dulu aja, ya :)",
        "Choice": None
    },
    "ending_2": {
        "text": "(Dennis dan Devi mulai sering chatting, bertukar cerita, dan akhirnya bertemu untuk pertama kalinya di kedai kopi kecil dekat kampus.) [💕 Happy Ending]",
        "Choice": None
    },
    "ending_3": {
        "text": "(Dennis dan Devi tetap saling follow, kadang bertukar pesan ringan. Tapi kamu bisa merasakan jarak tak kasat mata di antara mereka.) [🙂 Friendzone Ending]",
        "Choice": None
    },
    "ending_4": {
        "text": "(Devi menghargai Dennis sebagai teman, dan Dennis pun menerimanya dengan tulus. Siapa tahu, waktu akan mengubah banyak hal. Tapi untuk sekarang, hati itu belum tercipta.) [🌤️ Ending Teman Saja]",
        "Choice": None
    },
    "ending_5": {
        "text": "(Dennis dan Devi mulai sering ngobrol lewat chat dan call. Ternyata, mereka nyambung banget. Mulai dari nugas bareng, ngobrol soal musik, sampai bahas masa depan.) [💕 Happy Ending]",
        "Choice": None
    },
    "ending_6": {
        "text": "(Ini bukan lagi tentang seminar. Ini awal yang baru.) [💕 Happy Ending]",
        "Choice": None
    }
}

def jalankan_chat(tree):
    node = "Start"
    while True:
        current = tree[node]
        print("\n" + current["text"])  # Tampilkan teks dialog

        if not current.get("Choice"):
            print("\n[Chat selesai.]")
            break

        choices = list(current["Choice"].keys())
        for i, choice in enumerate(choices):
            print(f"{i + 1}. {choice}")

        while True:
            try:
                user_input = int(input("Pilih opsi (angka): "))
                if 1 <= user_input <= len(choices):
                    break
                else:
                    print("Pilihan tidak valid.")
            except ValueError:
                print("Masukkan angka yang benar.")

        selected_choice = choices[user_input - 1]
        node = current["Choice"][selected_choice]

# Jalankan:
jalankan_chat(chat_tree)
