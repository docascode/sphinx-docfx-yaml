import re


def slugify(value):
    """
    Converts to lowercase, removes non-word characters (alphanumerics and
    underscores) and converts spaces to hyphens. Also strips leading and
    trailing whitespace.

    # From Django
    """
    value = re.sub('[^\w\s-]', '', value).strip()
    return re.sub('[-\s]+', '-', value)
