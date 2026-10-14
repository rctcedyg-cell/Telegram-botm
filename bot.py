import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

AUTO_REPLIES = {
    "تعرفون احد يحل": "إيه أنا أحل! 👋 خبرة في كل المواد وضمان - تواصل خاص @vimlo0",
    "تعرف احد يحل": "إيه أنا أحل! 👋 خبرة في كل المواد وضمان - تواصل خاص @vimlo0",
    "احد يحل واجبات": "أنا أحل الواجبات كلها 🔥 سريع ومضمون - كلمني @vimlo0",
    "يحل واجب": "حياك! 👋 أحل جميع الواجبات باحترافية وضمان - تواصل خاص @vimlo0",
    "واجب هندسة": "متخصص في واجبات الهندسة 🔧 @vimlo0",
    "حل مسائل": "أحل المسائل مع خطوات الحل كاملة ✅ @vimlo0",
    "تلخيص": "أسوي تلخيص مرتب 📝 @vimlo0",
    "بوربوينت": "أسوي عرض بوربوينت احترافي 🎨 @vimlo0",
    "مشروع تخرج": "أساعدك في مشروع التخرج 🎓 @vimlo0",
}

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return
    text = update.message.text.lower()
    for keyword, reply in AUTO_REPLIES.items():
        if keyword in text:
            await update.message.reply_text(reply)
            break

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))
app.run_polling()
