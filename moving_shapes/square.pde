class Square {
  
  
   // member variables
   float squareX;
   float squareY;
   float displX;
   float displY;
   float red;
   float green;
   float blue;
   float speed;
   

   
   // Boolean variable
   boolean moveDown = true;
   boolean moveRight = true;
   
   // Constructor function
   Square(float x, float y, float r,float g,float b){
     squareX = x;
     squareY = y;
     speed = 1;
     
     displX = 1.5;
     displY = 1.5;
     
     // Color
     red = r;
     green = g;
     blue = b;
   }
   
  void moveSquare() {
 
    if (squareY <= 0) {
      moveDown = true; 
    } else if ( squareY >= height - 50 ) {
       moveDown = false; 
    }
    
    if (moveDown == true) {
      squareY += displY * speed;
    } else {
      squareY -= displY * speed; 
    }
  
  }
  
  
  
  
  
}
