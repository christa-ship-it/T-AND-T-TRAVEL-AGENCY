import re  
content = open('config.py').read()  
content = content.replace('CORS_ORIGINS = *', 'CORS_ORIGINS = \" "*\')  ; echo open('config.py', 'w').write(content)  ; python fix_config.py ; del fix_config.py
