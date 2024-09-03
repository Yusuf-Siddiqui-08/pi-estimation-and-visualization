# Pi Estimation and Visualization

## Estimation:

### How we know the area of a circle formula
To estimate $ \pi $, we must first understand how we know the formula of a circle to be a constant ($ \pi $) multiplied by the radius squared. 
Archimedes used integral calculus to find that when we cut a circle into infinite slices and put them side by side, we get a perfect rectangle.

For more info:

[<img alt="for more info" height="150" src="https://i.ytimg.com/vi/YokKp3pwVFc/maxresdefault.jpg" width="200"/>](http://www.youtube.com/watch?v=YokKp3pwVFc).

With this rectangle, we find that the length is half the circumference, and the width is the radius. 
Using the area of a rectangle formula, when we multiply half the circumference by the radius we get the area of a circle:
$$
\frac{2 \pi r}{2} \times r = \pi r^2
$$
But when estimating $ \pi $, we must pretend we don't know $ \pi $. So, all we know is that the area of a circle is equal to a constant $ \times r^2$. 
### Estimating pi
In this program, we estimate $ \pi $ in a very similar way Archimedes did, using a regular polygon inscribed inside a circle. 
With this polygon with $n$ sides, we can measure the apothem of each triangle using the following formula:

Where $A$ is the inside angle formed from the two legs of the triangle with length radius and
$a$ is the length of the apothem.

$$
\begin{split}
\cos A  = \frac{a}{r} \\
r\cos A = a
\end{split}
$$
Therefore, the apothem of each triangle in the polygon, is equal to $r\cos A$.

With the apothem, we can calculate the area of each triangle using $\frac {bh}{2}$ where the base of each triangle is the side length of the polygon and the height is the apothem.
With the area of each triangle, we can multiply this my $n$ to get the exact area of the polygon.

Finally, with the area of the polygon, we can input that as the area of the circle into our area formula which is a constant $ \times r^2$. 

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