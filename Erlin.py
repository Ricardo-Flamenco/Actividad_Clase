import turtle


ventana = turtle.Screen()
ventana.bgcolor("black")  
ventana.title("Mi primera figura - Turtle")


pen = turtle.Turtle()
pen.shape("turtle")       
pen.color("cyan")        
pen.pensize(3)            
pen.speed(3)             


for i in range(4):
    pen.forward(100)     
    pen.right(90)        

ventana.mainloop()