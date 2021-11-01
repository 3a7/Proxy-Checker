'''
1/11/2021

* This is a simple program made by https://www.instagram.com/a7.acc to check proxies with it's three 
different types.

* There is an explanation for pretty much every line i write.

* This program is for educational purposes only. Do not try to use what you learned on unethical programs/activities


* This program is completely free 0$ cost. If you bought this program from someone please report the owner on instagram
https://www.instagram.com/a7.acc


Enjoy!

'''

# Importing all the necessary libraries       All the libraries are pre installed but requests, threading and colorama.
# To install the libraries write in the cmd:
# 
# pip install <the library> 
import requests,threading,colorama
from random import choice
from time import sleep
from colorama import Fore
from os import system
colorama.init()


# COLORS
g = lambda x : Fore.GREEN+x+Fore.WHITE
rod = lambda x : Fore.RED+x+Fore.WHITE
b = lambda x : Fore.BLUE+x+Fore.WHITE
y = lambda x : Fore.YELLOW+x+Fore.WHITE
c = lambda x : Fore.CYAN+x+Fore.WHITE
m = lambda x : Fore.MAGENTA+x+Fore.WHITE
#  Example >>> g('Hi') will give green colored Hi


# STYLES
ques = f"[{m('?')}] "   # Question
exla = f"[{rod('!')}] " # Bad 
erro = f"[{y('!')}] "   # Error
succe= f"[{g('#')}] "   # Success
inff = f"[{c('*')}] "   # Information
# for ex print(ques+'How are you?')  will give : 
#
# [magenta colored exclamation mark] How are you?

# TO CLEAR THE CMD
clear = lambda: system("cls")




#      Clearing the cmd
clear()

# Here we are writing in the cmd title 
system('title Welcome To Proxy Checker v2 !!            MADE BY @a7.acc')


#                 The title down here from this website >> http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
print(y('''
  _____                        _____ _               _                    ___  
 |  __ \                      / ____| |             | |                  |__ \ 
 | |__) | __ _____  ___   _  | |    | |__   ___  ___| | _____ _ __  __   __ ) |
 |  ___/ '__/ _ \ \/ / | | | | |    | '_ \ / _ \/ __| |/ / _ \ '__| \ \ / // / 
 | |   | | | (_) >  <| |_| | | |____| | | |  __/ (__|   <  __/ |     \ V // /_ 
 |_|   |_|  \___/_/\_\\\\__, |  \_____|_| |_|\___|\___|_|\_\___|_|      \_/|____|
                       __/ |                                                   
                      |___/                                                    '''))
print('                                                                   CopyRight: '+m("https://www.instagram.com/a7.acc"))


print('<'+rod("!")+'> This program is completely free and '+y("NOT")+' for sell!\n\n')



#
#                    Stage 1            Proxy File
#



proxy_file = input(ques+'Enter the proxies file name >> ')

try:
    #          This command will add .txt to the file name if it does not exist to avoid having an error
    if not proxy_file.endswith('.txt'):
        proxy_file = proxy_file+'.txt'

    #         Here we are openning the file and reading it and spliting every line as a string in a list
    #         proxies varuable equal to ['35245:535','2464642:25624'...] and so on
    proxies = open(proxy_file,'r',encoding='utf-8').read().splitlines()


    #    If an error happens, this line will execute and err is the error message:
except Exception as err:
    print(erro+'Error while openning the proxies file! >> '+y(err))
    sleep(5)




#
#                    Stage 2             Emptying The Good Proxies File AND Getting The Threads Count AND Getting The Proxies Type
#



thr = int(input(ques+'How many threads do you want?: '))

open('Good.txt','w',encoding='utf-8').close()

typo = input(f"Enter the proxies type:\n[{c('1')}] HTTP/S\n[{c('2')}] SOCKS4\n[{c('3')}] SOCKS5\n >> ")

if typo == '1':
    #       For HTTP/S proxies
    def prox_function(prox):
        prox_dict = {
        'http':f'https://{prox}',
        'https':f'http://{prox}'
    }
        return prox_dict

elif typo == '2':
    #       For socks4 proxies
    def prox_function(prox):
        prox_dict = {
        'http':f'socks4://{prox}',
        'https':f'socks4://{prox}'
    }
        return prox_dict

elif typo == '3':
    #       For socks5 proxies
    def prox_function(prox):
        prox_dict = {
        'http':f'socks5://{prox}',
        'https':f'socks5://{prox}'
        }
        return prox_dict

else:
    #        Uknown type. other than 1,2 or 3 input
    print(erro+'Uknown proxy type! '+y(typo))
    sleep(5)




#
#                    Stage 3             Making A Checking Function
#


# First we gonna put variables to keep track of good, bad, checked and the unchecked proxies we gonna put them in ally variable
good, bad, checked, ally = 0,0,0,str(len(proxies))



# We are sending an http request to google.com cuz it is the simplest URL to check your proxies in
url = 'https://www.google.com'


def checkproxies():
    #  It is important to global the proxies list here to keep track of every proxy getting deleted globaly in all the threads
    global proxies , bad , good , checked


    while len(proxies) > 0:

        # Choosing a random proxy to check and removing it from the list
        proxy = choice(proxies)
        proxies.remove(proxy)

        proxy_d = prox_function(proxy)


        #    Here if requesty executed it means the proxy is good and no errors happend so we gonna take it and add it to the file
        try:
            requesty = requests.get(url,proxies=proxy_d,timeout=10)
            #        Good Proxy !
            if requesty.status_code == 200:
                print(succe+g(proxy))
                good += 1
                checked += 1
                with open('Good.txt','a',encoding='utf-8') as goodies:
                    goodies.write(proxy+'\n')
            else:
            #        Bad Proxy         NO 200 response from the server
                print(exla+rod(proxy))
                bad += 1
                checked += 1

            #  Here we are typing the information on the cmd's title on the top
            system(f'title   CHECKED:{str(checked)}/{ally}    GOOD:{str(good)}    BAD:{str(bad)}    THREADS:{str(threading.active_count()-1)}')
    
        except:
            #        Bad Proxy         NO response from the server
            print(exla+rod(proxy))
            bad += 1
            checked += 1
            system(f'title   CHECKED:{str(checked)}/{ally}    GOOD:{str(good)}    BAD:{str(bad)}    THREADS:{str(threading.active_count()-1)}')




#
#                     Stage 4               Threads
#



#         Making the threads begin
def start():
    #       thr equal to the number of the threads the user specified 
    for _ in range(thr):
        thread1 = threading.Thread(target=checkproxies)
        thread1.start()

start()