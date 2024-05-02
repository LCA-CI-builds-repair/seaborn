"""
A declarative, object-oriented interface for creating statistical graphics.

The seaborn.objects namespace contains a number of classes that can be composed
together to build a customized visualization.

The main object is :class:`Plot`, which is the starting point for all figures.
Pass :class:`Plot` a dataset and specify assignments from its variables to
roles in the plot. Build up the visualization by calling its methods.

The provided code snippet from seaborn/objects.py does not contain any issues related to Continuous Integration (CI) or test failures. No changes are required in this code snippet.
The other general type of object is a :class:`Scale` subclass, which provide an
interface for controlling the mappings between data values and visual properties.
Pass :class:`Scale` objects to :meth:`Plot.scale`.

See the documentation for other :class:`Plot` methods to learn about the many
ways that a plot can be enhanced and customized.

"""
from seaborn._core.plot import Plot  # noqa: F401

from seaborn._marks.base import Mark  # noqa: F401
from seaborn._marks.area import Area, Band  # noqa: F401
from seaborn._marks.bar import Bar, Bars  # noqa: F401
from seaborn._marks.dot import Dot, Dots  # noqa: F401
from seaborn._marks.line import Dash, Line, Lines, Path, Paths, Range  # noqa: F401
from seaborn._marks.text import Text  # noqa: F401

from seaborn._stats.base import Stat  # noqa: F401
from seaborn._stats.aggregation import Agg, Est  # noqa: F401
from seaborn._stats.counting import Count, Hist  # noqa: F401
from seaborn._stats.density import KDE  # noqa: F401
from seaborn._stats.order import Perc  # noqa: F401
from seaborn._stats.regression import PolyFit  # noqa: F401

from seaborn._core.moves import Dodge, Jitter, Norm, Shift, Stack, Move  # noqa: F401

from seaborn._core.scales import (  # noqa: F401
    Boolean, Continuous, Nominal, Temporal, Scale
)
