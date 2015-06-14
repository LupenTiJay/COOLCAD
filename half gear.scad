   numOfTeeth = 25;
   angle = 180;
   radius = .25;
   height = .25;
   for(i = [0: angle/numOfTeeth: angle]){
       
        translate([cos(i),sin(i),0]){rotate([0,0,i]){
            difference(){
                cylinder( h =height, r = radius, $fn = 3, center = true);

                translate([radius - 0.04,0,0]){
                    cylinder(h = height+.1, r = .045, $fn = 3, center = true);
                    }
                }
            } 
        } 
    }
   
   
   difference(){
        cube(size = [1.75,.5*cos(30),height], center = true);
  
   
        cylinder( h = height + .1, r = 0.1, $fn = 1000, center = true);
        translate([0,0,height / 2]){
            cylinder( h =  .25*height, r = 0.17, $fn = 6, center = true);    
        }
        
   }
   
    
   
   
   
   
   
   
   
   
   
   
  