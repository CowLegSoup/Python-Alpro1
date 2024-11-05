def reverse(s):
    if len(s)<2:
        return s
    first, rest = s[0],s[1:]
    return reverse(rest)+first
    
reverse('erlang suka ciwa')
