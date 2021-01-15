class Customer:
    """
    Целевой класс объявляет интерфейс, который уже имеет нужный вид.
    """
    def getCountryName(self) -> str:
        return self
    
    def getCompanyName(self) -> str:
        return self
        
class Contact:
    """
    Целевой класс объявляет интерфейс, который уже имеет нужный вид.
    """
    #name = input()
    #phone_num = input()

    def getName(self) -> str:
        return self
    
    def getPhoneNumber(self) -> str:
        return self
        
class IncomeData:
    """
    Адаптируемый класс содержит некоторое полезное поведение, но его интерфейс
    несовместим с существующим кодом. Адаптируемый класс будет приводится к нужному виду
    """
    
    def getCountryCode(self, code) -> str:
        return code
    
    def getCompany(self, company) -> str:
        return company
    
    def getContactFirstName(self, first_name) -> str:
        return first_name
    
    def getContactLastName(self, last_name) -> str:
        return last_name
    
    def getPhoneNumber_1(self, phone_num) -> str:
        return phone_num
    
    def getCountryPhoneCode_1(self, phone_code) -> str:
        return phone_code
        
class Adapter(Customer, Contact, IncomeData):
    """
    Адаптер делает интерфейс Адаптируемого класса совместимым с целевым
    интерфейсом благодаря множественному наследованию.
    """

    def getCompanyName(self) -> str:
        return f"Adapter companyName: {self.getCompany(company)}" #название компании никак не меняется 
    
    def getName(self) -> str:
        return f"Adapter Name: {self.getContactLastName(last_name) + ',' + self.getContactFirstName(first_name)}" # имя и фамилия приводятся к соответствующему виду
    
    def getPhoneNumber(self) -> str:
        num = self.getPhoneNumber_1(phone_num) # получение основной части номера (без кода страны)
        while (len(num) < 10):
            num = '0' + num
        num = '(' + num[0:3] + ')' + num[3:6] + '-' + num[6:8] + '-' + num[8:10]
        num = '+' + str(self.getCountryPhoneCode_1(phone_code)) + num
        return f"Adapter phoneNumber: {num}" # возвращение преобразованного номера телефона
    
    def getCountryName(self) -> str:
        a = {'UA':'Ukraine', 'RU': 'Russia', 'CA': 'Canada'} # словарь для страны и ее сокращения
        b = self.getCountryCode(code)
        for k in a.items(): 
            if (k[0] == b):
                return f"Adapter countryName: {k[1]}" # возвращение названия страны
             
def client_code(cus: "Customer", con: "Contact") -> None:
    """
    Печать преобразованной информации.
    """
    
    print(cus.getCountryName(), end="\n")
    print(cus.getCompanyName(), end="\n")
    print(con.getName(), end="\n")
    print(con.getPhoneNumber(), end="\n")
    
if __name__ == "__main__":
# ввод данных для адаптера
    print('Введите код страны:')
    code = input()
    print('Введите название компании:')
    company = input()
    print('Введите Имя:')
    first_name = input()
    print('Введите Фамилию:')
    last_name = input()
    print('Введите номер телефона:')
    phone_num = input()
    print('Введите код номера:')
    phone_code = int(input())
    
    adaptee = IncomeData()
    print("Это нужно адаптировать: ",end="\n" )
    print(adaptee.getPhoneNumber_1(phone_num))
    print(adaptee.getCountryCode(code))
    print(adaptee.getCompany(company))
    print(adaptee.getContactFirstName(first_name))
    print(adaptee.getContactLastName(last_name))
    print(adaptee.getCountryPhoneCode_1(phone_code))
    
    print("А это уже адаптированное:")
    adapter_1 = Adapter()
    adapter_2 = Adapter()
    client_code(adapter_1, adapter_2)
