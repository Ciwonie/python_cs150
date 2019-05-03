
Ball ball;
Paddle paddle1, paddle2;
int hitCount = 0;
int hitCount2 = 0;
int missCount;
int missCount2;

void setup() {
  size(700,700);
  

  ball = new Ball(350,500,60);
  paddle1 = new Paddle(100,320,0);
  paddle2 = new Paddle(600,320,1);
  
  
}


void draw() {
 
    background(255,255,255);
    
    ball.updatePosition(paddle1,paddle2);
    ball.drawBall();
 
    paddle1.drawPaddle();
    paddle1.drawText();
    

    paddle2.drawPaddle();
}



void mousePressed() {
    // Do any mouse pressed actions here, and delegate them to the instantiated objects 
  
}

void keyPressed() {
   // Do any key pressed action here
   paddle1.keyPressed();
   paddle2.keyPressed();
}
