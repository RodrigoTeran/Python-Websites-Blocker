# Sistemas
Windows = r"C:\\Windows\System32\drivers\etc\hosts"
Unix = "/etc/hosts"
Sistema_operativo = input("Sistema operativo (Windows, Unix): ")
if Sistema_operativo == "Windows":
    Sistema_operativo = Windows

elif Sistema_operativo == "Unix":
    Sistema_operativo = Unix
hosts_dir = Sistema_operativo
redirect = "127.0.0.1"
websites_list = [
    "www.facebook.com",
    "facebook.com",
    "www.google.com",
    "google.com",
    "translate.google.com.mx",
    "www.translate.google.com.mx",
    "www.translate.google.com",
    "translate.google.com",
    "web.whatsapp.com",
    "web.whatsapp",
    "drive.google.com",
    "mail.google.com",
    "https://www.youtube.com/?gl=MX&hl=es-419"
]
determinante = input("Habilitar o Deshabilitar páginas Web: ")
if determinante == "Habilitar":
    determinante = False
    print("Habilitando páginas web...")
elif determinante == "Deshabilitar":
    determinante = True
    print("Deshabilitando páginas web...")
while True:
    if determinante:
        with open(hosts_dir, 'r+') as file:
            content = file.read()
            for website in websites_list:
                if website in content:
                    pass
                else:
                    file.write("\n" + redirect + " " + website + "\n")
    elif not determinante:
        with open(hosts_dir, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites_list):
                    file.write(line)
            file.truncate()
