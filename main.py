temp =int(input("whats the temperature? "))
choice = int(input("type 1 for fahenheit-to-centigrade. type 2 for centigrade-to-farenheit. "))
if choice == 1:
    print((9*temp + (32 * 5))/5)
elif choice == 2: 
    print((5/9) * (temp - 32))