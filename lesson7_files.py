# -*- coding: utf8 -*-
import datetime
import csv
import json
from docxtpl import DocxTemplate
from docxtpl import InlineImage
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage

def get_context(brand,model,consumption,price):
    return {
        'brand':brand,
        'model':model,
        'consumption':consumption,
        'price':price
    }

def generate_report(brand,model,consumption,price):
    template='car_template.docx'
    template=DocxTemplate(template)
    context=get_context(brand,model,consumption,price)
    template.render(context)
    template.save(brand + '_' + model + '_' + str(datetime.datetime.now().date()) + '_report.docx')



field_names=['brand', 'model', 'consumption', 'price']
with open('cars.txt', "r", encoding="utf-8") as f:
    car_info=csv.DictReader(f, delimiter=',', fieldnames=field_names)
    print(car_info)
    # Если задано несколько машин, то делает 3 отчета для каждой
    for cur_car in car_info:
        print(cur_car)
        print(cur_car['brand'])
        ds = datetime.datetime.now()
        # Формируем файл Word
        generate_report(brand=cur_car['brand'],model=cur_car['model'], consumption=cur_car['consumption'], price=cur_car['price'])
        # Pro - вычисляем и сохраняем время ген. отчета Word в доп. поле словаря
        time_gen_report_mks=(datetime.datetime.now() - ds).microseconds
        cur_car['time_gen_report_mks']=time_gen_report_mks
        field_names = ['brand', 'model', 'consumption', 'price', 'time_gen_report_mks']

        filename=cur_car['brand'] + '_' + cur_car['model'] + '_' + str(datetime.datetime.now().date()) + '_report'
        # Формируем файл CSV
        with open(filename+'.csv', 'w', newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, delimiter=';', fieldnames=field_names)
            writer.writeheader()
            writer.writerow(cur_car)
        # Формируем файл JSON
        with open(filename+'_json.txt', 'w', newline='', encoding="utf-8") as f:
            json.dump(cur_car,f, ensure_ascii=False)






