import re


# # Stemming function using the given regex pattern
steming = {
        ('taa' , ''),  # padhtaa -> padh
        ('naa' , ''),  #likhnaa -> likh
        ('ai' , ''),  # sunai -> sun
        ('ti' ,''),  # gati -> ga
        ('te', ''),  # chalte -> chal  
        ('na' , ''), # jaana -> ja
        ('ta' , '') # uthta -> uth
    }


def stem_word(w):
    for rules in steming:
            suffix, replace = rules
            if w.endswith(suffix):
                w = w[:-len(suffix)] + replace
    return w
    # return re.sub(r'(.{2,}?)([aeiougyn]+$)', r'\1', word)
