import matplotlib.pylab as plt

coordinates = {}

def final():
    cotton_values = {50: 4.2, 60: 4.9, 90: 6.9, 100: 7.6}
    for i in range(0, 101):
        c_pcnt = i
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
        coordinates[c_pcnt] = fin

final()

listed = coordinates.items()
listed = sorted(listed)
x, y = zip(*listed)

def graph():
    plt.plot(x, y)
    plt.xlabel('Cotton Percentage')
    plt.ylabel('Average Percent Decrease in Dimensions')
    plt.title('Decrease in Dimensions of Cotton Shirts')
    plt.grid()
    plt.show()

graph()
