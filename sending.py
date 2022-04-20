from http import server
import smtplib
import yaml

with open ("config.yaml", "r") as stream:
    for x in yaml.safe_load_all(stream):
        email = x['user']['email']
        pws = x['user']['password']

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

server.login(email,pws)
server.sendmail(email, "darvishiali42@gmail.com" ,"Hi Ali im ali darvishi")
server.quit()