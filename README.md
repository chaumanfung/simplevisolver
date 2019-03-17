# simplevisolver (created in Python 2.7)
restructured on 10 march \
calculations of profits and surpluses added.\
plots of all variables showing convergence.\

# modified projection method and Euler method
run2.py (Euler method)\
run3.py (modified projection method; in chapter and slides)\
# available examples
  #Examples in Nagurney A, 2006. Supply Chain Network Economics (Chapter 2)\
  (def_class1.py, def_class2.py, def_class3.py, def_class4.py, def_class5.py, def_class6.py, def_class7.py, def_class8.py)\
  #direct link between manufacturer and market \
  (def_class_SCE.py)\
  #increase costs across geographical border\
  (def_class_brexit.py, def_class_brexit_post.py)\
  #more examples (coming soon)\
  expiration of patent, off-hour delivery regulation, lockers and drones, demand elasticities\

# starting.py
contains starting values, epsilon and max number of iterations\

# To Run: 
Change the name of the example file you want to run in the import line of run.py.\
Change the starting values and epsilon.\
Change the example file (def_class.py) if necessary:\
  Change number of manufacturers, retailers, markets (and connections between them using classes "Make, Retail and Buy"\
  Change the functions (production, cost and demand)\
Run the run2.py or run3.py.\

# Coming Soon:
More examples + descriptions\
Speed things up\
Trust region algorithm\



