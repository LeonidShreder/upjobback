from database import session


def base(func):

    def wrap(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            session.rollback()
            return None

    return wrap


@base
def create(func):

    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        session.add(result)
        session.commit()
        return result

    return wrap


@base
def delete(func):

    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        session.delete(result.Company)
        session.commit()
        return result

    return wrap


@base
def get(func):

    def wrap(*args, **kwargs):
        return func(*args, **kwargs)

    return wrap


@base
def update(func):

    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        session.execute(result)
        session.commit()

    return wrap
