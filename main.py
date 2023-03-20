import requests
from bs4 import BeautifulSoup
from smtplib import SMTP

# look up link
URL = "https://www.amazon.de/Hill-HeroQuest-Basisspiel-Brettspiel-Fantasie-Abenteuerspiel/dp/B09LHXS23S/ref=sr_1_3?keywords=" \
      "hero%2Bquest%2Bgrundspiel&qid=1679342446&sprefix=hero%2Bquest%2Bgrun%2Caps%2C101&sr=8-3&th=1"

#request header
header = {
  "Accept-Language": "en-US,en;q=0.5",
  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0",
}

#mail statics

smtp_name = "outlook.office365.com"
sender = ""
recipient = ""
port = int("")
user = ""
pwd = ""

#request
response = requests.get(URL,headers=header)

#mix the soup
soup = BeautifulSoup(response.text, "html.parser")
price_with_dot = soup.find(name="span", class_="a-offscreen").getText().replace(",",".")
price = float(price_with_dot.replace("€",""))
print(price)

# price check
if price <= 85.00:
  with SMTP(smtp_name,port=port) as sendmail:
    sendmail.starttls()
    sendmail.login(user=user,password=pwd)
    sendmail.sendmail(from_addr=sender, to_addrs=recipient, msg=f"Subject:Price Alert for Hero Quest\n\n"
                                                                f"Der Preis für Hero Quest (Hauptspiel) liegt aktuell bei {str(price)}€, jetzt zuschlagen.")