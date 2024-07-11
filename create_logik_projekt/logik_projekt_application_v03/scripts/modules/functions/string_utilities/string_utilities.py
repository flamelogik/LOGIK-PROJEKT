import re

def to_snake_case(s):
    """Convert CamelCase to snake_case."""
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()

def to_camel_case(s):
    """Convert snake_case to CamelCase."""
    return ''.join(word.title() if i != 0 else word for i, word in enumerate(s.split('_')))

def validate_string(s, pattern):
    """Validate string against a regex pattern."""
    return re.match(pattern, s) is not None


def string_clean(string):

    '''
    Clean string: allow only lower case letters, numbers, and underscores.

        * Convert to lowercase

        * Keep only lowercase letters, numbers, underscores, and replace
          other characters with underscores

        * Replace whitespace characters with underscores

        * Replace consecutive underscores with single underscore

        * Remove leading and trailing underscores

    '''

    string = string.lower()

    string = ''.join(
        character 
        if character.islower() 
        or character.isdigit() 
        or character == '_' 
        or character.isspace() 
        else '_' for character in string)

    string = string.replace(' ', '_')

    string = '_'.join(filter(None, string.split('_')))

    string = string.strip('_')

    return string
