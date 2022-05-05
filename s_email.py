# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 14:43:43 2022

@author: bruno.andriolli
"""

#def mail (lista,assunto,msg):
    
def s_email(lista,assunto,msg):
        
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    
    # Configuração
    host = 'smtp.jarezende.com.br'
    port = 587
    user = 'mis@jarezende.com.br'
    password = 'pEi5DfiYHYwXFprh6rWu'
    rem = 'mis@jarezende.com.br'
    lista_email = lista
    subject = assunto
    msgm = msg
    
    # Criando objeto
    print('Criando objeto servidor...')
    server = smtplib.SMTP(host, port)
    
    # Login com servidor
    print('Login...')
    server.ehlo()
    server.starttls()
    server.login(user, password)
    
    # Criando mensagem
    message = msgm
    print('Criando mensagem...')
    email_msg = MIMEMultipart()
    email_msg['From'] = rem
    email_msg['To'] = lista_email
    email_msg['Subject'] = subject
    print('Adicionando texto...')
    email_msg.attach(MIMEText(message, 'plain'))
    
    # Enviando mensagem
    print('Enviando mensagem...')
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())
    print('Mensagem enviada!')
    server.quit()
    
