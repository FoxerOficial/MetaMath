from django import template

register = template.Library()

@register.filter
def estado_es(value):
    text = str(value)
    text = text.replace('Submitted', 'Entregado')
    text = text.replace('minutes', 'minutos').replace('minute', 'minuto')
    text = text.replace('seconds', 'segundos').replace('second', 'segundo')
    text = text.replace('hours', 'horas').replace('hour', 'hora')
    text = text.replace('days', 'días').replace('day', 'día')
    return text