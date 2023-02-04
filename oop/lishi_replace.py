class User(object):
    def print_name(self):
        pass

class VipUser(User):
    def print_name(self):
        """
        保证参数和返回值类型需要和父类一样
        :return:
        """
        pass
def print_name(u):
    """
    不论使用User还是继承User的VipUser，调用的方式是一样的。这就要求User和VipUser的方法参数和返回值类型是一样的
    :param u:
    :return:
    """
    u.print_name()