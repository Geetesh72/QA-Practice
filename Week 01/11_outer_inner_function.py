def outer():
    msg ='Hello'
    def inner():
        print(msg)
    inner()

outer()        