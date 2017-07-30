import hashlib, string, random, datetime

from eajforms.forms.models import ApplyForm

def generate_hash_key(salt, random_str_size=5):
    random_str = random_key(random_str_size)
    text = random_str + salt
    generate_hash = hashlib.sha224(text.encode('utf-8')).hexdigest()
    
    if ApplyForm.objects.filter(access_code=generate_hash).exists():
        return generate_hash_key(salt, random_str_size)

    return generate_hash