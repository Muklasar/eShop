from django import template

register = template.Library()

@register.filter(name="currency")
def currency(number):
    return "₹" + str(number)

@register.filter(name="total")
def total(n1,n2):
    return n1 * n2