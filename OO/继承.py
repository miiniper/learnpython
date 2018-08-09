# class Animal:
#     def __init__(self,name,life,agg):
#         self.name = name
#         self.life =life
#         self.agg = agg
#     def eat(self):
#         self.life += 10
#
#
# class Person(Animal):
#     def __init__(self,money,name,life,agg):
#         super().__init__(name,life,agg)
#         self.money = money
#
#     def attack(self,other):
#         other.life -= self.agg
#
#
# class Dog(Animal):
#     def __init__(self,name,breed,life,agg):
#         super().__init__(name,life,agg)
#         self.breed = breed
#
#     def bite(self,person):
#         person.life -= self.agg
#
#     def eat(self):
#         super(Dog, self).eat()
#         print('dog is eating')
#
#
# ren = Person(20000,'ren',100,2)
# dog = Dog('dog','xdog',80,4)
#
# print(ren.life)
# dog.eat()
# print(ren.life)
#
# dog.bite(ren)
# print(ren.life)
#
########################################################################################
#
# class Pay1:
#     def pay(self, money):
#         print('this class Pay1,money is %s' % money)
#
#
# class Pay2:
#     def pay(self, money):
#         print('this class Pay2,money is %s' % money)
#
#
# def payment(obj, money):
#     obj.pay(money)
#
#
# app1 = Pay1()
# app2 = Pay2()
# payment(app1, 200)
# payment(app2, 300)
#
#######################################################################################

# class Payment:
#     def pay(self):
#         raise NotImplementedError
#
#
# class Wechat(Payment):
#     def pay(self, money):
#         print('wechat pay %s ' % money)
#
#
# class QQpay(Payment):
#     def pay(self, money):
#         print('QQ pay %s ' % money)
#
#
# e = Payment()
# e.pay()
# w = Wechat()
# w.pay(20)
#
# q = QQpay()
# q.pay(40)
#
####################################################################################


















