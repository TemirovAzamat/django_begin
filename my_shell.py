from shop.models import *

items1 = Item.objects.create(name='Компьютер', price=30000)
items2 = Item.objects.create(name='Наушники', price=10000)
items3 = Item.objects.create(name='Мышь', price=3500)
items4 = Item.objects.create(name='Камера', price=5000)
items5 = Item.objects.create(name='Клавиатура', price=5000)

item2 = Item.objects.get(id=2)
purchase2 = Purchase.objects.create(name='Темиров Азамат', age=18, item=item2)

item = Item.objects.get(id=2)
purchase = Purchase.objects.create(item=item, name='Темирлан', age=19)

item4 = Item.objects.get(id=4)
purchase4 = Purchase.objects.create(item=item4, name='Бекзат', age=13)

item1 = Item.objects.get(id=1)
purchase1 = Purchase.objects.create(item=item1, name='Аяна', age=22)

item5 = Item.objects.get(id=5)
purchase5 = Purchase.objects.create(name='Бакыт', age=30, item=item5)
