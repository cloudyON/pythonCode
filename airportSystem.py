class passenger():
    def __init__(self):
        self.money = 0
        self.schedule = 0
        self.reserv = []
        self.name

    def reservation(self, air:'nameofAirline',date,airline:'clsAl', airport_system:'clsAs'):
        slash = 0
        if '/' in date:
            slash = date.index('/')
            if air in airline.airlines and 12 >= int(date[0:(slash-1)]) >= 1 and 31 >= int(date[(slash+1):(len(date)-1)]) >= 1:
                airport_system.airSchedule[self.name] = [air, date]
                print(f"{date} 날짜에 {air}항공사에 등록되었습니다.")

            else:
                print("날짜나 항공사가 잘못 입력되셨습니다.")

        else:
            print("날짜를 잘못입력하셨습니다.")




class airport_system():
    def __init__(self):
        self.airSchedule = {}




class airline():
    def __init__(self):
        self.airlines = ['sun air', 'korea air', 'mountain air', 'cloud air', '1st\'s air', 'foru air']
        self.al_Schedule = {'sun air': ['1/12', '1/14', '1/19', '1/21', '2/1', '2/15'],
                            'korea air': ['1/30', '2/14', '2/15', '2/16'],
                            'moutain air': ['1/30', '2/21','3/21'],  # mountain air 는 아주 고급이라 조금밖에 운행 안합니다.
                            'cloud air': ['1/12', '1/15', '1/16', '1/21', '2/9', '2/10', '3/1', '3/12'],
                            '1st\'s air': ['1/21', '1/23', '2/1', '2/3', '2/5', '2/7', '2/9'],
                            'foru air': ['1/22', '1/23', '2/5', '2/7', '2/9', '2/14', '2/21']}

    def del_airline(self, dele):
        try :
            del self.airlines[self.airlines.index(dele)]
            del self.al_Schedule[dele]
        except ValueError:
            print(f"That airline : \'{dele}\' does not exist.")

    def create_airlines(self, name : ''):
        if name not in self.airlines:
            self.airlines.append(name)
            self.al_Schedule[name] = []
            print("항공사가 추가되었습니다.")

        else :
            print("이미 다른 항공사가 있습니다.")

    def create_schedule(self, airline : 'integer',schedule : 'string'):
        if airline in self.airlines :
            self.al_Schedule[airline].appned(schedule)

        else :
            print(f"{airline} 항공사는 존재하지 않습니다.")








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