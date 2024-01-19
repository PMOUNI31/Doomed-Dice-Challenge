die_faces=[1,2,3,4,5,6]
distribution_matrix=[[0]*6 for _ in range(6)]
for face_A in die_faces:
    for face_B in die_faces:
        current_sum=face_A+face_B
        distribution_matrix[face_A-1][face_B-1]+=1
        
print("distribution_matrix:")
for row in distribution_matrix:
    print(row)