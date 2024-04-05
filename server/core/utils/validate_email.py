def validate_email(email):
    SPECIAL_CHARS = ['!', '#', '$', '%', '&', '\'', '*', '+', '-', '/', '=', '?', '^', '_', '`', '{', '|', '}', '~', '.', ',']
    ALLOWED_CHARS = ['.', '-'] # allowed characters in domain portion
    MAX_LOCAL_LENGTH = 64
    MAX_DOMAIN_LENGTH = 255
    MAX_SUBDOMAIN_LENGTH = 63
    MAX_LENGTH = MAX_LOCAL_LENGTH + MAX_DOMAIN_LENGTH + 1 # +1 for '@'

    # empty
    if not email:
        return False
    
    # does not contain '@'
    if '@' not in email:
        return False
    
    # contains space
    if ' ' in email:
        return False
    
    # contains multiple '@'
    if email.count('@') > 1:
        return False
    
    # too short or too long
    if len(email) < 3 or len(email) > MAX_LENGTH:
        return False
    
    local, domain = email.split('@')

    # LOCAL VALIDATION
    # local is empty or too long
    if not local or len(local) > MAX_LOCAL_LENGTH:
        return False
    
    # has double special characters
    for special in SPECIAL_CHARS:
        if special * 2 in local:
            return False
        
    # has special character at beginning or end
    if local[0] in SPECIAL_CHARS or local[-1] in SPECIAL_CHARS:
        return False
    
    # DOMAIN VALIDATION
    # domain is empty or too long
    if not domain or len(domain) > MAX_DOMAIN_LENGTH:
        return False
    
    # has special characters
    for special in SPECIAL_CHARS:
        if special in ALLOWED_CHARS:
            continue

        if special in domain:
            return False
        
    # SUBDOMAIN VALIDATION
    subdomains = domain.split('.')

    # must have at least two subdomains (domain and tld)
    if len(subdomains) < 2:
        return False
    
    for sub in subdomains:
        # subdomain is too short or too long
        if len(sub) < 1 or len(sub) > MAX_SUBDOMAIN_LENGTH:
            return False
        
        # starts or ends with an ALLOWED_CHAR
        if sub[0] in ALLOWED_CHARS or sub[-1] in ALLOWED_CHARS:
            return False
        
    # TLD VALIDATION
    tld = subdomains[-1]

    # tld is too short
    if len(tld) < 2:
        return False
    
    return True
        


