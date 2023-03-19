import turtle as t

window = t.Screen()
window.title("INDIAN FLAG")
window.setup(width=800,height=500)

#ASHOKA CHAKRA:
cursor = t.Turtle()
cursor.speed(100)
cursor.home()
cursor.color("blue")
cursor.begin_fill()
cursor.dot(5)
cursor.end_fill()
cursor.lt(90)
cursor.fd(50)
cursor.lt(90)
    
for i in range(24):
    cursor.circle(50, 15)
    cursor.lt(90)
    cursor.fd(50)
    cursor.bk(50)
    cursor.rt(90)
    
#ORANGE COLOR
cursor.color("black", "orange")
cursor.begin_fill()
cursor.fd(200)
cursor.bk(400)
cursor.rt(90)
cursor.fd(100)
cursor.lt(90)
cursor.fd(400)
cursor.lt(90)
cursor.fd(100)
cursor.end_fill()
    
#WHITE COLOR
cursor.color("black", "")
cursor.begin_fill()
cursor.fd(100)
cursor.lt(90)
cursor.fd(400)
cursor.lt(90)
cursor.fd(100) 
cursor.bk(100)
cursor.end_fill()
    
#GREEN COLOR
cursor.color("black", "green")
cursor.begin_fill()
cursor.bk(100)
cursor.lt(90)
cursor.fd(400)
cursor.rt(90)
cursor.fd(100)
cursor.end_fill()
    
t.done()