import datetime

from docxtpl import DocxTemplate
from docxtpl import InlineImage
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage


def get_context(company, result_sku_list): # возвращает словарь аргуменов
    return {
        'retailer': company,
        'sku_list': result_sku_list,
    }

def from_template(company, result_sku_list, template, signature):
    ds = datetime.datetime.now()
    template = DocxTemplate(template)
    context = get_context(company, result_sku_list)  # gets the context used to render the document

    img_size = Cm(15)  # sets the size of the image
    acc = InlineImage(template, signature, img_size)

    context['acc'] = acc  # adds the InlineImage object to the context
    context['time_gen_sec'] = (datetime.datetime.now()-ds).microseconds/1000
    # print((datetime.datetime.now()-ds).microseconds)
    template.render(context)

    template.save(company + '_' + str(datetime.datetime.now().date()) + '_report.docx')


def generate_report(company, result_sku_list):
    template = 'report.docx'
    signature = 'acc.png'
    document = from_template(company, result_sku_list, template, signature)


# def toFixed(numObj, digits=0):
#     return f"{numObj:.{digits}f}"

generate_report('Ozon', [0.78, 0.12, 0.05, 0.01, 0.01, 0.0001])