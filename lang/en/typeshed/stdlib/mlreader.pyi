from typing import Tuple

def read_class_names() -> Tuple[str, ...]:
    """Return a tuple of the class names stored in the text file.

    Example: ``mlreader.read_class_names()``

    The class names in the text file are the ones set when the class data was recorded in ML-Machine.

    :return: The class names from the text file as a tuple, in the order they were recorded in.
    """
    ...