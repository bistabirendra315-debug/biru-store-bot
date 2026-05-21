import os
import json
import requests
from datetime import datetime

from telegram import (
    Update,
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove
)

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# =========================
# CONFIG
# =========================

TOKEN = "8811226656:AAH73jr-w5iPPa_8udxDmEGOXkI3RnEJvkY"  # आफ्नो bot token राख्ने

ADMIN_ID = 8823622915
SUPPORT_USERNAME = "@BIRU_BLOODLINE"

ESEWA_NUMBER = "9716110851"
QR_IMAGE = "esewa.jpg"

API_URL = "https://adminpanels.shop/api/reseller_v1.php"
API_KEY = "df65e8c151bbd0ca52c24a106190b582"

DB_FILE = "database.json"

# =========================
# DATABASE
# =========================

def load_db():
    if not os.path.exists(DB_FILE):
        return {
            "verified": [],
            "balance": {},
            "orders": {},
            "pending_deposits": {},
            "selected_product": {}
        }

    with open(DB_FILE, "r") as f:
        return json.load(f)


db = load_db()


def save_db():
    with open(DB_FILE, "w") as f:
        json.dump(db, f, indent=4)
# =========================
# PRODUCTS
# =========================
products = {

    "XYZ CHEATS ROOT": {
        "pid": 66,
        "prices": {
            "3 Days": 150,
            "7 Days": 300,
            "15 Days": 550,
            "30 Days": 999
        }
    },

    "MIGUL IPHONE IOS": {
        "pid": 69,
        "prices": {
            "1 Day Basic": 120,
            "7 Days Basic": 400,
            "30 Days Basic": 700,
            "1 Day PRO": 200,
            "7 Days PRO": 600,
            "30 Days PRO": 1000,
            "Esgin Gbox CERTIFICATE": 400
        }
    },

    "HG CHEATS NONROOT+ROOT": {
        "pid": 65,
        "prices": {
            "1 Day Root + Nonroot": 40,
            "7 Days Root + Nonroot": 120,
            "10 Days Root + Nonroot": 135,
            "30 Days Root + Nonroot": 299
        }
    },

    "HIKARI MOD FF ROOT": {
        "pid": 72,
        "prices": {
            "3 Days": 60,
            "7 Days": 120,
            "15 Days": 200,
            "30 Days": 350
        }
    },

    "NEO STRIKE ROOT": {
        "pid": 70,
        "prices": {
            "1 Day": 70,
            "7 Days": 300,
            "14 Days": 500
        }
    },

    "PATO TEAM NONROOT + ROOT": {
        "pid": 54,
        "prices": {
            "3 Days All Colours Mix": 249,
            "7 Days All Colours Mix": 450,
            "15 Days All Colours Mix": 620,
            "30 Days All Colours Mix": 1060
        }
    },

    "PRIME HOOK NONROOT": {
        "pid": 48,
        "prices": {
            "1 Day Nonroot": 80,
            "3 Days Nonroot": 149,
            "7 Days NonRoot": 319,
            "10 Days Nonroot": 349
        }
    },

    "BR MODZ PC": {
        "pid": 49,
        "prices": {
            "1 Day Pc Aim Silent": 50,
            "10 Days Pc Aim Silent": 250,
            "30 Days Pc Aim Silent": 499,
            "1 Day Pc Bypass + Silent": 79,
            "10 Days Pc Bypass + Silent": 279,
            "30 Days Pc Bypass + Silent": 599
        }
    },

    "BR MODZ ROOT": {
        "pid": 67,
        "prices": {
            "1 Day": 50,
            "7 Days": 150,
            "15 Days": 300,
            "30 Days": 400
        }
    },

    "DRIPCLIENT 8BP NONROOT": {
        "pid": 59,
        "prices": {
            "1 Day": 49,
            "7 Days": 129,
            "30 Days": 299
        }
    },

    "DRIPCLIENT ROOT": {
        "pid": 63,
        "prices": {
            "7 Days ROOT": 149,
            "30 Days ROOT": 350
        }
    },

    "DRIPCLIENT NONROOT": {
        "pid": 62,
        "prices": {
            "1 Day NONROOT": 49,
            "3 Days NONROOT": 75,
            "7 Days NONROOT": 149,
            "15 Days NONROOT": 250,
            "30 Days NONROOT": 350
        }
    },

    "DRIPCLIENT PC": {
        "pid": 44,
        "prices": {
            "1 Day PC AIMKILL": 79,
            "7 Days PC AIMKILL": 199,
            "15 Days PC AIMKILL": 349,
            "30 Days PC AIMKILL": 449
        }
    },

    "FLUORITE IOS": {
        "pid": 58,
        "prices": {
            "1 Day Fluorite FF": 199,
            "7 Days Fluorite FF": 599,
            "30 Days Fluorite FF": 1249,
            "Esign Gbox Certificate For iOS": 419
        }
    },

    "HAXX-CKER PRO ROOT": {
        "pid": 64,
        "prices": {
            "10 Days": 550
        }
    },

    "HEX BLADE ROOT": {
        "pid": 71,
        "prices": {
            "1 Day": 35,
            "10 Days": 130,
            "20 Days": 225
        }
    }
}


