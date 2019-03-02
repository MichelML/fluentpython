def clip(text: str, max_len: 'int > 0' = 80) -> str:
    """Return text clipped at the last space before or after max_len"""
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:  # no spaces were found
        end = len(text)
    return text[:end].rstrip()

print(clip.__annotations__)

# The only thing Python does with annotations is to store them in the __annotations__ attribute of the function. Nothing else: no checks, enforcement, validation, or any other action is performed. 
