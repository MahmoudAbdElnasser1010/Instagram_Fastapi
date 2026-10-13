import bcrypt


class Hash():
    @staticmethod
    def bcrypt(password: str):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    @staticmethod
    def verify(hashed_password: str, plain_password: str):
        try:
            return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
        except ValueError:
            # stored value is not a valid bcrypt hash (e.g. a plain-text password)
            return False
