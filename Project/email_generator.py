import smtplib

def sendemail(recommendation, recommendation_details, from_addr, to_addr, subject, message,
              login, password, smtpserver='smtp.gmail.com:587'):

    message = "We recommend the following based on your location, driving style, hours, age, parking, and usage:\n"
    if (recommendation['Keyloss']):
        message += " Keyloss "
    if (recommendation['Paint']):
        message += " Paint "
    if (recommendation['Tires']):
        message += " Tires "
    if (recommendation['Windshield']):
        message += " Windshield "
    message += "\n\n With the following recommendation details:\n"
    message += recommendation_details
    msg = "\r\n".join([
        "From: " + from_addr,
        "To: " + to_addr,
        "Subject: " + subject,
        "",
        message
    ])

    print(recommendation)
    print(recommendation_details)

    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr, msg)
    server.quit()