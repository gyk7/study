from _typeshed import Incomplete

from influxdb_client.domain.view_properties import ViewProperties

class CheckViewProperties(ViewProperties):
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        adaptive_zoom_hide: bool | None = None,
        type: Incomplete | None = None,
        shape: Incomplete | None = None,
        check_id: Incomplete | None = None,
        check: Incomplete | None = None,
        queries: Incomplete | None = None,
        colors: Incomplete | None = None,
        legend_colorize_rows: Incomplete | None = None,
        legend_hide: Incomplete | None = None,
        legend_opacity: Incomplete | None = None,
        legend_orientation_threshold: Incomplete | None = None,
    ) -> None: ...
    adaptive_zoom_hide: bool | None
    @property
    def type(self): ...
    @type.setter
    def type(self, type) -> None: ...
    @property
    def shape(self): ...
    @shape.setter
    def shape(self, shape) -> None: ...
    @property
    def check_id(self): ...
    @check_id.setter
    def check_id(self, check_id) -> None: ...
    @property
    def check(self): ...
    @check.setter
    def check(self, check) -> None: ...
    @property
    def queries(self): ...
    @queries.setter
    def queries(self, queries) -> None: ...
    @property
    def colors(self): ...
    @colors.setter
    def colors(self, colors) -> None: ...
    @property
    def legend_colorize_rows(self): ...
    @legend_colorize_rows.setter
    def legend_colorize_rows(self, legend_colorize_rows) -> None: ...
    @property
    def legend_hide(self): ...
    @legend_hide.setter
    def legend_hide(self, legend_hide) -> None: ...
    @property
    def legend_opacity(self): ...
    @legend_opacity.setter
    def legend_opacity(self, legend_opacity) -> None: ...
    @property
    def legend_orientation_threshold(self): ...
    @legend_orientation_threshold.setter
    def legend_orientation_threshold(self, legend_orientation_threshold) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
