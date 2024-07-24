import tkinter as tk
from tkinter import messagebox
import webbrowser

# Lista de dorks mÃ¡s populares, incluyendo extensiones de documentos
dorks = [
    'intitle:"Index of" inurl:admin',
    'inurl:wp-content inurl:uploads',
    'inurl:phpinfo.php',
    'filetype:sql "inurl:wp-content"',
    'filetype:sql inurl:backup',
    'inurl:admin intitle:login',
    'intitle:"Index of" inurl:wp-json/oembed',
    'intitle:"Index of" phpmyadmin',
    'intitle:"Index of" wp-admin',
    'intitle:index.of.?.sql',
    'inurl:/filemanager/dialog.php',
    's3 site:amazonaws.com filetype:log',
    'inurl:cgi/login.pl',
    'inurl:zoom.us/j and intext:scheduled for',
    'site:*/auth intitle:login',
    'inurl: admin/login.aspx',
    '"Index of" inurl:webalizer',
    '"Index of" inurl:htdocs inurl:xampp',
    's3 site:amazonaws.com intext:dhcp filetype:txt inurl:apollo',
    'inurl:Dashboard.jspa intext:"Atlassian Jira Project Management Software"',
    'inurl:app/kibana intext:Loading Kibana',
    'intitle:"index of" unattend.xml',
    'inurl:office365 AND intitle:"Sign In | Login | Portal"',
    'intext:"@gmail.com" AND intext:"@yahoo.com" filetype:sql',
    'intitle:"qBittorrent Web UI" inurl:8080',
    'intitle:"Swagger UI - " + "Show/Hide"',
    'ext:conf', 'ext:doc', 'ext:docx', 'ext:xls', 'ext:xlsx', 'ext:xml', 'ext:yml', 'ext:env', 'ext:txt', 'ext:ans', 'ext:zip', 'ext:zipx', 'ext:7z', 'ext:tar', 'ext:gz', 'ext:tgz', 'ext:rar', 'ext:database', 'ext:db', 'ext:exe', 'ext:jar', 'ext:java', 'ext:js', 'ext:jsp', 'ext:rtf', 'ext:sh',
    'ext:sys', 'ext:vb', 'ext:inc', 'ext:bak', 'ext:old', 'ext:bat', 'ext:py', 'ext:json', 'ext:properties', 'ext:pem', 'ext:yaml', 'ext:ts', 'ext:c', 'ext:asa', 'ext:config', 'ext:rtf', 'ext:pptx', 'ext:bkf', 'ext:bkp', 'ext:backup', 'ext:sql', 'ext:log',
    'ext:php', 'ext:php5', 'ext:aspx', 'ext:asp',
    'intitle:index.of â€œparent directory"',
    'intitle:"index of"',
    'intitle:index.of name size',
    'intitle:index.of.admin or intitle:index.of inurl:admin',
    'intitle:index.of index.php.bak or inurl:index.php.bak',
    'inurl:admin',
    'site:amazonaws.com',
    'intitle:"Index of/"',
    'inurl:*.doc', 'inurl:*.xls', 'inurl:*.sql',
    'ext:log', 'ext:conf', 'ext:cnf', 'ext:ini', 'ext:env', 'ext:sh', 'ext:bak', 'ext:backup', 'ext:swp', 'ext:old', 'ext:git', 'ext:svn', 'ext:htpasswd', 'ext:htaccess', 'ext:json',
    'filetype:pdf',
    'filetype:doc',
    'filetype:docx',
    'filetype:xls',
    'filetype:xlsx',
    'filetype:ppt',
    'filetype:pptx',
    'filetype:txt',
    'filetype:rtf',
    'filetype:csv',
    'filetype:xml',
    'filetype:json',
    'filetype:yaml',
    'filetype:log'
]

# FunciÃ³n para buscar dorks en un dominio y abrir en Google
def buscar_dorks():
    dominio = entry.get()
    if not dominio:
        messagebox.showwarning("Advertencia", "Por favor, ingresa un dominio.")
        return

    for dork in dorks:
        query = f"inurl:{dominio} {dork}"
        webbrowser.open(f"https://www.google.com/search?q={query}")

# ConfiguraciÃ³n de la interfaz grÃ¡fica
root = tk.Tk()
root.title("BÃºsqueda de Dorks")

label = tk.Label(root, text="Ingresa el dominio:")
label.pack(pady=5)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

button = tk.Button(root, text="Buscar Dorks", command=buscar_dorks)
button.pack(pady=10)

resultados = tk.Text(root, width=80, height=20)
resultados.pack(pady=5)

root.mainloop()

# Firma del creador
print("\nScript creado por Arturo Correa 'P4nth4 R31'")
