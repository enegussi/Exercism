def response(hey_bob):
    
    msg = hey_bob.strip() 

    if msg == "":
        return "Fine. Be that way!"
    
    has_letters = any(ch.isalpha() for ch in msg)
    is_yelling = has_letters and msg.upper() == msg
    is_question = msg.endswith("?")

    
    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    if is_yelling:
        return "Whoa, chill out!"
    if is_question:
        return "Sure."
    return "Whatever."