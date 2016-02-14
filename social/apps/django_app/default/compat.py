from django import VERSION


if VERSION >= (1, 8):
    from itertools import chain

    def get_all_field_names_from_options(options):
        names = list(set(chain.from_iterable(
                (field.name, field.attname) if hasattr(field, 'attname') else (field.name,)
                for field in options.get_fields()
        )))
        return names
else:
    def get_all_field_names_from_options(options):
        return options.get_all_field_names()
