from itsdangerous import URLSafeTimedSerializer
'''import os
secret_key=os.urandom(20)
serializer=URLSafeTimedSerializer(secret_key)
token=serializer.dumps('ujjwala2123!',salt='confirmation')

print(token)
print(serializer.loads(token,salt='confirmation',max_age=60))
#serializer.loads(token,salt='confirmation',max_age=120)
'''
from key import secret_key
def token(email,salt):
    serializer=URLSafeTimedSerializer(secret_key)
    return serializer.dumps(email,salt=salt)
