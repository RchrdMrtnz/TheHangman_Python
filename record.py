import time
date=time.ctime()
def record():
    try:
        record=open("record.txt","a")
        hall_of_fame=input("Congratulations you win, tell me your name to put it in the hall of fame \n")
        texto=f"This stupid win \"{hall_of_fame}\" the day {date}\n"
        record.write(texto)
        record.close
    except SyntaxError:
        record=open("record.txt","w")
def leer():  
    leer_archivo=open("record.txt","r")
    leer=leer_archivo.read()
    leer_archivo.close
    print(leer)
if __name__ == "__main__":
    record()
    leer()

