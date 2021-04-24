from django import template

register = template.Library()

@register.filter(name="is_in_cart")
def is_in_cart(product, cart):
    try:
        keys = cart.keys()
        for id in keys:
            if int(id) == product.id:
                return True
    except Exception:
        return False
    # if cart != None :
    #     keys = cart.keys()
    #     for id in keys:
    #         if int(id) == product.id:
    #             return True
    # else:          
    #     return False

@register.filter(name="cart_quantity")
def cart_quantity(product, cart):
    if cart != None:
        keys = cart.keys()
        for id in keys:
            if int(id) == product.id:
                return cart.get(id)
    else:           
        return 0

@register.filter(name="total_price")
def total_price(product, cart):
    return product.price * cart_quantity(product, cart)

@register.filter(name="cart_total")
def cart_total(products, cart):
    sum = 0;
    for p in products:
        sum += total_price(p, cart) 
    return sum