from Satellite import *

sat_one = Satellite(0.5, "sat_one", 40)
sat_two = Satellite(0.75, "sat_two", 40)
sat_three = Satellite(0.5, "sat_three", 40)
sat_four = Satellite(0.5, "sat_four", 40)

sat_one.add_links([sat_two])

while True:
    sat_one.update_pos()
    sat_two.update_pos()
    if sat_one.check_proximity(sat_two):

        print("close enough")