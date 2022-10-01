#user defined functions (with default argument)
def a(qty):
    print("price :",qty*40,"Rs.")

def b(qty):
    print("price :",qty*80,"Rs.")

#here we use default argument
def c(qty = 1):
    print("price :",qty*40,"Rs.")
