import random

# Introduce here the number of elements you want to generate
n = 10
# Introduce the limits ratio
min = 4/3
max = 16/9
# Introduce the min and max amount of pixels for y axis
y_min = 360
y_max = 2160
x_min = y_min*min
x_max = y_max*max
# Indicate the minium diference between each y value, note that it
# must be less than (y_max-ymin)/n
diff = 150

def aproves(y_list, y):
    for i in y_list:
        if(abs(y-i) < diff): return False
    return True

def main():
    s = '['
    i = 0
    y_list = [0]
    while i < n:
        x = random.randint(x_min, x_max)
        y = random.randint(y_min, y_max)
        if (x/y >= min and x/y <= max):
            if ( aproves(y_list, y) ):
                y_list.append(y)
                s = s + '[' + str(x) + ', ' + str(y) + '], '
                i += 1

    s = s[:len(s)-2] + ']'
    print(s)

if __name__ == "__main__":
	main()
