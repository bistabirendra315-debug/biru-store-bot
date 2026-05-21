from telegram import (
    Update,
    ReplyKeyboardMarkup,
    KeyboardButton
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = "8811226656:AAH73jr-w5iPPa_8udxDmEGOXkI3RnEJvkY"

verified_users = set()

products = [
    "DRIP CLIENT NON ROOT + ROOT",
    "DRIP CLIENT PC",
    "DRIP CLIENT 8BP NON ROOT",
    "HG CHEAT NON ROOT + ROOT",
    "BR MODZ PC",
    "BR MODZ ROOT",
    "FLUORITE IOS",
    "HAXX-CKER PRO ROOT",
    "HEX BLADE ROOT",
    "HIKARI MODZ ROOT",
    "MIGUL IPHONE IOS",
    "NEO STRIKE ROOT",
    "PATO TEAM NON ROOT",
    "PRIME HOOK NON ROOT",
    "XYZ CHEATS ROOT"
]


async def show_products(update, context):
    keyboard = [[p] for p in products]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "🔥 Welcome to BIRU_BLOODLINE STORE\n\n🛒 Select Product:",
        reply_markup=reply_markup
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if user_id in verified_users:
        await show_products(update, context)
        return

    button = KeyboardButton(
        "📞 Verify Number",
        request_contact=True
    )

    keyboard = [[button]]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        one_time_keyboard=True
    )

    await update.message.reply_text(
        "📱 Please verify your phone number first.",
        reply_markup=reply_markup
    )


async def handle_contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    phone = update.message.contact.phone_number

    verified_users.add(user_id)

    await update.message.reply_text(
        f"✅ Number Verified\n\n📞 {phone}"
    )

    await show_products(update, context)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    await update.message.reply_text(
        f"✅ You selected:\n\n{text}\n\nDuration menu coming next..."
    )


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.CONTACT, handle_contact))
app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        handle_message
    )
)

print("Bot Running...")
app.run_polling()
