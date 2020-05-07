import ldap


class Auth(object):
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.server_address = 'ldap://192.168.10.6:389'
        self.auth = ldap.initialize(uri=self.server_address)
        self.auth.protocol_version = ldap.VERSION3
        self.auth.set_option(ldap.OPT_REFERRALS, 0)
    def check_authorize(self):
        try:
            self.check_user = self.auth.bind_s(f'{self.login}@agrohold.ru', self.password)
        except ldap.INVALID_CREDENTIALS:
            return 'Incorrect username or password!'
        except ldap.SERVER_DOWN:
            return ('Server URL is not validate')
        else: return 'Authorized'
    def getIsaGropup(self):
        self.search = Auth(self.login, self.password).check_authorize()
        if self.search == 'Authorized':
            self.auth.bind_s(f'{self.login}@agrohold.ru', self.password)
            self.search = self.auth.search_s('dc=agrohold,dc=ru', ldap.SCOPE_SUBTREE, f'mail={self.login}@agrohold.ru')
            self.isalist = []
            for se in self.search[0][1]['memberOf']:
                gr = se.decode('utf-8').split(',',1)[0][3:]
                if gr[:3 ] == 'ISA':
                    self.isalist.append(gr)
            return self.isalist
        else:print('Unauthorized')

au = Auth('am.fesenko', 'vInc093290193')
print(au.getIsaGropup())

