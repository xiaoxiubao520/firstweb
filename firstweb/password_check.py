import re  
  
def validate_password(password):  
    """  
    验证密码是否满足以下要求：  
    1. 至少包含一个小写字母  
    2. 至少包含一个大写字母  
    3. 至少包含一个数字  
    4. 至少包含一个特殊字符（如!@#$%^&*()-+）  
    5. 长度至少为8个字符  
    """  
    if len(password) < 8:  
        return False  
      
    if not re.search("[a-z]", password):  
        return False  
      
    if not re.search("[A-Z]", password):  
        return False  
      
    if not re.search("[0-9]", password):  
        return False  
      
    if not re.search("[!@#$%^&*()-+.]", password):  
        return False  
      
    return True  
