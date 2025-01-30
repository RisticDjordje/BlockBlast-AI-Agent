import subprocess

def save_score(score):
    with open("high_score.txt", "w") as file:
        file.write(str(score))
        
    subprocess.run(["hash_decrypt", "hash"])

def get_score():
    subprocess.run(["hash_decrypt", "decrypt"])
    
    with open("high_score.txt", "r") as file:
        score = file.read()
    
    save_score(score)
    return int(score)
