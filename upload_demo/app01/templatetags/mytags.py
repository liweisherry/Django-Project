from django import template
register = template.Library()


@register.inclusion_tag('dropdown.html')
def sql_list(num):
    return {'num': [(i, '{}的平方是{}'.format(i, i**2)) for i in range(1, num+1)]}