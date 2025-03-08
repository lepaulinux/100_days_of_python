def calculate_love_score(name1, name2):
    # Combine both names and convert to lowercase
    combined_names = (name1 + name2).lower()
    
    # Count occurrences of letters in "TRUE"
    true_count = sum(combined_names.count(letter) for letter in "true")
    
    # Count occurrences of letters in "LOVE"
    love_count = sum(combined_names.count(letter) for letter in "love")
    
    # Form the two-digit love score
    love_score = int(str(true_count) + str(love_count))
    
    print(f"{love_score}")
    

calculate_love_score("Jack", "Rose")
