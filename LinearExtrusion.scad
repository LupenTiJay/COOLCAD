for(j = [0:90:360]){
    rotate([0,0,j]){
for( i = [180: 20: 720]){
rotate([i,0,0]){
linear_extrude(height = 2, center = false, convexity = 10, twist = 45, $fn = 100)
translate([i/100, i/100, 0])
circle(r = 0.5, $fn = 3);
}
}
}
}