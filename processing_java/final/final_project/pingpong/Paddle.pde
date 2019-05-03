class Paddle {
  
   int xPos,yPos;
   float R = random(255);
   float G = random(255);
   float B = random(255);
   
   // Width and length of the paddle
   int xWidth,yLength;
   
   // 0 = player 1, 1 = player 2
   int  player;
   
   Paddle(int x,int y,int playerType) {
     xPos = x;
     yPos = y;
     player = playerType;
     xWidth = 10;
     yLength = 100;
   }
   
     
   void keyPressed() {
        // Paddle can only go up and down, and is bordered by the top and bottom edge of the screen
       if (player == 0 ) {
           if (key == 'w'  && yPos > 0) {
              yPos -= 40;  // yPos = yPos - 7 
             
           }else if (key  == 'z'  && yPos < height - yLength ) {
                yPos += 40; 
           }
          
          
        } else {
             if (key == 'p' && yPos > 0) {
              yPos -= 40;  // yPos = yPos - 7 
             
           }else if (key  == '.') {
                 if (yPos < height - yLength) {
                      yPos += 40; 
                 }
           }  
          
        }
   }
   
   void drawPaddle() {
       // This will be called by the main function pinpong.pde to draw the paddle 
       fill(R,G,B);
       rect(xPos,yPos,xWidth,yLength);
   }
   
   void drawText() {
     // Draw text for the hit and miss from the ball
     
     stroke(0,255,0);
     textSize(20);
     // Player 1
     text("Hit ",100,height -50);
     text("Miss ", 200, height - 50);
     
     
     // Player 2
     text("Hit ", width -200,height - 50);
     text("Miss ", width -100,height - 50);
     
     text(str(hitCount) , 105,height -75);
     text(str(hitCount2) , 505,height -75);
     
     text(str(missCount) , 205,height -75);
     text(str(missCount2) , 605,height -75);
     
   }
   void missHit() {
      missCount += 1; 
   }
   void missHit2() {
      missCount2 += 1; 
   }
   void incrementHit() {
      hitCount += 1; 
   }
   void incrementHit2() {
      hitCount2 += 1;
   }
 
  
}
