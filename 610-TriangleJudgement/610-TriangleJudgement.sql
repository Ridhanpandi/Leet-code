-- Last updated: 31/07/2026, 08:54:01

select *, if(x+y>z and y+z>x and x+z>y, "Yes","No") as triangle from triangle