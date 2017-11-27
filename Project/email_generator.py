import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text      import MIMEText
from email.mime.image     import MIMEImage

def sendemail(recommendation, recommendation_details, from_addr, to_addr, subject, message,
              login, password, smtpserver='smtp.gmail.com:587'):

    message = '<img src="cid:image1"><br>' \
              '<b>We recommend the following based on your ' \
              '<i>location, driving style, hours, age, parking, ' \
              'and usage</i>:</b><br>'
    if (recommendation['Keyloss']):
        message += " Keyloss "
    if (recommendation['Paint']):
        message += " Paint "
    if (recommendation['Tires']):
        message += " Tires "
    if (recommendation['Windshield']):
        message += " Windshield "
    message += '<br><br><b>With the following recommendation details:</b><br>'
    message += recommendation_details

    msgRoot = MIMEMultipart('related')
    msgRoot["Subject"] = "BMWCare Recommendations"
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    msgText = MIMEText(message, 'html')
    msgAlternative.attach(msgText)

    fp = open('images/CT_logo1.png', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)

    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    server.sendmail(from_addr, to_addr, msgRoot.as_string())
    server.quit()