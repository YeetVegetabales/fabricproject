import time
import itertools
import threading
import sys
import colorama
from colorama import Fore, Style

cotton_values = {50: 4.2, 60: 4.9, 90: 6.9, 100: 7.6}
c_pcnt = 0

def calculate(cotton_percentage: int = 100):
    polyester_percentage = 100 - int(cotton_percentage)
    print(Fore.CYAN + "\nCotton Percentage: ", Fore.RED + str(cotton_percentage))
    print(Fore.CYAN + "Polyester Percentage: ", Fore.RED + str(polyester_percentage), "\n")
try:
    c_pcnt = int(input(Fore.CYAN + "What percentage of cotton is in your shirt?\n"))
except ValueError:
    print(Fore.RED + "\n\nValues must be integers.")
    quit()

def look():
    if c_pcnt < 0 or c_pcnt > 100:
        print(Fore.RED + "\n\nCotton percentage cannot be more than 100% or less than 0%")
        quit()
    else:
        pass

look()

calculate(c_pcnt)

done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write(Fore.GREEN + Style.DIM + '\rLoading... ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r\n\n')

t = threading.Thread(target=animate)
t.start()
time.sleep(3)
done = True

def final():
    fin = 0
    hundred, ninety, sixty, fifty = cotton_values[100], cotton_values[90], cotton_values[60], cotton_values[50]
    if c_pcnt in cotton_values.keys():
        fin = cotton_values[c_pcnt]
    else:
        if c_pcnt == 0:
            fin = 0
        elif 0 < c_pcnt < 50:
            p = fifty/50
            fin = p * c_pcnt
        elif 50 < c_pcnt < 60:
            partial = (sixty - fifty)/10
            x = c_pcnt - 50
            almost = partial * x
            fin = almost + fifty
        elif 60 < c_pcnt < 90:
            partial2 = (ninety - sixty)/30
            x2 = c_pcnt - 60
            almost2 = partial2 * x2
            fin = almost2 + sixty
        elif 90 < c_pcnt < 100:
            partial3 = (hundred-ninety)/10
            x3 = c_pcnt - 90
            almost3  = partial3 * x3
            fin = almost3 + ninety
    print(Style.RESET_ALL + Fore.CYAN + "\n\nExpected Percent Decrease in Dimensions: {}%".format(Fore.RED + str(round(fin, 2))))

final()

# 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