# =========================
# MENUS
# =========================

def main_menu():

    return ReplyKeyboardMarkup(
        [
            ["🛍 Buy Products"],
            ["💰 Deposit", "👛 My Balance"],
            ["📦 My Orders", "🆘 Support"]
        ],
        resize_keyboard=True
    )


def back_menu():
    return ReplyKeyboardMarkup(
        [["⬅️ Back"]],
        resize_keyboard=True
    )
# =========================
# FUNCTIONS
# =========================

async def show_home(update, user):

    uid = str(user.id)
    balance = db["balance"].get(uid, 0)

    text = f"""
🏪 BIRU_BLOODLINE STORE

👋 Welcome, {user.first_name}

━━━━━━━━━━━━━━━
👤 User ID: {user.id}
💰 Wallet Balance: ₹{balance}
━━━━━━━━━━━━━━━

💎 Premium Products
⚡ Instant Auto Delivery
🔒 Secure Purchase System
💳 Deposit Available

━━━━━━━━━━━━━━━
👇 Select Option Below
"""

    await update.message.reply_text(
        text,
        reply_markup=main_menu()
    )


# =========================
# START
# =========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user
    uid = str(user.id)

    if uid in db["verified"]:
        await show_home(update, user)
        return

    button = KeyboardButton(
        text="📞 Verify Number",
        request_contact=True
    )

    keyboard = [[button]]

    await update.message.reply_text(
        "🔐 IDENTITY CHECK NEEDED\n\nTap below to verify.",
        reply_markup=ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True
        )
    )


# =========================
# VERIFY
# =========================

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user
    uid = str(user.id)

    if uid not in db["verified"]:
        db["verified"].append(uid)

    if uid not in db["balance"]:
        db["balance"][uid] = 0

    save_db()

    await update.message.reply_text(
        "✅ Verification Complete!"
    )

    await show_home(update, user)

