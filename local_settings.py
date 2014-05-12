'''
Configuration Settings

Includes keys for Twilio, etc.  Second stanza intended for Heroku deployment.
'''

# Uncommet to configure in file.
ACCOUNT_SID = "ACfded4bbaff2a8d787e1ed9ddace6ffb2" 
AUTH_TOKEN = "a79dcad5f4029d347e8016232e8bd4d9"
BSSSPAM_APP_SID = "APbec82e3b6ffd6f2c1c24dd2de3defae4"
BSS_SPAM_ID = "+15088154347"


# Begin Heroku configuration - configured through environment variables.
import os
ACCOUNT_SID = os.environ['ACCOUNT_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']
BSSSPAM_APP_SID = os.environ['BSSSPAM_APP_SID']
BSS_SPAM_ID = os.environ['BSS_SPAM_ID']
