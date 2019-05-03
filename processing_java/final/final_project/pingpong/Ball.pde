class Ball {
   int xc,yc;
   float R,G,B;
   int radius;
   
   
   boolean moveLeft, moveUp, delayBall;
  
  Ball(int x, int y, int r) {
    
      xc = x; yc = y; radius = r;
      R = random(255);
      G = random(255);
      B = random(255);
      java.awt.Toolkit.getDefaultToolkit().beep();
  }
  
  // This functions will be called by the pingpong.pde draw callback function
  
  void updatePosition(Paddle paddle1,Paddle paddle2) {
      
      // Player 1 
      if ( (xc < paddle1.xPos + paddle1.xWidth + (radius/2))
           &&  (yc > paddle1.yPos) 
           &&  (yc < paddle1.yPos + paddle1.yLength) 
      
          ) {
            
           // Ball is detected on player 1 paddle
           moveLeft  = false;
           paddle1.incrementHit();
           //float R = random(255);
           //float G = random(255);
           //float B = random(255);
           //java.awt.Toolkit.getDefaultToolkit().beep();
           
        
      } else if ( (xc > paddle2.xPos - (radius/2))
           &&  (yc > paddle2.yPos) 
           &&  (yc < paddle2.yPos + paddle2.yLength)) {
        // Ball detected on player 2 paddle
        moveLeft = true;
        paddle2.incrementHit2();
        //float R = random(255);
        //float G = random(255);
        //float B = random(255);
        //java.awt.Toolkit.getDefaultToolkit().beep();
      }
      
      if ( yc < radius/2  ) {
           // Ball is at the top 
           // Increment paddle1  ( example this should 
           // not be in your program
           moveUp = false;
           
        
      } else if (yc  > height - radius/2)  {
        moveUp = true;
      }
      
      if ( xc > width + radius) {
         xc = (width/2);
         yc = (height/2);
         moveLeft  = true;
         paddle1.missHit2();
         delayBall = true;
         
      } else if (xc < -radius) {
        moveLeft = false;
        xc = (width/2);
        yc = (height/2);
        paddle2.missHit();
        delayBall = true;
      }
      
      if (delayBall == true) {
        delay(1000);
        delayBall = false;
      }
    
    
  }
  
  void drawBall() {
    
      if ( moveUp == true ) {
         yc -= 3; 
      }else {
         // Move down
         yc += 3; 
      }
      
      if (moveLeft == true) {
         //xc = xc - 3; 
         xc -= 3;
      } else {
         // Moving to the right
         xc += 3; 
        
      }

      
      fill(R,G,B);
      ellipse(xc,yc,radius,radius);
      
      
    
  }
}
