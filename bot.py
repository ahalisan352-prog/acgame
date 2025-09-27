import requests
import time
from datetime import datetime

TELEGRAM_TOKEN = "7690340562:AAEpyw0by4zP40mXIH9K_XTsTeJR0FP1ZPQ"
CHAT_ID = "7313667208"

def send_welcome():
    message = "🤖 **ربات فروشگاه اکانت فعال شد!**\n\n"
    message += "✅ سیستم آماده دریافت اطلاعات:\n"
    message += "📝 ثبت‌نام‌های جدید\n"
    message += "🛒 درخواست‌های خرید\n"
    message += "📞 پیام‌های تماس\n\n"
    message += "⏰ زمان فعال‌سازی: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("✅ پیام فعال‌سازی ارسال شد")
        else:
            print("❌ خطا در ارسال پیام")
    except Exception as e:
        print(f"❌ خطا: {e}")

def get_bot_info():
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getMe"
    response = requests.get(url)
    if response.status_code == 200:
        bot_info = response.json()
        print(f"🤖 نام ربات: {bot_info['result']['first_name']}")
        print(f"🔗 یوزرنیم: @{bot_info['result']['username']}")
        return True
    else:
        print("❌ خطا در اتصال به ربات")
        return False

print("🚀 در حال راه‌اندازی ربات فروشگاه...")
print("=" * 50)

if get_bot_info():
    send_welcome()
    print("=" * 50)
    print("✅ ربات با موفقیت فعال شد!")
    print("📱 از این لحظه تمام اطلاعات به این چت ارسال می‌شود")
    print("⏳ در حال مانیتورینگ...")
    
    # حلقه اصلی برای نگه داشتن ربات فعال
    while True:
        try:
            time.sleep(300)  # چک هر 5 دقیقه
            print(f"💚 سیستم فعال - آخرین چک: {datetime.now().strftime('%H:%M:%S')}")
        except KeyboardInterrupt:
            print("\n\n❌ ربات متوقف شد")
            break
else:
    print("❌ لطفاً توکن و آیدی را بررسی کنید")