import random
def roll_dice():
    die_A=random.randint(1,6)
    die_B=random.randint(1,6)
    return die_A+die_B
def calculate_probabilities(num_rolls=1000):
    sum_counts={sum_val:0 for sum_val in range(2,13)}
    for _ in range (num_rolls):
        sum_val=roll_dice()
        sum_counts[sum_val]+=1
    total_combinations=6*6
    probabilities={sum_val:count/total_combinations for sum_val,count in sum_counts.items()}
    return probabilities

if __name__ == "__main__":
    probabilities=calculate_probabilities()
    print("sum\tprobability")
    for sum_val, probability in probabilities.items():
        print(f"{sum_val}\t{probability:.4f}")
    
    