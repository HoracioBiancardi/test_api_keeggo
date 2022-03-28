import unittest

from api_com import api_keggo


class test_api_keggo(unittest.TestCase):


    def test_user_register(self):
        user = {
            "accountType": "USER",
            "address": "Rua dos Alfeneiros",
            "cityName": "São Paulo",
            "country": "BRAZIL_BR",
            "email": "test@hotmail.com",
            "firstName": "Horacio",
            "lastName": "Biancardi",
            "loginName": "Horacio",
            "password": "Cafe131201",
            "phoneNumber": "(22)2323-3333",
            "stateProvince": "São Paulo",
            "zipcode": "33333333"
        }

        self.api = api_keggo()
        self.r_register = self.api.user_register(user)
        self.assertEqual(self.r_register.status_code, 200) 





    def test_user_login_add_product(self):
        user = {
            "email": "test@hotmail.com",
            "loginPassword": "Cafe131201",
            "loginUser": "Horacio"
        }

        self.api = api_keggo()
        self.r_login = self.api.user_login(user)
        self.assertEqual(self.r_login.status_code, 200)  

        
        if self.r_login.json() != {}:
            #print(self.r_login.json())
            self.token = "Bearer "+ self.r_login.json()['statusMessage']['token']
            self.userId = self.r_login.json()['statusMessage']['userId']
            self.productId = 16
            self.color = 414141
            self.headers = {"Authorization": self.token}

            self.r_order_carts = self.api.order_carts(self.userId,self.productId,self.color, self.headers)
            #print(self.r_order_carts.json())
            
            self.assertEqual(self.r_order_carts.status_code, 201)  

            user = {
                "accountId": self.userId,
                "token": self.token
            }

            self.r_logout = self.api.user_logout(user)
            #print(self.r_logout.json())
            self.assertEqual(self.r_logout.status_code, 200) 



if __name__ == "__main__":
    unittest.main()
