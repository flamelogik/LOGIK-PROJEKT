# def string_clean(s):
#     """Clean string: allow only lower case letters, numbers, and underscores."""
#     s = s.lower()  # Convert to lowercase
#     s = ''.join(c if c.islower() or c.isdigit() or c == '_' else '' for c in s)  # Keep only lowercase letters, numbers, and underscores
#     s = '_'.join(filter(None, s.split('_')))  # Replace consecutive underscores with single underscore
#     s = s.strip('_')  # Remove leading and trailing underscores
#     return s

def string_clean(s):
    """Clean string: allow only lower case letters, numbers, and underscores."""
    s = s.lower()  # Convert to lowercase
    s = ''.join(c if c.islower() or c.isdigit() or c == '_' or c.isspace() else '_' for c in s)  # Keep only lowercase letters, numbers, underscores, and replace other characters with underscores
    s = s.replace(' ', '_')  # Replace whitespace characters with underscores
    s = '_'.join(filter(None, s.split('_')))  # Replace consecutive underscores with single underscore
    s = s.strip('_')  # Remove leading and trailing underscores
    return s
