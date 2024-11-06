
import re
import requests
import pandas as pd
from bs4 import BeautifulSoup

from web_content.config import canvas_user

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

# Setting up logging
    
def get_netid_login(url_website = 'https://canvas.rutgers.edu/'):
    '''
    Function to take the website and return the login link for netid
    '''

    response = requests.get(url_website, headers)
    # BS object
    soup = BeautifulSoup(response.content, 'html.parser')

    ### Use different method to get the netid login for now and the href 
    ### Get all the hrefs which go to a login page
    pattern = re.compile(r'.*login.*', re.IGNORECASE)
    logins = soup.find_all('a', href=pattern)

    ### Filter netid login
    ### Out of those filter ones which are netid logins
    pattern_netid = re.compile(r'.*netid.*', re.IGNORECASE)
    netid_login = [login for login in logins if pattern_netid.search(login.text)]
    netid_login_url = netid_login[0].get('href')

    return netid_login_url

def send_request(netid_login_url = 'https://rutgers.instructure.com/login/saml/'):
    '''
    Function to return the netid login
    '''

    # Start a session
    with requests.Session() as session:

        login_url = netid_login_url
        login_payload = {
            "username":canvas_user.get("user"),
            "password":canvas_user.get("password")
        }

        # Initial login request
        # Put login request until you get the response as 200
        # while True:
        #     login_response = session.get(login_url)
        #     print(login_response)
        #     if login_response in [200]:
        #         break

        #     login_url = login_response

        login_response = session.get(login_url, allow_redirects=True)
        print("Initial login response:")
        print(login_response.url)
        print(login_response.history)
        print(login_response.content)

        login_response_1 = session.post(login_response.url, allow_redirects=True)
        print("Next login response:")
        print(login_response_1.url)
        print(login_response_1.history)
        print(login_response_1.content)

        with open('check.html', 'w') as f:
            f.write(login_response_1.content.decode('utf-8'))



    pass


if __name__ == '__main__':

    url_website = 'https://canvas.rutgers.edu/'

    # Getting netid login url
    netid_login_url = get_netid_login(url_website)
    print(netid_login_url)


    # 2fa_login
    print('Sending request')
    send_request(netid_login_url)