// touching the perimeter with a square, what do we have to be mindful of?
// we build our square with x1 y1 coordinates. 
// when x1 is < 0, moveLeft = false
// when x1 is > width - x1, moveLeft = true
// what about moving up and down?
// if y1 < 0, moveDown = true
// if y1 > height - y1, moveDown = false



// Triangles
// x1 y1, x2 y2, x3 y3
// y1 and y2 are the base. y3 is the pointed top. therefore is y3 < 0, moveDown = true
// if y1 or y2 > height - (y1 or y2), moveDown = false
