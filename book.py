class Book:
    def __init__(self, name):
        self.name = name
        self.order = []
        self.compteur = 1

    def insert_buy(self, quantity, price):
        orderbuy = Order(quantity=quantity, price=price,type="BUY",id=self.compteur)
        self.print_call(orderbuy)
        self.execute(orderbuy)
        self.order.append(orderbuy)
        self.print_history()
        self.order.sort(key=lambda x:  x.price, reverse = True)

    def insert_sell(self, quantity, price):
        ordersell = Order(quantity=quantity, price=price, type="SELL",id=self.compteur)
        self.print_call(ordersell)
        self.execute(ordersell)
        self.order.append(ordersell)
        self.print_history()
        self.order.sort(key=lambda x: x.price, reverse= True)


    def execute(self, order):
        self.order.sort(key=lambda x: x.price, reverse= True)
        k = order.quantity
        
        if (order.type == "SELL"):
            
            for hist in self.order:
                if(hist.price >= order.price and order.type != hist.type and order.quantity > 0 and hist.quantity >0):
                    
                    if (k>=hist.quantity):
                        print(f'execute {hist.quantity} at {hist.price} on {self.name}')
                        order.quantity -= hist.quantity
                        hist.quantity = 0
                        Book.execute(self, order)
                    
                    else :       
                        print(f'execute {order.quantity} at {hist.price} on {self.name}')
                        hist.quantity -= order.quantity
                        order.quantity = 0
        else:
            for hist in self.order:
                if(hist.price <= order.price and order.type != hist.type and order.quantity > 0 and hist.quantity >0):
                    
                    if (k>=hist.quantity):
                        print(f'execute{hist.quantity} at {hist.price} on {self.name}')
                        order.quantity -= hist.quantity
                        hist.quantity = 0
                        Book.execute(self, order)
                           
                    else :         
                        print(f'execute {order.quantity} at {hist.price} on {self.name}')
                        hist.quantity -= order.quantity
                        order.quantity = 0
            
        

    def print_history(self):
        self.order.sort(key=lambda x: x.price, reverse= True)
        print('\n')
        for x in self.order:
            if (x.quantity > 0):    
                print(f'{x.type} {x.quantity}@{x.price} id={x.id}')
        print("------------------------")

    def print_call(self,order):
        print('\n')
        print(f'-- Insert {order.type} {order.quantity}@{order.price} id={self.compteur} on {self.name}\n Book on {self.name}\n')
        self.compteur += 1


class Order:
        def __init__(self, quantity, price, type, id):
            self.quantity = quantity
            self.price = price
            self.type = type
            self.id = id

