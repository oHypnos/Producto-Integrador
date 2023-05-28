En este [Script](Enviodecorreos.py)

Se importan los módulos necesarios: smtplib para enviar el correo, y las clases MIMEMultipart, MIMEText y MIMEImage del módulo email.mime para configurar el contenido del correo.

Se definen las variables from_email, password, to_email, subject, alumno y matricula con los detalles del correo electrónico. Aquí, se especifica la dirección de correo del remitente, la contraseña del remitente (que deberá ser proporcionada), la dirección de correo del destinatario, el asunto del correo y los detalles del alumno (nombre y matrícula).

Se crea una variable html que contiene el cuerpo del mensaje en formato HTML. En este caso, se utiliza formato HTML para incluir información sobre la práctica y los detalles del alumno en el mensaje.

Se carga la imagen que se desea adjuntar al correo utilizando la sentencia with open('FCFM_COOL.png', 'rb') as f:. Aquí, se asume que la imagen se encuentra en el mismo directorio que el script.

Se crea un objeto msg de tipo MIMEMultipart que representa el mensaje a enviar. Se establecen los campos del remitente, destinatario y asunto utilizando los valores previamente definidos. Además, se adjunta el cuerpo del mensaje HTML y la imagen cargada en el paso anterior.

Se intenta enviar el mensaje a través del servidor SMTP de Gmail. Se establece una conexión segura con el servidor utilizando server.starttls() y se realiza la autenticación con el remitente utilizando server.login(from_email, password). Luego, se convierte el objeto msg a una cadena de texto utilizando msg.as_string() y se envía el correo utilizando server.sendmail(from_email, to_email, text). Finalmente, se cierra la conexión con el servidor SMTP mediante server.quit().

Si ocurre alguna excepción durante el proceso de envío del correo, se captura y se imprime un mensaje de error.

Es importante tener en cuenta que se debe proporcionar la contraseña del remitente para poder autenticarse en el servidor SMTP y enviar el correo exitosamente.

Recuerda que para ejecutar el script, necesitarás tener instalado el módulo smtplib. Además, asegúrate de tener una conexión a Internet activa y que el servidor SMTP utilizado (en este caso, el de Gmail) permita el envío de correos mediante el protocolo SMTP.
