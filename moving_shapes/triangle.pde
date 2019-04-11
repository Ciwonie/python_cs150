class Triangle {
  
  
   // member variables
   float triangleX1;
   float triangleY1;
   float triangleX2;
   float triangleY2;
   float triangleX3;
   float triangleY3;
   
   float displ;
   
   float red;
   float green;
   float blue;
   
   float speed;
   
   // Boolean variable
   boolean moveDown = true;
   
   // Constructor function
   Triangle(float x1, float y1, float x2, float y2, float x3, float y3, float r,float g,float b){
     
     triangleX1 = x1;
     triangleY1 = y1;
     triangleX2 = x2;
     triangleY2 = y2;
     triangleX3 = x3;
     triangleY3 = y3;
     
     speed = 1;
     
     displ = 1.5;
     
     // Color
     red = r;
     green = g;
     blue = b;
   }
   
  void moveTriangle() {
 
    if (triangleY2 <= 0 ) {
      moveDown = true;
    } else if ( triangleY3 >= height ) {
       moveDown = false; 
    }
    
    if (moveDown == true) {
      triangleY1 += displ * speed;
      triangleY2 += displ * speed;
      triangleY3 += displ * speed;
    } else {
      triangleY1 -= displ * speed; 
      triangleY2 -= displ * speed;
      triangleY3 -= displ * speed;
    }
  
  }
  
  
  
  
  
}
