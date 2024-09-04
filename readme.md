# Pi Estimation and Visualization

## Estimation:

### How we know the area of a circle formula
To estimate $\pi$, we must first understand how we know the formula of a circle to be a constant ($\pi$) multiplied by the radius squared. 
Archimedes used integral calculus to find that when we cut a circle into infinite slices and put them side by side, we get a perfect rectangle.

For more info:

[<img alt="for more info" height="150" src="https://i.ytimg.com/vi/YokKp3pwVFc/maxresdefault.jpg" width="200"/>](http://www.youtube.com/watch?v=YokKp3pwVFc).

With this rectangle, we find that the length is half the circumference, and the width is the radius. 
Using the area of a rectangle formula, when we multiply half the circumference by the radius we get the area of a circle:
$$\frac{2 \pi r}{2} \times r = \pi r^2
$$
But when estimating $\pi$, we must pretend we don't know $\pi$. So, all we know is that the area of a circle is equal to a constant $\times r^2$. 
### Estimating pi
In this program, we estimate $\pi$ in a very similar way Archimedes did, using a regular polygon inscribed inside a circle. 
With this polygon with $n$ sides, we can measure the apothem of each triangle using the following formula:

Where $A$ is the inside angle formed from the two legs of the triangle with length radius and
$a$ is the length of the apothem.


$$\begin{split}
\cos A  = \frac{a}{r} \\
r\cos A = a
\end{split}
$$

Therefore, the apothem of each triangle in the polygon, is equal to $r\cos A$.

With the apothem, we can calculate the area of each triangle using $\frac {bh}{2}$ where the base of each triangle is the side length of the polygon and the height is the apothem.
With the area of each triangle, we can multiply this my $n$ to get the exact area of the polygon.

Finally, with the area of the polygon, we can input that as the area of the circle into our area formula which is a constant $\times r^2$. 

$$
\begin{split}
Area_{circle} \approx Area_{polygon} \\
Area_{polygon} = constant \times r^2
\end{split}
$$

Knowing the area of the polygon and the radius, we can solve for the unknown constant which would be an approximation of $\pi$. 

## Visualization

To make the visualization, I used the Turtle graphics module. 
For the controls, I used the listen method and everytime the user inputted a key or mouse press, the program performs all the calculations and re-renders the drawing again.

## Benchmark/Testing
### Things to Note:
* The actual circle area remains the same throughout
* All of these tests were performed in as similar of an environment to one another. Meaning, I ran the same background apps (Google Chrome, etc.) and held the tests on the same computer with the same specs ONE AT A TIME.
* My PC specs are as follows: 

| CPU                              	| GPU                     	| RAM  	| OS         	| Python Version 	| IDE                                  	|
|----------------------------------	|-------------------------	|------	|------------	|----------------	|--------------------------------------	|
| 11th Gen Intel i5-11400 @ 2.6GHz 	| NVIDIA GeForce RTX 3060 	| 16GB 	| Windows 11 	| Python 3.11    	| PyCharm Community Version 2024.2.0.1 	|
* Render duration increases at a fairly consistent and linear rate
* The 96-sided polygon is the last polygon Archimedes approximating $\pi$ on (granted his method was slightly more complicated and accurate than what this program replicates).
* The first time we reach $\pi$ accurate to 5 decimals places (3.14159) is with a polygon with just below 5000 sides.

### Results:
| Number of Sides 	| Actual Circle Area 	| Polygon Area       	| Pi Estimate        	| Pi Error                 	| Render Duration    	|
|-----------------	|--------------------	|--------------------	|--------------------	|--------------------------	|--------------------	|
| 3               	| 49.483152130933064 	| 20.461118704751872 	| 1.2990381056766584 	| 1.8425545479131347       	| 0.9379889965057373 	|
| 4               	| 49.483152130933064 	| 31.501953045624983 	| 1.9999999999999987 	| 1.1415926535897944       	| 1.0251493453979492 	|
| 5               	| 49.483152130933064 	| 37.45017215008198  	| 2.3776412907378814 	| 0.7639513628519117       	| 1.0590147972106934 	|
| 6               	| 49.483152130933064 	| 40.92223740950367  	| 2.5980762113533125 	| 0.5435164422364807       	| 1.1340358257293701 	|
| 7               	| 49.483152130933064 	| 43.1011326380236   	| 2.7364101886380974 	| 0.40518246495169574      	| 1.1997427940368652 	|
| 8               	| 49.483152130933064 	| 44.55048923836323  	| 2.828427124746185  	| 0.31316552884360815      	| 1.2585244178771973 	|
| 9               	| 49.483152130933064 	| 45.560396471973434 	| 2.8925442435894224 	| 0.2490484100003707       	| 1.334967851638794  	|
| 10              	| 49.483152130933064 	| 46.29095854657074  	| 2.9389262614623597 	| 0.20266639212743343      	| 1.3704252243041992 	|
| 20              	| 49.483152130933064 	| 48.67319423549873  	| 3.09016994374947   	| 0.051422709840323044     	| 2.064829111099243  	|
| 50              	| 49.483152130933064 	| 49.353020484988214 	| 3.1333308391076007 	| 0.008261814482192431     	| 5.422649145126343  	|
| 75              	| 49.483152130933064 	| 49.42529046775846  	| 3.1379191249618508 	| 0.0036735286279423462    	| 5.596475839614868  	|
| 96              	| 49.483152130933064 	| 49.44783134507798  	| 3.1393502030468747 	| 0.002242450542918384     	| 6.798015832901001  	|
| 100             	| 49.483152130933064 	| 49.450599948071165 	| 3.1395259764656953 	| 0.0020666771240978044    	| 7.013974905014038  	|
| 250             	| 49.483152130933064 	| 49.47794291800626  	| 3.141261930417217  	| 0.00033072317257598627   	| 16.565859079360962 	|
| 500             	| 49.483152130933064 	| 49.48184979686067  	| 3.1415099708386314 	| 0.0000826827511617445    	| 32.386380672454834 	|
| 1000            	| 49.483152130933064 	| 49.48282654549867  	| 3.141571982780341  	| 0.000020670809452116856  	| 63.49086785316467  	|
| 2500            	| 49.483152130933064 	| 49.483100037209645 	| 3.141589346256858  	| 0.000003307332935076346  	| 158.71818161010742 	|
| 5000            	| 49.483152130933064 	| 49.48313910744267  	| 3.1415918267527796 	| 0.0000008268370135233738 	| 314.69306540489197 	|

### Graphs:
#### Relation of the number of sides on the polygon to the $\pi$ error
![Relation of the number of sides on the polygon to the $\pi$ error](/read_me_src/pi_error_num_sides.png)
#### Relation of the number of sides on the polygon to the render duration
![Relation of the number of sides on the polygon to the render duration](/read_me_src/render_duration_num_sides.png)