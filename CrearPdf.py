import pdfkit
import jinja2



def crea_pdf(ruta_template,info,rutacss=''):

    nombre_template = ruta_template.split('/')[-1]
    ruta_template = ruta_template.replace(nombre_template,'')
    
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(ruta_template))
    template = env.get_template(nombre_template)
    html = template.render(info)

    options = {
        'page-size': 'Letter',
        'margin-top': '0.05in',
        'margin-right': '0.05in',
        'margin-bottom': '0.05in',
        'margin-left': '0.05in',
        'encoding': "UTF-8"
    }

    ruta_wkthmltopdf = '/usr/bin/wkhtmltopdf'
    config = pdfkit.configuration(wkhtmltopdf=ruta_wkthmltopdf)
    ruta_salida = '/home/falv/Documentos/MoonCode/CreatePdf/reconocimento.pdf'

    pdfkit.from_string(html,ruta_salida,css=rutacss,options=options,configuration=config)
    


if __name__ == "__main__":
    ruta_template = "/home/falv/Documentos/MoonCode/CreatePdf/template.html"
    crea_pdf(ruta_template,
             {"nombreAlumno": "Felipe Luna", "nombreCurso": "Introducción a Python"},
             "/home/falv/Documentos/MoonCode/CreatePdf/estilos.css")