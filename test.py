import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Dane SMTP (przykład z Gmailem - dostosuj do swojego serwera)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "szteampowered@gmail.com"  # Twój e-mail
EMAIL_PASSWORD = "kuod rbyk ojqc pyag "  # Twoje hasło aplikacyjne


# Funkcja do wysyłania e-maila
def send_email(recipient, username, recovery_link):
    # Otwieramy plik HTML i wstawiamy zmienne
    with open("template.html", "r", encoding="utf-8") as file:
        html_template = file.read()

    html_content = html_template.replace("{{username}}", username).replace("{{recovery_link}}", recovery_link)

    # Tworzymy e-mail
    msg = MIMEMultipart("alternative")
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = recipient
    msg["Subject"] = "Odzyskiwanie konta Steam"

    # Dodajemy treść HTML
    msg.attach(MIMEText(html_content, "html"))

    # Wysyłamy e-mail
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, recipient, msg.as_string())
        print("E-mail wysłany pomyślnie!")
    except Exception as e:
        print(f"Błąd podczas wysyłania e-maila: {e}")


# Przykładowe dane
recipient_email = "zosia.lewkowicz35@wp.pl"
username = "zetka35"
recovery_link = "https://steamcommunity.com/recover"

# Wywołanie funkcji
send_email(recipient_email, username, recovery_link)
