import re
import urllib.request


def get_10_minute_mail():

    req = urllib.request.Request(
        "https://10minutemail.com/10MinuteMail/index.html",
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
        }
    )

    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        m = re.search(
            'value="([a-zA-Z0-9@.]*)" class="mail-address-address" id="mailAddress"', html)

        return m.group(1)


print(get_10_minute_mail())
