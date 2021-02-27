# 몇가지 self.   를 넣었습니다.

class Consumer():

    def __init__(self, name, age, gender):  # 이름, 나이, 성별 넣기
        self.money = 50000
        self.health = 50
        self.work = {
            'name': '',
            'wage': 0,
        }
        self.name = str(name)
        self.age = age
        self.gender = str(gender)
        self.order = []  # 주문된 메뉴
        self.receive = []  # 배달 완료된 메뉴


    # 직업 설정
    def set_work(self, work_name: 'str', wage: 'int'):  # 하는 일
        self.work['name'] = work_name
        self.work['wage'] = wage
        print("your job just saved : %s " % (self.work))
        return


    # 돈벌기 기본 1시간 할당.
    def working(self):
        if not self.work.get('name'):
            return print('직업이 없습니다.')
        self.money += self.work.get('wage')
        print(f'{self.work["wage"]}만큼 돈을 벌었습니다.')


    def get_profile(self):  # 이 기능은 현재 상태를 알기 위한 만들었습니다.
        print('-------------------------')
        print(f'이름 : {self.name}')
        print(f'체력 : {self.health}')
        print(f'나이 : {self.age}')
        print(f'성별 : {self.gender}')
        print(f'돈 : {self.money}')
        print('-------------------------')


    def set_rename(self, name):  # 이름 개명
        self.name = name
        print("you name just renamed : %s" % (self.name))


    def buy(self, menuName: 'str', clsMenu: 'Menu'):  # 사기
        if menuName in clsMenu.coffee_list:
            self.order.append(menuName)
            price = int(clsMenu.coffee_list[menuName][0])
            self.money -= price
            clsMenu.baristar.money += price
            print(f'상품 {menuName}을 {clsMenu.coffee_list[menuName][0]} 구매하셨습니다.')
            
            clsMenu.baristar.make_coffee(self) # make.coffee를 buy 하면 즉각 적으로 나오게 추가함

        
        else :
            print(f"{menuName} 상품은 존재하지 않습니다.")


    def drink(self, clsMenu):  # 먹기
        for menu in self.receive:
            if self.health < 100:
                self.health += int(clsMenu.coffee_list[menu][1])
        print("you ate all of your food")
        self.order = []
        self.receive = []


    def complain(self, complains, clsMenu):  # 불평
        print("ok. your complain has been deliverd.")
        clsMenu.baristar.feedback.append(complains)


class Baristar():
    def __init__(self, name: 'str'):  # 초기화 , clsMenu는 menu 클래스를 가리킴
        self.name = name
        self.money = 0
        self.feedback = []  # 불평/피드백


    def get_info(self):
        print('------ 바리스타 ------')
        print(self.name, self.money)
        print(self.feedback)
        print('--------------------')


    def tell_menu(self, clsMenu):  # 메뉴 말하기
        print("this coffe shop have this menu :")
        for i in clsMenu.coffee_list:
            print("%s " % i, end='')
        print("\n")


    def add_menu(self, name, price, energy, clsMenu):  # 메뉴 추가하기
        clsMenu.coffee_list[name] = [str(price), int(energy)]
        print("menu been adit")


    def remove_menu(self, name, clsMenu):  # 메뉴 삭제
        del clsMenu.coffe_list[name]
        print("menu been deleted")


    def receive_money(self, clsConsumer, clsMenu):  # 돈 받기
        for menuName in clsConsumer.order:
            self.money += int(clsMenu.coffee_list[menuName][0])


    def make_coffee(self, clsConsumer):  # receive_money 한다음 사용하기
        print("---system---")
        for i in clsConsumer.order:
            print("The %s you ordered came out." % i)
            clsConsumer.receive.append(i)
            del clsConsumer.order[clsConsumer.order.index(i)]
        print("------------\n")
        


class Menu():  # 메뉴
    # Menu라는 객체 생성시 무조건 하위에 기본 메뉴들이 생긴다.
    # Menu의 CRUD를 구현하자.

    def __init__(self):
        self.coffee_list = {
            'americano': ['3500', 30],
            'espresso': ['4200', 15],
            'cappuccino': ['2000', 45],
            'strawberry Latte': ['7500', 25],
            'bread': ['5000', 50]
        }

    def set_baristar(self, baristar: 'Baristar'):
        self.baristar = baristar
        print(f'바리스타 {baristar.name}이 배정되었습니다.')

    # Create
    def add_menu(self, menu: 'dict'):
        self.coffee_list.update(menu)
        print(f'성공적으로 추가가 되었습니다.')

    # Read
    def show_menu(self):
        print(self.coffee_list)

    # Update
    def price_modify(self, name: 'str', price: 'str'):
        self.coffee_list[name][0] = str(price)
        print(f'{name}가격이 {price}로 수정되었습니다.')

    # Delete
    def deleted_menu(self, name: 'str'):
        self.coffee_list.pop(name)
        print(f'{name}을 메뉴에서 지웠습니다.')


if __name__ == "__main__":  # 시작

    # 사는 것은 buy, receive_money,make_coffee, drink 순으로 해주세요.

    # 바리스타
    won_sang = Baristar('won-sang')

    # 메뉴
    print()
    menu = Menu()
    menu.show_menu()
    menu.set_baristar(won_sang)

    # 메뉴 가격 수정
    menu.price_modify('espresso', 2500)
    menu.price_modify('cappuccino', 4500)
    menu.show_menu()

    # 메뉴 삭제
    menu.deleted_menu('bread')
    menu.show_menu()

    # 메뉴 생성
    menu.add_menu({'bread': ['5000', 50]})
    menu.show_menu()

    # Consumer
    print()
    donggyun = Consumer("dong-gyun", 14, "male")

    donggyun.set_work(work_name='개발자', wage=10000)
    donggyun.working()

    donggyun.get_profile()

    donggyun.buy('bread', menu)
    donggyun.get_profile()
    won_sang.get_info()

    # a = Consumer("hihi", 22, "male")
    # menu = Menu()
    # bari = Baristar(menu)

    # a.buy("americano", menu)
    # bari.receive_money(a, menu)
    # bari.make_coffee(a)

    # a.drink(menu)

    # a.enfo()
    # a.complain("the coffee is too strong", bari)
    

    bariA = Baristar('bariA')
    menuV2 = Menu()
    pororo = Consumer('nello', 12, 'male')
    
    menuV2.set_baristar(bariA)
    
    pororo.buy('bread',menuV2)
    pororo.buy('americano',menuV2)

    pororo.complain('the coffee is too strong', menuV2)

    bariA.get_info()