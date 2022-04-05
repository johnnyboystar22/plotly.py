from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Circle(_BaseLayoutHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = "layout.mapbox.layer"
    _path_str = "layout.mapbox.layer.circle"
    _valid_props = {"radius"}

    # radius
    # ------
    @property
    def radius(self):
        """
        Sets the circle radius (mapbox.layer.paint.circle-radius). Has
        an effect only when `type` is set to "circle".

        The 'radius' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["radius"]

    @radius.setter
    def radius(self, val):
        self["radius"] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        radius
            Sets the circle radius (mapbox.layer.paint.circle-
            radius). Has an effect only when `type` is set to
            "circle".
        """

    def __init__(self, arg=None, radius=None, **kwargs):
        """
        Construct a new Circle object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.mapbox.layer.Circle`
        radius
            Sets the circle radius (mapbox.layer.paint.circle-
            radius). Has an effect only when `type` is set to
            "circle".

        Returns
        -------
        Circle
        """
        super(Circle, self).__init__("circle")

        if "_parent" in kwargs:
            self._parent = kwargs["_parent"]
            return

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.layout.mapbox.layer.Circle 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.layout.mapbox.layer.Circle`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("radius", None)
        _v = radius if radius is not None else _v
        if _v is not None:
            self["radius"] = _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
