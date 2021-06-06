
class DbConnector:
    """ Manages connection for SQL databse """

    def __init__(self):
        
    async def initialize(self, config: AppConfig):
        """ Init Database """
        try:
            conn = psycopg2.connect(
                user=config.db.user,
                password=config.db.password,
                host=config.db.host,
                port=config.db.port,
                name=config.db.name
            )
        except asyncpg.ConnectionFailureError as exc:
            log.error("Database Error %s", exc)