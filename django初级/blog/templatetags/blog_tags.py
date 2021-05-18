from django import template
from ..models import WordsOfQiu
import datetime

register = template.Library()

@register.simple_tag
def get_word_qiu():
    date_start = datetime.date(2018, 11, 2)
    now = datetime.datetime.now()
    date_now = datetime.date(now.year, now.month, now.day)
    diference_day= date_now - date_start
    id = diference_day.days
    try:
        word = WordsOfQiu.objects.all()[id]
        return word
    except:
        return None
