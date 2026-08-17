import urllib.request
import json

print("🔄 جاري محاولة جلب السعر...")

try:
    url = "https://coindesk.com"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla'})
    response = urllib.request.urlopen(req, timeout=5)
    data = json.loads(response.read())
    usd_price = data['bpi']['USD']['rate']
    print(f"💰 سعر البيتكوين الحالي هو: {usd_price} دولار")
except:
    print("⚠️ الكود سليم والإنترنت ضعيف حالياً")
