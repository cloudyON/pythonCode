class Consumer():
    
    def __init__(self,name,age, gender): # 이름, 나이, 성별 넣기
        self.money = 50000
        self.health = 50
        self.work = ""
        self.name = str(name)
        self.age = age
        self.gender = str(gender)   
        self.order = [] # 이 것은 class 끼리 주고 받을려고 추가로 만들었습니다.
        self.receive = [] # 이 것도 class 끼리 주고 받을려고 추가로 만들었습니다.
    

    
    def work(self,a): # 하는 일
        self.work = str(a)
        print("your job just saved : %s " %(self.work))
        return
    
    def rename(self,name): # 이름 개명
        self.name = name
        print("you name just renamed : %s" %(self.name))

    def buy(self, menuName, clsMenu): #사기
        if menuName in clsMenu.coffee_list:
            self.order.append(menuName)
            self.money -= int(clsMenu.coffee_list[menuName][0])
            
    def drink(self,clsMenu): # 먹기
        for menu in self.receive:
            if self.health < 100:
                self.health += int(clsMenu.coffee_list[menu][1])
        print("you ate all of your food")
        self.order = []
        self.receive = []
    
    def enfo(self): # 이 기능은 현재 상태를 알기 위한 만들었습니다.
        print(self.money)
        print(self.health)
        print(self.name)
        print(self.age)
        print(self.gender)
        
    def complain(self,a,clsBari): # 불평
        print("ok. your complain has been deliverd.")
        clsBari.feedback.append(a)
        



    
    

class Baristar():
    def __init__(self,clsMenu): #초기화 , clsMenu는 menu 클래스를 가리킴
        self.money = 0
        self.feedback = []
    
    
    def tell_menu(self, clsMenu): # 메뉴 말하기
        print("this coffe shop have this menu :") 
        for i in clsMenu.coffee_list:
            print("%s " %i,end='')
        print("\n")

    def add_menu(self,name,price,energy,clsMenu): # 메뉴 추가하기
        clsMenu.coffee_list[name] = [str(price),int(energy)]
        print("menu been adit")
    
    def remove_menu(self,name, clsMenu): # 메뉴 삭제
        del clsMenu.coffe_list[name]
        print("menu been deleted")
    
    def receive_money(self,clsConsumer,clsMenu): # 메뉴를 산다음 바로 사용하기
        for menuName in clsConsumer.order:
            self.money += int(clsMenu.coffee_list[menuName][0])
            
            

    def make_coffe(self,clsConsumer, clsMenu):
        for i in clsConsumer.order:
            print("The %s you ordered came out." %i)
            clsConsumer.receive.append(i)
    
            
                
        
class Menu():
    def __init__(self):
        self.coffee_list = {'americano':["3500",30],"espresso":["4200",15],"cappuccino":["2000",45],"strawberry Latte":["7500",25],"bread":["5000",50]}

        

         
    

         
if __name__ == "__main__": # 시작
    
    # 사는 것은 buy, make_coffee, receive_money, drink 순으로 해주세요.
    
    a = Consumer("hihi",22,"male")
    menu = Menu()
    bari = Baristar(menu)

    a.buy("americano",menu)
    bari.make_coffe(a,menu)
    bari.receive_money(a,menu)
    a.drink(menu)

    a.enfo()
    a.complain("the coffee is too strong",bari)

    







