class passenger():
    def __init__(self):
        self.money = 0
        self.reservation = 0


class airport_system():
    def __init__(self):
        self.airSchedule = []




class airline():
    def __init__(self):
        self.airlines = ['sun air', 'korea air', 'mountain air', 'cloud air', '1st\'s air', 'foru air']
        self.al_Schedule = {'sun air':['1/12','1/14','1/19','1/21','2/1','2/15'],
                            'korea air':['1/30','2/14','2/15','2/16'],
                            'moutain air':['1/30', '2/21','3/21'], # mountain air 는 아주 고급이라 조금밖에 운행 안합니다.
                            'cloud air':['1/12','1/15','1/16','1/21','2/9','2/10','3/1','3/12'],
                            '1st\'s air':['1/21','1/23','2/1','2/3','2/5','2/7','2/9'],
                            'foru air':['1/22','1/23','2/5','2/7','2/9','2/14','2/21']}

    def del_airline(self, delt):
        try :
            del self.airlines[self.airlines.index(delt)]
        except ValueError:
            print(f"That airline : \'{delt}\' does not exist.")






if __name__ == "__main__":
    airline = airline()
    airline.del_airline('sasdfasdf')





# 계획
# class passenger()
#   표 예약
#   체크인
#   체크인할때 자기의 짐


# class airport_system()
#   승객 체크인 도와주기.
#   비행기 입/츨국.

# class(airline)
#   그저 비행사