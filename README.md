# simplevisolver (created in Python 2.7)
changes on 26 april:

use "lambdify" to replace "subs" in sympy\
use numpy arrays instead of lists (fewer for-loops)

Additions on 24 april:

Three examples added with descriptions

Changes on 1 april:

Allow stepsize (alpha) to adjust in iterations:\
(CAUTION: The lower bound of stepsize should not be too low, in case the iterations stop prematurely)\
a/ decrease alpha when values are oscillating\
b/ decrease alpha in later iterations (close to solution)\
c/ decrease alpha when the values become zero\
d/ increase alpha, otherwise\
(This allows us to start with a large stepsize and decrease when things go wrong)\
profits ,etc are shown with the results.\
plots of different variables and step size are shown with the results.


# simple projection and modified projection method
run_test.py (projection with varying stepsize)\
run_test3.py (modified projection with varying stepsize)\
run2.py (projection)\
run3.py (modified projection method; in chapter and slides)

# available examples
  Examples in Nagurney A, 2006. Supply Chain Network Economics (Chapter 2)\
  (def_class1.py, def_class2.py, def_class3.py, def_class4.py, def_class5.py, def_class6.py, def_class7.py, def_class8.py)\
  direct link between manufacturer and market \
  (def_class_SCE.py)
  
  set_a.docx: Brexit\
  (def_class222.py, def_class222b.py)\
  set_b.docx: Expiration of patent\
  (def_class121.py, def_class121b.py)\
  set_c.docx: Relocation of wholesale outlet\
  (def_class241.py, def_class241b.py)

# starting.py
contains starting values, epsilon and max number of iterations

# To Run: 
Change the name of the example file you want to run in the import line of run.py.\
Change the starting values and epsilon.\
Change the example file (def_class.py) if necessary:\
  Change number of manufacturers, retailers, markets (and connections between them using classes "Make, Retail and Buy"\
  Change the functions (production, cost and demand)\
Run run_test.py, run_test3.py, run2.py or run3.py.





