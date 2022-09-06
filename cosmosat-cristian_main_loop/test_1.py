def error():
    1/0

try:
    error()
except:
    print('unoi entre 0')