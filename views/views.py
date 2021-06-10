from models import models as md
from datetime import datetime


def split_array(self):
    """
    Metodo recibe el arreglo obtenido al leer el archivo
    separa el arreglo en nombre de empleado y horario
    """
    data = []
    for item in range(len(self)):
        data.append(self[item].split('='))
    return data


def read_file(self):
    """
    Metodo recibe como parametro el nombre (file.txt) del archivo
    lee el archivo recibido y lo separa en arreglos por salto de linea \n
    retorna un arreglo separando el nombre de empleado y horario
    """
    try:
        f = open(self, 'r')
        line = f.read()
        data = line.split('\n')
        f.close()
        return split_array(data)
    except FileNotFoundError:
        msg = 'File not found'
        return msg


def convert_time(self):
    """
    Metodo recibe una cadena de texto
    convierte la cadena en horas en el formato 00:00:00
    retorna un objeto de tipo time
    """
    return datetime.strptime(self, '%H:%M').time()


def split_hours(self):
    """
    Metodo recibe el arreglo separado del nombre de empleado y horarios laborado
    retorna un arreglo con el nombre del empleado y sus horarios separados en un arreglo
    """
    count = 0
    for elem in self:
        self[count][1] = elem[1].split(',')
        count += 1
    return self


def pay_employee(self):
    """
    Metodo recibe el arreglo con el nombre del empleado y horarios separados
    calcular el total a pagar a un empleado en funcion a dias laborados y horas
    """
    cad = 'The amount to pay '
    pay = 0
    for item in self:
        cad += item[0] + ' is: '
        for elem in item[1]:
            day = elem[0:2]
            pay += int(payment_schedules(day, elem[2:]))
        cad += str(pay)
        pay = 0
        print(cad)
        cad = 'The amount to pay '


def payment_schedules(day, hours):
    """
    Metodo recibe como parametro dia de la semana y las horas laboradas por dia
    Calcula el valor de las horas trabajas en base al rango al que pertenecen
    """
    x = 0
    h_init = convert_time(hours[0:5])
    h_end = convert_time(hours[6:])
    if day in md.weekdays:
        if h_init >= convert_time('00:01') and h_end <= convert_time('09:00'):
            x += int(25)
        elif h_init >= convert_time('09:01') and h_end <= convert_time('18:00'):
            x += int(15)
        elif h_init >= convert_time('18:01') and h_end >= convert_time('00:00'):
            x += int(20)
    elif day in md.week_end:
        if h_init >= convert_time('00:01') and h_end <= convert_time('09:00'):
            x += int(30)
        elif h_init >= convert_time('09:01') and h_end <= convert_time('18:00'):
            x += int(20)
        elif h_init >= convert_time('18:01') and h_end >= convert_time('00:00'):
            x += int(25)
    return x



