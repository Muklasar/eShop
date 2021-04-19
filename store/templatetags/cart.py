from django import template

register = template.Library()

@register.filter(name="is_in_cart")
def is_in_cart(product, cart):
    if cart != None :
        keys = cart.keys()
        for id in keys:
            if int(id) == product.id:
                return True
    else:          
        return False

@register.filter(name="cart_quantity")
def cart_quantity(product, cart):
    if cart != None:
        keys = cart.keys()
        for id in keys:
            if int(id) == product.id:
                return cart.get(id)
    else:           
        return 0