# =========================
# MESSAGE SYSTEM
# =========================

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text or ""
    user = update.effective_user
    uid = str(user.id)

    # ===================
    # BUY PRODUCTS
    # ===================

    if text == "🛍 Buy Products":

        keyboard = [[x] for x in products.keys()]
        keyboard.append(["⬅️ Back"])

        await update.message.reply_text(
            "🎮 Select Product",
            reply_markup=ReplyKeyboardMarkup(
                keyboard,
                resize_keyboard=True
            )
        )

    elif text in products:

        db["selected_product"][uid] = text
        save_db()

        keyboard = []

        for duration, price in products[text]["prices"].items():
            keyboard.append([f"{duration} - ₹{price}"])

        keyboard.append(["⬅️ Back"])

        await update.message.reply_text(
            f"🎮 {text}\n\nChoose Duration:",
            reply_markup=ReplyKeyboardMarkup(
                keyboard,
                resize_keyboard=True
            )
        )

    # ===================
    # DEPOSIT
    # ===================

    elif text == "💰 Deposit":

        db["pending_deposits"][uid] = True
        save_db()

        if os.path.exists(QR_IMAGE):

            with open(QR_IMAGE, "rb") as photo:
                await update.message.reply_photo(
                    photo=photo,
                    caption=(
                        f"💳 Deposit via eSewa\n\n"
                        f"Number: {ESEWA_NUMBER}\n\n"
                        f"Send Amount Example:\n500"
                    ),
                    reply_markup=back_menu()
                )

        else:
            await update.message.reply_text(
                f"eSewa Number:\n{ESEWA_NUMBER}\n\nEnter Amount:",
                reply_markup=back_menu()
            )

    elif text.isdigit() and uid in db["pending_deposits"]:

        amount = int(text)

        context.user_data["amount"] = amount

        await update.message.reply_text(
            f"💳 Pay ₹{amount}\n\n"
            f"eSewa Number:\n{ESEWA_NUMBER}\n\n"
            f"After Payment Send Screenshot",
            reply_markup=back_menu()
        )

    # ===================
    # SCREENSHOT DEPOSIT
    # ===================

    elif update.message.photo:

        amount = context.user_data.get("amount")

        if not amount:
            return

        file_id = update.message.photo[-1].file_id

        db["pending_deposits"][uid] = amount
        save_db()

        caption = f"""
💰 NEW DEPOSIT REQUEST

👤 User:
{user.first_name}

🆔 ID:
{uid}

💵 Amount:
₹{amount}

Approve:
YES {uid} {amount}
"""

        await context.bot.send_photo(
            chat_id=ADMIN_ID,
            photo=file_id,
            caption=caption
        )

        await update.message.reply_text(
            "✅ Deposit Request Sent To Admin"
        )

    # ===================
    # ADMIN APPROVE
    # ===================

    elif text.startswith("YES") and user.id == ADMIN_ID:

        try:
            _, target_uid, amount = text.split()

            amount = int(amount)

            current = db["balance"].get(
                target_uid,
                0
            )

            db["balance"][target_uid] = current + amount

            save_db()

            await context.bot.send_message(
                chat_id=target_uid,
                text=(
                    f"✅ Deposit Approved\n\n"
                    f"Added: ₹{amount}\n"
                    f"Balance: ₹{db['balance'][target_uid]}"
                )
            )

            await update.message.reply_text(
                "✅ Approved"
            )

        except:
            await update.message.reply_text(
                "❌ Error"
            )

    # ===================
    # MY BALANCE
    # ===================

    elif text == "👛 My Balance":

        balance = db["balance"].get(uid, 0)

        await update.message.reply_text(
            f"💰 Wallet Balance:\n₹{balance}"
        )

    # ===================
    # SUPPORT
    # ===================

    elif text == "🆘 Support":

        await update.message.reply_text(
            f"Support:\n{SUPPORT_USERNAME}"
        )

    # ===================
    # ORDER HISTORY
    # ===================

    elif text == "📦 My Orders":

        orders = db["orders"].get(uid, [])

        if not orders:

            await update.message.reply_text(
                "❌ No Orders Found"
            )

        else:

            await update.message.reply_text(
                "\n\n".join(orders)
            )

    # ===================
    # BUY SYSTEM + API
    # ===================

    elif "₹" in text:

        product = db["selected_product"].get(uid)

        if not product:
            return

        duration = text.split(" - ")[0]

        price = products[product]["prices"][duration]

        balance = db["balance"].get(uid, 0)

        if balance < price:

            await update.message.reply_text(
                f"❌ Not Enough Balance\n\nNeed ₹{price}"
            )
            return

        pid = products[product]["pid"]

        data = {
            "api_key": API_KEY,
            "action": "buy",
            "product_id": pid,
            "duration": duration
        }

        try:

            r = requests.post(
                API_URL,
                data=data
            )

            res = r.json()

            if res["status"] == "success":

                db["balance"][uid] -= price

                key = res["key"]

                order = (
                    f"✅ Purchased\n"
                    f"📦 {product}\n"
                    f"⏳ {duration}\n"
                    f"💰 ₹{price}\n"
                    f"🔑 {key}\n"
                    f"📅 {datetime.now().strftime('%d %b %Y | %I:%M %p')}"
                )

                db["orders"].setdefault(
                    uid,
                    []
                ).append(order)

                save_db()

                await update.message.reply_text(
                    f"""
✅ Purchase Successful

📦 Product:
{product}

⏳ Duration:
{duration}

💰 Deducted:
₹{price}

💳 Remaining:
₹{db["balance"][uid]}

🔑 KEY:
{key}
"""
                )

            else:

                await update.message.reply_text(
                    f"❌ {res.get('msg')}"
                )

        except Exception as e:

            await update.message.reply_text(
                f"❌ API Error\n{e}"
            )

    # ===================
    # BACK
    # ===================

    elif text == "⬅️ Back":

        await show_home(
            update,
            user
        )


# =========================
# RUN BOT
# =========================

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(
    CommandHandler("start", start)
)

app.add_handler(
    MessageHandler(
        filters.CONTACT,
        contact
    )
)

app.add_handler(
    MessageHandler(
        filters.TEXT | filters.PHOTO,
        message
    )
)

import asyncio

print("Bot Running...")

try:
    loop = asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

app.run_polling()
