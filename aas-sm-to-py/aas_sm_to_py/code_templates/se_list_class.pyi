{% extends "se_col_class.pyi" %}

{%- block after_init -%}

def _check_constraints(self, new, existing) -> None:
    # Since the id_short contains randomness, unset it temporarily for pretty and predictable error messages.
    # This also prevents the random id_short from remaining set in case a constraint violation is encountered.
    saved_id_short = new.id_short
    new.id_short = None

    # We relax constraint AASd-108here: It is allowed to add subclasses of the specified in type_value_list_element
    if not isinstance(new, self.type_value_list_element):
        raise base.AASConstraintViolation(108, "All first level elements must be of the type specified in "
                                               f"type_value_list_element={self.type_value_list_element.__name__}, "
                                               f"got {new!r}")

    if self.semantic_id_list_element is not None and new.semantic_id is not None \
            and new.semantic_id != self.semantic_id_list_element:
        # Constraint AASd-115 specifies that if the semantic_id of an item is not specified
        # but semantic_id_list_element is, the semantic_id of the new is assumed to be identical.
        # Not really a constraint...
        # TODO: maybe set the semantic_id of new to semantic_id_list_element if it is None
        raise base.AASConstraintViolation(107, f"If semantic_id_list_element={self.semantic_id_list_element!r} "
                                               "is specified all first level children must have the same "
                                               f"semantic_id, got {new!r} with semantic_id={new.semantic_id!r}")

    # If we got here we know that `new` is an instance of type_value_list_element and that type_value_list_element
    # is either Property or Range. Thus, `new` must have the value_type property.
    # Furthermore, value_type_list_element cannot be None, as this is already checked in __init__().
    if isinstance(self.type_value_list_element, Property) or isinstance(self.type_value_list_element, Range) \
            and not isinstance(new.value_type, self.value_type_list_element):  # type: ignore
        raise base.AASConstraintViolation(109, "All first level elements must have the value_type "  # type: ignore
                                               "specified by value_type_list_element="
                                               f"{self.value_type_list_element.__name__}, got "  # type: ignore
                                               f"{new!r} with value_type={new.value_type.__name__}")  # type: ignore

    # If semantic_id_list_element is not None that would already enforce the semantic_id for all first level
    # elements. Thus, we only need to perform this check if semantic_id_list_element is None.
    if new.semantic_id is not None and self.semantic_id_list_element is None:
        for item in existing:
            if item.semantic_id is not None and new.semantic_id != item.semantic_id:
                raise base.AASConstraintViolation(114, f"Element to be added {new!r} has semantic_id "
                                                       f"{new.semantic_id!r}, while already contained element "
                                                       f"{item!r} has semantic_id {item.semantic_id!r}, which "
                                                       "aren't equal.")

    # Re-assign id_short
    new.id_short = saved_id_short
{% endblock %}