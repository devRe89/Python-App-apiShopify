import os
from dotenv import load_dotenv
load_dotenv()

class Parametros:

    def get_p(self):
        a = os.getenv('DOMAIN_HBWZURICH')
        print(a)

