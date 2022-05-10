from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


default_lang = "en"

start_message_text = """
Assalomu alaykum {} \U0001F60E

**▶️GoTarjima [Bot]** - Telegram ijtimoiy tarmog'ida foydalanuvchilarga qulaylik yaratish uchun chiqarilgan Google Tarjimon Boti 🌐

/language - Tilni tanlash
/help - Qo'llanma
/developer - Aloqa"""

start_message_reply_markup = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(  
                        "🔍 Inline izlash",
                        switch_inline_query_current_chat=" "
                    )
        ],
        [
            InlineKeyboardButton(
                "🔖 Yordam",  callback_data="help")
        ],
    ]
)

help_markup = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("🔙 Orqaga", callback_data="back")],
            ]
        )

credits = """Dasturchi 🧑‍💻
 • @Django_Programmer
 • Sizga mukammal tarzda bot yaratib berishimiz mumkin
 • Iltimos lichkaga bot kodini sorab yozmang!

Kanal 💡
 • @ilova_bozor"""

help_text = """
**🎫 Buyruqlar**

⚜️ /tr (til kodi) => reply orqali
 
⚜️ /tr (til kodi) (xabar) => tezkor tarjima

⚜️ @GoTarjimonBot (til kodi) (xabar) => inline rejim

ℹ️ /language buyrug'i orqali tillar ro'yhatini ko'rishingiz mumkin
"""

developer_text = """
**💌 Savol va takliflar uchun dasturchiga muroojat qiling ☎️**

__⚠️Eslatma: Siz dasturchi bilan aloqadasiz qo'pol va haqoratli so'zlar ishlatmang__

👨‍💻Dasturchi: @TheKing_World
"""

language_text = """
**Tillar**

__Tarjima qilmoqchi bo'lgan tilni tanlang.__

•/lang (til kodi) 

Masalan: ```/lang uz``` 

Til kodlari ro'yxati: https://cloud.google.com/translate/docs/languages


"""

error_group_no_reply = """Tarjima qilish uchun xabarga javob bering"""

error_ocr_no_reply = """matnni olish uchun fotosuratga javob bering"""

lang_saved_message = """Tarjima tili {}ga muvaffaqiyatli o'zgartirildi! """

ocr_message_text = """```rasmdagi matn:``` \n\n {}"""

translate_string_one = """**\ud83c\udf10 Tarjima**:\n\n```{}```\n\n**🔍 Aniqlangan til:** {} \n\n **Tarjima qilingan**: {}"""

translate_string_two = """**\ud83c\udf10 Tarjima**:\n\n```{}```\n\n**🔍 Aniqlangan til:** {}"""

inline_text_string_one = """So'z tarjima qilindi {} dan {} ga"""
