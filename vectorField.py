"""

Vector fields associate a 2D vector to each point of the 2D plane. Vector fields are common in Physics as they provide solutions to differential equations. Matplotlib provides functions to visualize vector fields. To illustrate the visualization of vector fields, let's visualize the velocity flow of an incompressible fluid around a cylinder. We do not need to bother about how to compute such a vector field but only about how to show it. The pyplot.quiver() function is what we need. 

How the project work: 

Although the script is a bit long, the purely graphical part is simple. The vector field is stored in the matrices U and V: the coordinates of each vector we sampled from the vector field. The matrices X and Y contain the sample positions. The matrices X, Y, U, and V are passed to pyplot.quiver(), which renders the vector field. Note that pyplot.quiver() can take just U and V as parameters, but then the legend will show the indexes of the samples rather than their coordinates. As the vector field that we used as an illustration here the fluid flow around a shape, the shape itself is shown as follows:



shape = patches.Circle((0, 0), radius = 1., lw = 2., fc = 'w', ec 

 = 'k', zorder = 0) 

plt.gca().add_patch(shape)



The vector field inside the cylinder does not appear; we use a masked array. We first create a mask that defines which samples should be shown. Then, we apply this mask on U and V, as shown in the following script: 

"""

import numpy as np

import sympy 

from sympy.abc import x, y 

from matplotlib import pyplot as plt 

import matplotlib.patches as patches 

plt.style.use("dark_background")

fig = plt.figure(figsize=(3.641, 3.295), dpi=100)

def cylinder_stream_function(U = 1, R = 1): 

    r = sympy.sqrt(x ** 2 + y ** 2) 

    theta = sympy.atan2(y, x) 

    return U * (r - R ** 2 / r) * sympy.sin(theta) 

 

def velocity_field(psi): 

    u = sympy.lambdify((x, y), psi.diff(y), 'numpy') 

    v = sympy.lambdify((x, y), -psi.diff(x), 'numpy') 

    return u, v 

 

U_func, V_func = velocity_field(cylinder_stream_function() ) 



xmin, xmax, ymin, ymax = -2.5, 2.5, -2.5, 2.5

Y, X = np.ogrid[ymin:ymax:19j, xmin:xmax:16j] 

U, V = U_func(X, Y), V_func(X, Y) 



M = (X ** 2 + Y ** 2) < 1

U = np.ma.masked_array(U, mask = M) 

V = np.ma.masked_array(V, mask = M) 



shape = patches.Circle((0, 0), radius = 1, lw = 2, fc = 'w', ec 

    = 'k', zorder = 0) 

 

plt.gca().add_patch(shape) 

plt.quiver(X, Y, U, V, zorder = 1, color="red") 

plt.xticks([])

plt.yticks([])

plt.grid(False)

plt.box(False)

plt.suptitle('Vector fields are well-known to provide solutions of differentialⁿ equations!', fontsize=6, color="white")

plt.title('Vector Fields', color="white", fontsize=10)

plt.figtext(0.82, 0.01, "© Mǟɖ↻ôɖɆⱤ™", color="white", fontsize=6)

plt.show()

plt.savefig('myfig.png', dpi= 200)
