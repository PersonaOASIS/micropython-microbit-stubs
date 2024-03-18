"""Use the inported machine learning model.
"""

from typing import Tuple

def get_class_names() -> Tuple[str, ...]:
    """Return a tuple of the class names of the current model.

    Example: ``ml.get_class_names()``

    The class names are the ones set when the class data was recorded in ML-Machine.

    :return: The class names as a tuple, in the order they were recorded in.
    """
    ...

def current_action() -> str:
    """Get the name of the currently recognised action.

    Example: `` ml.current_action()``

    The action names depend on the labels set when the class data was recorded in ML-Machine. Class names are always represented as strings.

    :return: The current recognised action.
    """
    ...

def is_action(name: str) -> bool:
    """Check if the named class is currently recognised.

    Example: `` ml.is_action('still')``

    The action names depend on the labels set when the class data was recorded in ML-Machine. Class names are always represented as strings.

    :param name: The action name.
    :return: ``True `` if the action is being recognised, ``False`` otherwise.
    """
    ...   

def was_action(name: str) -> bool:
    """Check if the named class was recognised since the last call.

    Example: `` ml.is_action('still')``

    The action names depend on the labels set when the class data was recorded in ML-Machine. Class names are always represented as strings.

    :param name: The action name.
    :return: ``True `` if the action was recognised since the last call, ``False`` otherwise.
    """
    ... 