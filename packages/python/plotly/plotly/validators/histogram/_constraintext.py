import _plotly_utils.basevalidators


class ConstraintextValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="constraintext", parent_name="histogram", **kwargs):
        super(ConstraintextValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop("values", ["inside", "outside", "both", "none"]),
            **kwargs,
        )
