#Fernando Javier Marin Salas
#Matricula: 1679139
#Importacion de modulos necesarios para enviar el correo atraves de SMTP y adjuntar una imagen.
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


# Configura los detalles del correo electrónico
#En esta seccion se definen detalles del correo electronico que enviaremos.
from_email = 'fershomarin@gmail.com'
password = ''
to_email = 'gerardo.bernal@uanl.edu.mx'
subject = 'Prueba de envio (script Python) - 1679139'
alumno = 'Fernando Javier Marin Salas'
matricula = '1679139'

#El cuerpo del mensaje en formato HTML
html = f"""\
<html>
  <body>
    <p>Practica 12</p>
    <p>Ejercicio de la practica 12 para envío de correos</p>
    <p>Alumno: {'Fernando Javier Marin Salas'}</p>
    <p>Matricula: {1679139}</p>
  </body>
</html>
"""

# Cargar la imagen que deseas adjuntar
with open('FCFM_COOL.png', 'rb') as f:
    img_data = f.read()

# Crea el mensaje y adjunta la imagen
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(html, 'html'))
img = MIMEImage(img_data, name='FCFM_COOL.png')
msg.attach(img)

# Envía el mensaje a través de SMTP
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()
    print('Correo enviado exitosamente.')
except Exception as e:
    print('Error al enviar el correo:', str(e))
