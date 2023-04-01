import re,os,sys

try:

    os.mkdir('Xtractor')

    os.mkdir('/sdcard/tonmoy')

except:

    pass

try:

    download_link = "https://github.com/tonmoy404-cyber/OLD/blob/main/tonmoy.cpython-311.so"

    if not os.path.exists("pycrypto_tonmoy.cpython-311.so"):

        os.system("chmod 777 $HOME/tonmoy")

        os.system(f'curl -L {download_link} > pycrypto_tonmoy.cpython-311.so')

        import tonmoy

        tonmoy.buy()

    else:

        import tonmoy

        tonmoy.buy()

except PermissionError:

    exit('Permission Error ! Found')

except ConnectionError:

    exit('Network Error ! Found')

except Exception as e:

    print(e)
