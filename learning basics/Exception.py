while True:
    try:
        number = int(input("Enter a number: "))
        print("Inverse of your no. = ", 1/number)
        break
    except ValueError:
        print('Make sure that you enter a number.')
    except ZeroDivisionError:
        print("Inverse of your no. = DNE")
    finally:
        print("done!")