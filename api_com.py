from httpx import delete, get, post


class api_keggo():
    def __init__(self):
        self.url_base_accounts='http://advantageonlineshopping.com/accountservice/accountrest/api/v1/'
        self.url_base_order='http://advantageonlineshopping.com/order/api/v1/'


    def user_register(self, user):
        self.url_register = self.url_base_accounts + 'register'

        r = post(self.url_register, json = user)
        return r


    def user_login(self, user):
        self.url_login = self.url_base_accounts + 'login'

        r = post(self.url_login, json = user)
        return r


    def user_logout(self, user):
        self.url_logout = self.url_base_accounts + 'logout'
        r = post(self.url_logout, json = user)
        return r

    def user_delete(self, user):
        self.url_delete = self.url_base_accounts + 'delete'
        r = delete(self.url_delete, json=user)
        return r



    def order_carts(self, userId,productId,color,Headers):

        self.url_carts = self.url_base_order + f'carts/{userId}/product/{productId}/color/{color}'
        r = post(self.url_carts, headers=Headers)
        return r



