class Circle {
  
  
   // member variables
   float centerX;
   float centerY;
   float radius;
   float displX;
   float displY;
   float red;
   float green;
   float blue;
   float speed;
   

   
   // Boolean variable
   boolean moveUp = true;
   boolean moveRight = true;
   
   // Constructor function
   Circle(float x, float y, float r,float g,float b,float rad){
     centerX = x;
     centerY = y;
     speed = 1;
     
     displX = 1.5;
     displY = 1.5;
     
     // Color
     red = r;
     green = g;
     blue = b;
     
     radius = rad;
   }
   
   void moveCircle() {
      //  ------------------- X displacement --------------  
      // Check if the circle is on the left edge - the moveRight - true
      if (centerX <= (0 + radius)) {
          moveRight = true; 
    
       }else if (centerX >= width - radius) {
         // Moving left
          moveRight = false; 
       }
  
       if (moveRight == true ) {
           centerX += displX;
   
       }else {
          centerX -= displX; 
       }
  
  // ----------------   Y displacement ----------------------
  if (centerY <= radius) {
     // At the top 
     moveUp = false;
  } else if (centerY >= height - radius) {
     // Bottom up the screen
     moveUp = true; 
  }
  
  if (moveUp == true) {
     centerY  -= displY * speed;
  }else {
     centerY += displY  * speed; 
  }
     
     
   }
  
  
  
  
  
  
}
