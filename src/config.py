class Development(object):
    """
    Development environment configuration
    """

    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Summer2019@localhost:3307' \
                              '/ideas-collector '


class Production(object):
    """
    Production environment configuration
    """

    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://admin:Summer2019@ideas-collector.' \
                              'csiaqjz2well.us-east-2.rds.amazonaws.com:3306' \
                              '/ideas-collector '


app_config = {
    'development': Development,
    'production': Production
}
