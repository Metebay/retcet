import openai
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# OpenAI API anahtarınızı buraya girin
openai.api_key = "YOUR_OPENAI_API_KEY"

# /start komutuna yanıt
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Merhaba! Ben bir yapay zeka destekli sohbet botuyum. Bana bir şeyler sorabilirsiniz.")

# Yapay zeka ile sohbet fonksiyonu
def chat_with_ai(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text  # Kullanıcının mesajı

    # GPT-3 ile sohbet etme
    response = openai.Completion.create(
        engine="text-davinci-003",  # GPT-3 modelini kullanıyoruz
        prompt=user_message,       # Kullanıcının mesajını modele gönderiyoruz
        max_tokens=150,            # Yanıtın uzunluğunu sınırlıyoruz
        temperature=0.7,           # Yaratıcılığı belirliyoruz
        top_p=1,                   # Yanıt çeşitliliğini ayarlıyoruz
        frequency_penalty=0.5,     # Tekrarlanan cevapları azaltıyoruz
        presence_penalty=0.5      # Yeni konulara geçmeyi teşvik ediyoruz
    )

    # GPT-3'ün cevabını alıyoruz
    ai_response = response.choices[0].text.strip()

    # Kullanıcıya cevabı gönderiyoruz
    update.message.reply_text(ai_response)

# Ana fonksiyon
def main():
    token = '7412031464:AAEtV7d8wuqRBLgCytIdF6ormEnKwPOC70s'  # Telegram bot tokeninizi buraya ekleyin

    # Updater ve Dispatcher ayarları
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher

    # Komutları ekleyin
    dispatcher.add_handler(CommandHandler("start", start))

    # Mesajları AI'ye yönlendiren mesaj handler'ı ekleyin
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, chat_with_ai))

    # Botu başlatın
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
