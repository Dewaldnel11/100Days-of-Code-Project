import smtplib
import datetime as dt

my_email = "allaboardprojects@gmail.com"
password = "Dncgrams123" #remember to go and generate the app password if you actually want to use this script.

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email , password=password)
    connection.sendmail(from_addr=my_email, 
                        to_addrs="dewaldnel.nel@gmail.com", 
                        msg="Subject:Hello\n\n{quote}"
                        )
    




