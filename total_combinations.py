die_faces=[1,2,3,4,5,6]
total_combinations=0
for face_A in die_faces:
    for face_B in die_faces:
        current_sum=face_A+face_B
        print(f"die A :{face_A},die B:{face_B},sum:{current_sum}")
        total_combinations+=1
        
print(f"Total_combinations:{total_combinations}")