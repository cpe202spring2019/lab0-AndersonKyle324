def weight_on_planets():
   # write your code here
   earthWeight = int(input("What do you weigh on earth? "))
   marsWeight = earthWeight * .38
   jupWeight = earthWeight * 2.34
   print("\nOn Mars you would weigh", marsWeight, "pounds.\nOn Jupiter you would weigh", jupWeight, "pounds.")    
   
   
if __name__ == '__main__':
   weight_on_planets()
