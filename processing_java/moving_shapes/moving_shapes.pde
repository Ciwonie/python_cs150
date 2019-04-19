Circle circle;
Circle circle1;
Square square;
Triangle triangle;

boolean circleOn = false;
boolean squareOn = false;
boolean triangleOn = false;

// Boolean variable is either true or false
// if true the circle moves to the right 
// if false the circle moves to the left
boolean moveRight = true;
boolean circleMoveUp = true;

void setup() {
   // Bring up window resolution 600 x 600 ( pixels)
   size(600,600); 
   circle = new Circle(100,100,255,0,0,30);
   circle1 = new Circle(300,50,0,255,0,25);
   square = new Square(500, 100, 216, 17, 89);
   triangle = new Triangle(30, 75, 58, 20, 86, 75, 25, 10, 100); 
}

void draw() {
  
  background(255,255,255);
   circle.moveCircle();
   circle1.moveCircle();
   square.moveSquare();
   triangle.moveTriangle();
   
   if (circleOn == true) {
     ellipseMode(RADIUS);
     fill(circle.red,circle.green,circle.blue);
     ellipse(circle.centerX,circle.centerY,circle.radius,circle.radius); 
   
     fill(circle1.red,circle1.green,circle1.blue);
     ellipse(circle1.centerX,circle1.centerY,circle1.radius,circle1.radius); 
   }
  
  if (squareOn == true) {
     rectMode(CORNER);  // Set rectMode to CORNER
     fill(square.red, square.green, square.blue);
     rect(square.squareX,square.squareY,50,50);
  }
  
  if (triangleOn == true) {
    fill(triangle.red, triangle.green, triangle.blue);
    triangle(triangle.triangleX1, triangle.triangleY1, triangle.triangleX2, triangle.triangleY2, triangle.triangleX3, triangle.triangleY3);
  }

}


// This is the callback function that is executed when hitting a key
void keyPressed() {
    
    if (keyCode == LEFT) {
       // Losing 5% of my speed each time the key is pressed
       circle.speed *= .95; 
       square.speed *= .90;
    } else if (keyCode == RIGHT) {
       // Gaining 5% more speed each time the key is pressed 
       circle.speed *= 1.05;
       square.speed *= 1.05;
    }
    
    if (key == 'c') {
       // Toggle the circle on and off
       if (circleOn == true) {
          circleOn = false; 
       }else {
          circleOn = true; 
       }
       
    }
    
    if (key == 's') {
       // Toggle the square on and off
       if (squareOn == true) {
          squareOn = false; 
       }else {
          squareOn = true; 
       }
       
    }
    
    if (key == 't') {
      if (triangleOn == true) {
       triangleOn = false; 
      } else {
          triangleOn = true;
      }
    }
    
}

// triangle math
// we need to take y = y3 + (y2-y3)/2
// x = x1 + (x2-x1)/2
// picture
//          x3, y3
//          /  \
//         /    \  
//        /  *   \
///x1,y1 /________\


// square math
// shape of the square is:
// x,y --------- x+w, y
//  |              |
//  |              |
//  |              |
// x,y+h ------- x+w, y+h

// if mousex > x && mouse x < x+w && mouse y > y && mouse y < y+h
// inSquare = true

void mousePressed() {
  
   if (dist(circle.centerX,circle.centerY,mouseX,mouseY) <= circle.radius) {
       circle.red = random(255);
       circle.green = random(255);
       circle.blue = random(255);
   }
   
   if (dist(circle1.centerX,circle1.centerY,mouseX,mouseY) <= circle1.radius) {
       circle1.red = random(255);
       circle1.green = random(255);
       circle1.blue = random(255);
   }
   
   if (dist(square.squareX,square.squareY,mouseX,mouseY) <= square.squareY) {
       square.red = random(255);
       square.green = random(255);
       square.blue = random(255);
   }
   
   if (dist(triangle.triangleX1,triangle.triangleY1,mouseX,mouseY) <= triangle.triangleY2) {
       triangle.red = random(255);
       triangle.green = random(255);
       triangle.blue = random(255);
   }
   

    
}
