from itertools import product
def cal_probabilities(die_a,die_b):
    total_combinations=0
    probabilities={}
    
    for face_a,face_b in product(die_a,die_b):
        current_sum=face_a+face_b
        probabilities[current_sum]=probabilities.get(current_sum,0)+1
        total_combinations += 1
    for key in probabilities:
        probabilities[key]/= total_combinations
    return probabilities
def undoom_dice(die_a,die_b):
    original_probabilities=cal_probabilities(die_a,die_b)
    
    new_die_a= []
    for face_a in die_a:
        face_a_probabilities={}
        for face_b in die_b:
            current_sum=face_a+face_b
            face_a_probabilities[current_sum]=original_probabilities.get(current_sum,0)
        max_spots=min(4,max(face_a_probabilities,key=face_a_probabilities.get))
        new_die_a.append(max_spots)
    
    new_die_b= die_b
    return new_die_a,new_die_b
die_a=[1,2,3,4,5,6]
die_b=die_a
new_die_a,new_die_b= undoom_dice(die_a,die_b)
print("original_die_a:",die_a)
print("original_die_b:",die_b)
print("new_die_a:",new_die_a)
print("new_die_b:",new_die_b)
    
