import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

api_key = "689cf3225ae761e40687e3020574205e"

solver = TwoCaptcha(api_key)

def captcha_solver() -> str:
    try:
        result = solver.recaptcha(
            sitekey='6LfCDysjAAAAAGs8JWTrqGmPEXUtAxuftHnlxchJ',
            url='https://uz-appointment.visametric.com/uz/appointment-form')

    except Exception as e:
        print(e)

    else:
        return result.get("code")