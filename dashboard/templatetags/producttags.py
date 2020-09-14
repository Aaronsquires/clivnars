from django import template


register = template.Library()

@register.filter
def diff(a, b):
    return abs(a-b)

@register.filter()
def readable_integer(integer):
    readable=str(integer).split(".")[0][::-1]
    readable=[readable[i:i+3] for i in range(0, len(readable), 3)]
    if len(str(integer).split("."))==1:
        end=""
    else:
        end="."+str(integer).split(".")[1]
    return " ".join(readable[::-1])+end
