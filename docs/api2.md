# Summary of API for dtcc

## Modules

* `building`
* `city`
* `dtcc_pb2`
* `geometry`
* `grid`
* `gridfields`
* `landuse`
* `meshes`
* `meshfields`
* `model`
* `pointcloud`
* `proto`
* `raster`
* `roadnetwork`
* `utils`

## Classes

### Bounds
Bounds(xmin: float = 0.0, ymin: float = 0.0, xmax: float = 0.0, ymax: float = 0.0)
### Building
A base representation of a singele building.

    Attributes:
    uuid (str): The UUID of the building.
    footprint (Polygon): The polygon representing the footprint of the building.
    height (float): The height of the building.
    ground_level (float): The ground level of base of the building.
    roofpoints (PointCloud): The point cloud representing the roof points of the building.
    crs (str): The coordinate reference system of the building.
    error (int): Encoding the errors the occured when generating 3D represention of building.
    properties (dict): Additional properties of the building.

    
### City
A City is the top-level container class for city models
### Georef
Georef(crs: str = '', epsg: int = 0, x0: float = 0.0, y0: float = 0.0)
### Grid
Grid(bounds: dtcc_model.geometry.Bounds = <factory>, width: int = 0, height: int = 0, xstep: float = 0.0, ystep: float = 0.0)
### GridField
GridField(grid: dtcc_model.grid.Grid = <factory>, values: numpy.ndarray = <factory>)
### GridVectorField
GridVectorField(grid: dtcc_model.grid.Grid = <factory>, values: numpy.ndarray = <factory>)
### Landuse
A polygon of a singele landuse area.:
    available landuse types are:
    WATER, GRASS, FOREST, FARMLAND, URBAN, INDUSTRIAL, MILITARY, ROAD, RAIL
### Mesh
Mesh(vertices: numpy.ndarray = <factory>, vertex_colors: numpy.ndarray = <factory>, normals: numpy.ndarray = <factory>, faces: numpy.ndarray = <factory>, face_colors: numpy.ndarray = <factory>, markers: numpy.ndarray = <factory>)
### MeshField
MeshField(mesh: dtcc_model.meshes.Mesh = <factory>, values: numpy.ndarray = <factory>)
### MeshVectorField
MeshVectorField(mesh: dtcc_model.meshes.Mesh = <factory>, values: numpy.ndarray = <factory>)
### PointCloud
A point cloud is a set of points with associated attributes.
    Attributes:
      bounds (Bounds): The bounds of the point cloud.
      georef (Georef): The georeference of the point cloud.
      points (np.ndarray): The points of the point cloud as (n,3) dimensional numpy array.

      The following attributes are as defined in the las specification:
      classification (np.ndarray): The classification of the points as (n,) dimensional numpy array.
      intensity (np.ndarray): The intensity of the points as (n,) dimensional numpy array.
      return_number (np.ndarray): The return number of the points as (n,) dimensional numpy array.
      num_returns (np.ndarray): The number of returns of the points as (n,) dimensional numpy array.


    
### Raster
A georeferenced n-dimensional raster of values.
    data is a numpy array of shape (height, width, channels) or (height, width)
    if channels is 1.
    
### RoadNetwork
RoadNetwork(roads: List[dtcc_model.roadnetwork.Road] = <factory>, vertices: numpy.ndarray = <factory>, georef: dtcc_model.geometry.Georef = <factory>)
### RoadType
None
### VolumeMesh
VolumeMesh(vertices: numpy.ndarray = <factory>, cells: numpy.ndarray = <factory>, markers: numpy.ndarray = <factory>)
### VolumeMeshField
VolumeMeshField(mesh: dtcc_model.meshes.Mesh = <factory>, values: numpy.ndarray = <factory>)
### VolumeMeshVectorField
VolumeMeshVectorField(mesh: dtcc_model.meshes.Mesh = <factory>, values: numpy.ndarray = <factory>)

## Functions:


# Summary of API for dtcc.building

## Modules

* `np`
* `proto`

## Classes

### Any
Special type indicating an unconstrained type.

    - Any is compatible with every type.
    - Any assumed to have all methods.
    - All values assumed to be instances of Any.

    Note that all the above statements are true from the point of view of
    static type checkers. At runtime, Any should not be used with instance
    checks.
    
### Building
A base representation of a singele building.

    Attributes:
    uuid (str): The UUID of the building.
    footprint (Polygon): The polygon representing the footprint of the building.
    height (float): The height of the building.
    ground_level (float): The ground level of base of the building.
    roofpoints (PointCloud): The point cloud representing the roof points of the building.
    crs (str): The coordinate reference system of the building.
    error (int): Encoding the errors the occured when generating 3D represention of building.
    properties (dict): Additional properties of the building.

    
### DTCCModel
Base class for all DTCC models. Must implement to_proto and from_proto
    methods that converts to and from the protobuf representation.
    
### PointCloud
A point cloud is a set of points with associated attributes.
    Attributes:
      bounds (Bounds): The bounds of the point cloud.
      georef (Georef): The georeference of the point cloud.
      points (np.ndarray): The points of the point cloud as (n,3) dimensional numpy array.

      The following attributes are as defined in the las specification:
      classification (np.ndarray): The classification of the points as (n,) dimensional numpy array.
      intensity (np.ndarray): The intensity of the points as (n,) dimensional numpy array.
      return_number (np.ndarray): The return number of the points as (n,) dimensional numpy array.
      num_returns (np.ndarray): The number of returns of the points as (n,) dimensional numpy array.


    
### Polygon

    A geometry type representing an area that is enclosed by a linear ring.

    A polygon is a two-dimensional feature and has a non-zero area. It may
    have one or more negative-space "holes" which are also bounded by linear
    rings. If any rings cross each other, the feature is invalid and
    operations on it may fail.

    Parameters
    ----------
    shell : sequence
        A sequence of (x, y [,z]) numeric coordinate pairs or triples, or
        an array-like with shape (N, 2) or (N, 3).
        Also can be a sequence of Point objects.
    holes : sequence
        A sequence of objects which satisfy the same requirements as the
        shell parameters above

    Attributes
    ----------
    exterior : LinearRing
        The ring which bounds the positive space of the polygon.
    interiors : sequence
        A sequence of rings which bound all existing holes.

    Examples
    --------
    Create a square polygon with no holes

    >>> coords = ((0., 0.), (0., 1.), (1., 1.), (1., 0.), (0., 0.))
    >>> polygon = Polygon(coords)
    >>> polygon.area
    1.0
    

## Functions:

### dataclass()
Add dunder methods based on the fields defined in the class.

    Examines PEP 526 __annotations__ to determine fields.

    If init is true, an __init__() method is added to the class. If repr
    is true, a __repr__() method is added. If order is true, rich
    comparison dunder methods are added. If unsafe_hash is true, a
    __hash__() method is added. If frozen is true, fields may not be
    assigned to after instance creation. If match_args is true, the
    __match_args__ tuple is added. If kw_only is true, then by default
    all fields are keyword-only. If slots is true, a new class with a
    __slots__ attribute is returned.
    
### field()
Return an object to identify dataclass fields.

    default is the default value of the field.  default_factory is a
    0-argument function called to initialize a field's value.  If init
    is true, the field will be a parameter to the class's __init__()
    function.  If repr is true, the field will be included in the
    object's repr().  If hash is true, the field will be included in the
    object's hash().  If compare is true, the field will be used in
    comparison functions.  metadata, if specified, must be a mapping
    which is stored but not otherwise examined by dataclass.  If kw_only
    is true, the field will become a keyword-only parameter to
    __init__().

    It is an error to specify both default and default_factory.
    
### pb_polygon_from_shapely()
None
### pb_polygon_to_shapely()
None

# Summary of API for dtcc.city

## Modules

* `np`
* `proto`

## Classes

### Bounds
Bounds(xmin: float = 0.0, ymin: float = 0.0, xmax: float = 0.0, ymax: float = 0.0)
### Building
A base representation of a singele building.

    Attributes:
    uuid (str): The UUID of the building.
    footprint (Polygon): The polygon representing the footprint of the building.
    height (float): The height of the building.
    ground_level (float): The ground level of base of the building.
    roofpoints (PointCloud): The point cloud representing the roof points of the building.
    crs (str): The coordinate reference system of the building.
    error (int): Encoding the errors the occured when generating 3D represention of building.
    properties (dict): Additional properties of the building.

    
### City
A City is the top-level container class for city models
### DTCCModel
Base class for all DTCC models. Must implement to_proto and from_proto
    methods that converts to and from the protobuf representation.
    
### Georef
Georef(crs: str = '', epsg: int = 0, x0: float = 0.0, y0: float = 0.0)
### Landuse
A polygon of a singele landuse area.:
    available landuse types are:
    WATER, GRASS, FOREST, FARMLAND, URBAN, INDUSTRIAL, MILITARY, ROAD, RAIL
### Raster
A georeferenced n-dimensional raster of values.
    data is a numpy array of shape (height, width, channels) or (height, width)
    if channels is 1.
    
### RoadNetwork
RoadNetwork(roads: List[dtcc_model.roadnetwork.Road] = <factory>, vertices: numpy.ndarray = <factory>, georef: dtcc_model.geometry.Georef = <factory>)

## Functions:

### dataclass()
Add dunder methods based on the fields defined in the class.

    Examines PEP 526 __annotations__ to determine fields.

    If init is true, an __init__() method is added to the class. If repr
    is true, a __repr__() method is added. If order is true, rich
    comparison dunder methods are added. If unsafe_hash is true, a
    __hash__() method is added. If frozen is true, fields may not be
    assigned to after instance creation. If match_args is true, the
    __match_args__ tuple is added. If kw_only is true, then by default
    all fields are keyword-only. If slots is true, a new class with a
    __slots__ attribute is returned.
    
### field()
Return an object to identify dataclass fields.

    default is the default value of the field.  default_factory is a
    0-argument function called to initialize a field's value.  If init
    is true, the field will be a parameter to the class's __init__()
    function.  If repr is true, the field will be included in the
    object's repr().  If hash is true, the field will be included in the
    object's hash().  If compare is true, the field will be used in
    comparison functions.  metadata, if specified, must be a mapping
    which is stored but not otherwise examined by dataclass.  If kw_only
    is true, the field will become a keyword-only parameter to
    __init__().

    It is an error to specify both default and default_factory.
    
### getmembers()
Return all members of an object as (name, value) pairs sorted by name.
    Optionally, only return members that satisfy a given predicate.
### isfunction()
Return true if the object is a user-defined function.

    Function objects provide these attributes:
        __doc__         documentation string
        __name__        name with which this function was defined
        __code__        code object containing compiled function bytecode
        __defaults__    tuple of any default values for arguments
        __globals__     global namespace in which this function was defined
        __annotations__ dict of parameter annotations
        __kwdefaults__  dict of keyword only parameters with defaults
### ismethod()
Return true if the object is an instance method.

    Instance method objects provide these attributes:
        __doc__         documentation string
        __name__        name with which this method was defined
        __func__        function object containing implementation of method
        __self__        instance to which this method is bound
### replace()
Return a new object replacing specified fields with new values.

    This is especially useful for frozen classes.  Example usage::

      @dataclass(frozen=True)
      class C:
          x: int
          y: int

      c = C(1, 2)
      c1 = replace(c, x=3)
      assert c1.x == 3 and c1.y == 2
    

# Summary of API for dtcc.dtcc_pb2

## Modules

* `_descriptor`
* `_message`
* `_reflection`
* `_symbol_database`

## Classes

### AffineTransform
None
### Bounds
None
### Building
None
### City
None
### Georef
None
### Grid
None
### GridField
None
### GridVectorField
None
### LandUse
None
### LineString
None
### LineString3D
None
### LinearRing
None
### Mesh
None
### MeshField
None
### MeshVectorField
None
### MultiPoint
None
### MultiPoint3D
None
### MultiPolygon
None
### PointCloud
None
### Polygon
None
### Raster
None
### Road
None
### RoadNetwork
None
### Vector2D
None
### Vector3D
None
### VolumeMesh
None
### VolumeMeshField
None
### VolumeMeshVectorField
None

## Functions:


# Summary of API for dtcc.geometry

## Modules

* `np`
* `proto`

## Classes

### Bounds
Bounds(xmin: float = 0.0, ymin: float = 0.0, xmax: float = 0.0, ymax: float = 0.0)
### DTCCModel
Base class for all DTCC models. Must implement to_proto and from_proto
    methods that converts to and from the protobuf representation.
    
### Georef
Georef(crs: str = '', epsg: int = 0, x0: float = 0.0, y0: float = 0.0)

## Functions:

### dataclass()
Add dunder methods based on the fields defined in the class.

    Examines PEP 526 __annotations__ to determine fields.

    If init is true, an __init__() method is added to the class. If repr
    is true, a __repr__() method is added. If order is true, rich
    comparison dunder methods are added. If unsafe_hash is true, a
    __hash__() method is added. If frozen is true, fields may not be
    assigned to after instance creation. If match_args is true, the
    __match_args__ tuple is added. If kw_only is true, then by default
    all fields are keyword-only. If slots is true, a new class with a
    __slots__ attribute is returned.
    
### getmembers()
Return all members of an object as (name, value) pairs sorted by name.
    Optionally, only return members that satisfy a given predicate.
### isfunction()
Return true if the object is a user-defined function.

    Function objects provide these attributes:
        __doc__         documentation string
        __name__        name with which this function was defined
        __code__        code object containing compiled function bytecode
        __defaults__    tuple of any default values for arguments
        __globals__     global namespace in which this function was defined
        __annotations__ dict of parameter annotations
        __kwdefaults__  dict of keyword only parameters with defaults
### ismethod()
Return true if the object is an instance method.

    Instance method objects provide these attributes:
        __doc__         documentation string
        __name__        name with which this method was defined
        __func__        function object containing implementation of method
        __self__        instance to which this method is bound

# Summary of API for dtcc.grid

## Modules

* `np`
* `proto`

## Classes

### Bounds
Bounds(xmin: float = 0.0, ymin: float = 0.0, xmax: float = 0.0, ymax: float = 0.0)
### DTCCModel
Base class for all DTCC models. Must implement to_proto and from_proto
    methods that converts to and from the protobuf representation.
    
### Grid
Grid(bounds: dtcc_model.geometry.Bounds = <factory>, width: int = 0, height: int = 0, xstep: float = 0.0, ystep: float = 0.0)

## Functions:

### dataclass()
Add dunder methods based on the fields defined in the class.

    Examines PEP 526 __annotations__ to determine fields.

    If init is true, an __init__() method is added to the class. If repr
    is true, a __repr__() method is added. If order is true, rich
    comparison dunder methods are added. If unsafe_hash is true, a
    __hash__() method is added. If frozen is true, fields may not be
    assigned to after instance creation. If match_args is true, the
    __match_args__ tuple is added. If kw_only is true, then by default
    all fields are keyword-only. If slots is true, a new class with a
    __slots__ attribute is returned.
    
### field()
Return an object to identify dataclass fields.

    default is the default value of the field.  default_factory is a
    0-argument function called to initialize a field's value.  If init
    is true, the field will be a parameter to the class's __init__()
    function.  If repr is true, the field will be included in the
    object's repr().  If hash is true, the field will be included in the
    object's hash().  If compare is true, the field will be used in
    comparison functions.  metadata, if specified, must be a mapping
    which is stored but not otherwise examined by dataclass.  If kw_only
    is true, the field will become a keyword-only parameter to
    __init__().

    It is an error to specify both default and default_factory.
    
### getmembers()
Return all members of an object as (name, value) pairs sorted by name.
    Optionally, only return members that satisfy a given predicate.
### isfunction()
Return true if the object is a user-defined function.

    Function objects provide these attributes:
        __doc__         documentation string
        __name__        name with which this function was defined
        __code__        code object containing compiled function bytecode
        __defaults__    tuple of any default values for arguments
        __globals__     global namespace in which this function was defined
        __annotations__ dict of parameter annotations
        __kwdefaults__  dict of keyword only parameters with defaults
### ismethod()
Return true if the object is an instance method.

    Instance method objects provide these attributes:
        __doc__         documentation string
        __name__        name with which this method was defined
        __func__        function object containing implementation of method
        __self__        instance to which this method is bound

# Summary of API for dtcc.gridfields

## Modules

* `np`
* `proto`

## Classes

### DTCCModel
Base class for all DTCC models. Must implement to_proto and from_proto
    methods that converts to and from the protobuf representation.
    
### Grid
Grid(bounds: dtcc_model.geometry.Bounds = <factory>, width: int = 0, height: int = 0, xstep: float = 0.0, ystep: float = 0.0)
### GridField
GridField(grid: dtcc_model.grid.Grid = <factory>, values: numpy.ndarray = <factory>)
### GridVectorField
GridVectorField(grid: dtcc_model.grid.Grid = <factory>, values: numpy.ndarray = <factory>)

## Functions:

### dataclass()
Add dunder methods based on the fields defined in the class.

    Examines PEP 526 __annotations__ to determine fields.

    If init is true, an __init__() method is added to the class. If repr
    is true, a __repr__() method is added. If order is true, rich
    comparison dunder methods are added. If unsafe_hash is true, a
    __hash__() method is added. If frozen is true, fields may not be
    assigned to after instance creation. If match_args is true, the
    __match_args__ tuple is added. If kw_only is true, then by default
    all fields are keyword-only. If slots is true, a new class with a
    __slots__ attribute is returned.
    
### field()
Return an object to identify dataclass fields.

    default is the default value of the field.  default_factory is a
    0-argument function called to initialize a field's value.  If init
    is true, the field will be a parameter to the class's __init__()
    function.  If repr is true, the field will be included in the
    object's repr().  If hash is true, the field will be included in the
    object's hash().  If compare is true, the field will be used in
    comparison functions.  metadata, if specified, must be a mapping
    which is stored but not otherwise examined by dataclass.  If kw_only
    is true, the field will become a keyword-only parameter to
    __init__().

    It is an error to specify both default and default_factory.
    
### getmembers()
Return all members of an object as (name, value) pairs sorted by name.
    Optionally, only return members that satisfy a given predicate.
### isfunction()
Return true if the object is a user-defined function.

    Function objects provide these attributes:
        __doc__         documentation string
        __name__        name with which this function was defined
        __code__        code object containing compiled function bytecode
        __defaults__    tuple of any default values for arguments
        __globals__     global namespace in which this function was defined
        __annotations__ dict of parameter annotations
        __kwdefaults__  dict of keyword only parameters with defaults
### ismethod()
Return true if the object is an instance method.

    Instance method objects provide these attributes:
        __doc__         documentation string
        __name__        name with which this method was defined
        __func__        function object containing implementation of method
        __self__        instance to which this method is bound

# Summary of API for dtcc.landuse

## Modules

* `proto`

## Classes

### Any
Special type indicating an unconstrained type.

    - Any is compatible with every type.
    - Any assumed to have all methods.
    - All values assumed to be instances of Any.

    Note that all the above statements are true from the point of view of
    static type checkers. At runtime, Any should not be used with instance
    checks.
    
### DTCCModel
Base class for all DTCC models. Must implement to_proto and from_proto
    methods that converts to and from the protobuf representation.
    
### Enum

    Create a collection of name/value pairs.

    Example enumeration:

    >>> class Color(Enum):
    ...     RED = 1
    ...     BLUE = 2
    ...     GREEN = 3

    Access them by:

    - attribute access::

    >>> Color.RED
    <Color.RED: 1>

    - value lookup:

    >>> Color(1)
    <Color.RED: 1>

    - name lookup:

    >>> Color['RED']
    <Color.RED: 1>

    Enumerations can be iterated over, and know how many members they have:

    >>> len(Color)
    3

    >>> list(Color)
    [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]

    Methods can be added to enumerations, and members can have their own
    attributes -- see the documentation for details.
    
### Landuse
A polygon of a singele landuse area.:
    available landuse types are:
    WATER, GRASS, FOREST, FARMLAND, URBAN, INDUSTRIAL, MILITARY, ROAD, RAIL
### LanduseClasses
None
### Polygon

    A geometry type representing an area that is enclosed by a linear ring.

    A polygon is a two-dimensional feature and has a non-zero area. It may
    have one or more negative-space "holes" which are also bounded by linear
    rings. If any rings cross each other, the feature is invalid and
    operations on it may fail.

    Parameters
    ----------
    shell : sequence
        A sequence of (x, y [,z]) numeric coordinate pairs or triples, or
        an array-like with shape (N, 2) or (N, 3).
        Also can be a sequence of Point objects.
    holes : sequence
        A sequence of objects which satisfy the same requirements as the
        shell parameters above

    Attributes
    ----------
    exterior : LinearRing
        The ring which bounds the positive space of the polygon.
    interiors : sequence
        A sequence of rings which bound all existing holes.

    Examples
    --------
    Create a square polygon with no holes

    >>> coords = ((0., 0.), (0., 1.), (1., 1.), (1., 0.), (0., 0.))
    >>> polygon = Polygon(coords)
    >>> polygon.area
    1.0
    
### auto

    Instances are replaced with an appropriate value in Enum class suites.
    

## Functions:

### dataclass()
Add dunder methods based on the fields defined in the class.

    Examines PEP 526 __annotations__ to determine fields.

    If init is true, an __init__() method is added to the class. If repr
    is true, a __repr__() method is added. If order is true, rich
    comparison dunder methods are added. If unsafe_hash is true, a
    __hash__() method is added. If frozen is true, fields may not be
    assigned to after instance creation. If match_args is true, the
    __match_args__ tuple is added. If kw_only is true, then by default
    all fields are keyword-only. If slots is true, a new class with a
    __slots__ attribute is returned.
    
### field()
Return an object to identify dataclass fields.

    default is the default value of the field.  default_factory is a
    0-argument function called to initialize a field's value.  If init
    is true, the field will be a parameter to the class's __init__()
    function.  If repr is true, the field will be included in the
    object's repr().  If hash is true, the field will be included in the
    object's hash().  If compare is true, the field will be used in
    comparison functions.  metadata, if specified, must be a mapping
    which is stored but not otherwise examined by dataclass.  If kw_only
    is true, the field will become a keyword-only parameter to
    __init__().

    It is an error to specify both default and default_factory.
    
### pb_polygon_from_shapely()
None
### pb_polygon_to_shapely()
None

# Summary of API for dtcc.meshes

## Modules

* `np`
* `proto`

## Classes

### DTCCModel
Base class for all DTCC models. Must implement to_proto and from_proto
    methods that converts to and from the protobuf representation.
    
### Mesh
Mesh(vertices: numpy.ndarray = <factory>, vertex_colors: numpy.ndarray = <factory>, normals: numpy.ndarray = <factory>, faces: numpy.ndarray = <factory>, face_colors: numpy.ndarray = <factory>, markers: numpy.ndarray = <factory>)
### VolumeMesh
VolumeMesh(vertices: numpy.ndarray = <factory>, cells: numpy.ndarray = <factory>, markers: numpy.ndarray = <factory>)

## Functions:

### dataclass()
Add dunder methods based on the fields defined in the class.

    Examines PEP 526 __annotations__ to determine fields.

    If init is true, an __init__() method is added to the class. If repr
    is true, a __repr__() method is added. If order is true, rich
    comparison dunder methods are added. If unsafe_hash is true, a
    __hash__() method is added. If frozen is true, fields may not be
    assigned to after instance creation. If match_args is true, the
    __match_args__ tuple is added. If kw_only is true, then by default
    all fields are keyword-only. If slots is true, a new class with a
    __slots__ attribute is returned.
    
### field()
Return an object to identify dataclass fields.

    default is the default value of the field.  default_factory is a
    0-argument function called to initialize a field's value.  If init
    is true, the field will be a parameter to the class's __init__()
    function.  If repr is true, the field will be included in the
    object's repr().  If hash is true, the field will be included in the
    object's hash().  If compare is true, the field will be used in
    comparison functions.  metadata, if specified, must be a mapping
    which is stored but not otherwise examined by dataclass.  If kw_only
    is true, the field will become a keyword-only parameter to
    __init__().

    It is an error to specify both default and default_factory.
    
### getmembers()
Return all members of an object as (name, value) pairs sorted by name.
    Optionally, only return members that satisfy a given predicate.
### isfunction()
Return true if the object is a user-defined function.

    Function objects provide these attributes:
        __doc__         documentation string
        __name__        name with which this function was defined
        __code__        code object containing compiled function bytecode
        __defaults__    tuple of any default values for arguments
        __globals__     global namespace in which this function was defined
        __annotations__ dict of parameter annotations
        __kwdefaults__  dict of keyword only parameters with defaults
### ismethod()
Return true if the object is an instance method.

    Instance method objects provide these attributes:
        __doc__         documentation string
        __name__        name with which this method was defined
        __func__        function object containing implementation of method
        __self__        instance to which this method is bound

# Summary of API for dtcc.meshfields

## Modules

* `np`
* `proto`

## Classes

### DTCCModel
Base class for all DTCC models. Must implement to_proto and from_proto
    methods that converts to and from the protobuf representation.
    
### Mesh
Mesh(vertices: numpy.ndarray = <factory>, vertex_colors: numpy.ndarray = <factory>, normals: numpy.ndarray = <factory>, faces: numpy.ndarray = <factory>, face_colors: numpy.ndarray = <factory>, markers: numpy.ndarray = <factory>)
### MeshField
MeshField(mesh: dtcc_model.meshes.Mesh = <factory>, values: numpy.ndarray = <factory>)
### MeshVectorField
MeshVectorField(mesh: dtcc_model.meshes.Mesh = <factory>, values: numpy.ndarray = <factory>)
### VolumeMesh
VolumeMesh(vertices: numpy.ndarray = <factory>, cells: numpy.ndarray = <factory>, markers: numpy.ndarray = <factory>)
### VolumeMeshField
VolumeMeshField(mesh: dtcc_model.meshes.Mesh = <factory>, values: numpy.ndarray = <factory>)
### VolumeMeshVectorField
VolumeMeshVectorField(mesh: dtcc_model.meshes.Mesh = <factory>, values: numpy.ndarray = <factory>)

## Functions:

### dataclass()
Add dunder methods based on the fields defined in the class.

    Examines PEP 526 __annotations__ to determine fields.

    If init is true, an __init__() method is added to the class. If repr
    is true, a __repr__() method is added. If order is true, rich
    comparison dunder methods are added. If unsafe_hash is true, a
    __hash__() method is added. If frozen is true, fields may not be
    assigned to after instance creation. If match_args is true, the
    __match_args__ tuple is added. If kw_only is true, then by default
    all fields are keyword-only. If slots is true, a new class with a
    __slots__ attribute is returned.
    
### field()
Return an object to identify dataclass fields.

    default is the default value of the field.  default_factory is a
    0-argument function called to initialize a field's value.  If init
    is true, the field will be a parameter to the class's __init__()
    function.  If repr is true, the field will be included in the
    object's repr().  If hash is true, the field will be included in the
    object's hash().  If compare is true, the field will be used in
    comparison functions.  metadata, if specified, must be a mapping
    which is stored but not otherwise examined by dataclass.  If kw_only
    is true, the field will become a keyword-only parameter to
    __init__().

    It is an error to specify both default and default_factory.
    
### getmembers()
Return all members of an object as (name, value) pairs sorted by name.
    Optionally, only return members that satisfy a given predicate.
### isfunction()
Return true if the object is a user-defined function.

    Function objects provide these attributes:
        __doc__         documentation string
        __name__        name with which this function was defined
        __code__        code object containing compiled function bytecode
        __defaults__    tuple of any default values for arguments
        __globals__     global namespace in which this function was defined
        __annotations__ dict of parameter annotations
        __kwdefaults__  dict of keyword only parameters with defaults
### ismethod()
Return true if the object is an instance method.

    Instance method objects provide these attributes:
        __doc__         documentation string
        __name__        name with which this method was defined
        __func__        function object containing implementation of method
        __self__        instance to which this method is bound

# Summary of API for dtcc.model

## Modules

* `logging`

## Classes

### ABC
Helper class that provides a standard way to create an ABC using
    inheritance.
    
### DTCCModel
Base class for all DTCC models. Must implement to_proto and from_proto
    methods that converts to and from the protobuf representation.
    

## Functions:

### MessageToJson()
Converts protobuf message to JSON format.

  Args:
    message: The protocol buffers message instance to serialize.
    including_default_value_fields: If True, singular primitive fields,
        repeated fields, and map fields will always be serialized.  If
        False, only serialize non-empty fields.  Singular message fields
        and oneof fields are not affected by this option.
    preserving_proto_field_name: If True, use the original proto field
        names as defined in the .proto file. If False, convert the field
        names to lowerCamelCase.
    indent: The JSON object will be pretty-printed with this indent level.
        An indent level of 0 or negative will only insert newlines.
    sort_keys: If True, then the output will be sorted by field names.
    use_integers_for_enums: If true, print integers instead of enum names.
    descriptor_pool: A Descriptor Pool for resolving types. If None use the
        default.
    float_precision: If set, use this to specify float field valid digits.
    ensure_ascii: If True, strings with non-ASCII characters are escaped.
        If False, Unicode strings are returned unchanged.

  Returns:
    A string containing the JSON formatted protocol buffer message.
  
### _add_method()
None
### abstractmethod()
A decorator indicating abstract methods.

    Requires that the metaclass is ABCMeta or derived from it.  A
    class that has a metaclass derived from ABCMeta cannot be
    instantiated unless all of its abstract methods are overridden.
    The abstract methods can be called using any of the normal
    'super' call mechanisms.  abstractmethod() may be used to declare
    abstract methods for properties and descriptors.

    Usage:

        class C(metaclass=ABCMeta):
            @abstractmethod
            def my_abstract_method(self, ...):
                ...
    
### dataclass()
Add dunder methods based on the fields defined in the class.

    Examines PEP 526 __annotations__ to determine fields.

    If init is true, an __init__() method is added to the class. If repr
    is true, a __repr__() method is added. If order is true, rich
    comparison dunder methods are added. If unsafe_hash is true, a
    __hash__() method is added. If frozen is true, fields may not be
    assigned to after instance creation. If match_args is true, the
    __match_args__ tuple is added. If kw_only is true, then by default
    all fields are keyword-only. If slots is true, a new class with a
    __slots__ attribute is returned.
    
### field()
Return an object to identify dataclass fields.

    default is the default value of the field.  default_factory is a
    0-argument function called to initialize a field's value.  If init
    is true, the field will be a parameter to the class's __init__()
    function.  If repr is true, the field will be included in the
    object's repr().  If hash is true, the field will be included in the
    object's hash().  If compare is true, the field will be used in
    comparison functions.  metadata, if specified, must be a mapping
    which is stored but not otherwise examined by dataclass.  If kw_only
    is true, the field will become a keyword-only parameter to
    __init__().

    It is an error to specify both default and default_factory.
    
### getmembers()
Return all members of an object as (name, value) pairs sorted by name.
    Optionally, only return members that satisfy a given predicate.
### isfunction()
Return true if the object is a user-defined function.

    Function objects provide these attributes:
        __doc__         documentation string
        __name__        name with which this function was defined
        __code__        code object containing compiled function bytecode
        __defaults__    tuple of any default values for arguments
        __globals__     global namespace in which this function was defined
        __annotations__ dict of parameter annotations
        __kwdefaults__  dict of keyword only parameters with defaults
### ismethod()
Return true if the object is an instance method.

    Instance method objects provide these attributes:
        __doc__         documentation string
        __name__        name with which this method was defined
        __func__        function object containing implementation of method
        __self__        instance to which this method is bound
### ismodule()
Return true if the object is a module.

    Module objects provide these attributes:
        __cached__      pathname to byte compiled file
        __doc__         documentation string
        __file__        filename (missing for built-in modules)

# Summary of API for dtcc.pointcloud

## Modules

* `np`
* `proto`
* `sys`

## Classes

### Bounds
Bounds(xmin: float = 0.0, ymin: float = 0.0, xmax: float = 0.0, ymax: float = 0.0)
### DTCCModel
Base class for all DTCC models. Must implement to_proto and from_proto
    methods that converts to and from the protobuf representation.
    
### Georef
Georef(crs: str = '', epsg: int = 0, x0: float = 0.0, y0: float = 0.0)
### PointCloud
A point cloud is a set of points with associated attributes.
    Attributes:
      bounds (Bounds): The bounds of the point cloud.
      georef (Georef): The georeference of the point cloud.
      points (np.ndarray): The points of the point cloud as (n,3) dimensional numpy array.

      The following attributes are as defined in the las specification:
      classification (np.ndarray): The classification of the points as (n,) dimensional numpy array.
      intensity (np.ndarray): The intensity of the points as (n,) dimensional numpy array.
      return_number (np.ndarray): The return number of the points as (n,) dimensional numpy array.
      num_returns (np.ndarray): The number of returns of the points as (n,) dimensional numpy array.


    

## Functions:

### dataclass()
Add dunder methods based on the fields defined in the class.

    Examines PEP 526 __annotations__ to determine fields.

    If init is true, an __init__() method is added to the class. If repr
    is true, a __repr__() method is added. If order is true, rich
    comparison dunder methods are added. If unsafe_hash is true, a
    __hash__() method is added. If frozen is true, fields may not be
    assigned to after instance creation. If match_args is true, the
    __match_args__ tuple is added. If kw_only is true, then by default
    all fields are keyword-only. If slots is true, a new class with a
    __slots__ attribute is returned.
    
### field()
Return an object to identify dataclass fields.

    default is the default value of the field.  default_factory is a
    0-argument function called to initialize a field's value.  If init
    is true, the field will be a parameter to the class's __init__()
    function.  If repr is true, the field will be included in the
    object's repr().  If hash is true, the field will be included in the
    object's hash().  If compare is true, the field will be used in
    comparison functions.  metadata, if specified, must be a mapping
    which is stored but not otherwise examined by dataclass.  If kw_only
    is true, the field will become a keyword-only parameter to
    __init__().

    It is an error to specify both default and default_factory.
    

# Summary of API for dtcc.proto

## Modules

* `_descriptor`
* `_message`
* `_reflection`
* `_symbol_database`

## Classes

### AffineTransform
None
### Bounds
None
### Building
None
### City
None
### Georef
None
### Grid
None
### GridField
None
### GridVectorField
None
### LandUse
None
### LineString
None
### LineString3D
None
### LinearRing
None
### Mesh
None
### MeshField
None
### MeshVectorField
None
### MultiPoint
None
### MultiPoint3D
None
### MultiPolygon
None
### PointCloud
None
### Polygon
None
### Raster
None
### Road
None
### RoadNetwork
None
### Vector2D
None
### Vector3D
None
### VolumeMesh
None
### VolumeMeshField
None
### VolumeMeshVectorField
None

## Functions:


# Summary of API for dtcc.raster

## Modules

* `np`
* `proto`

## Classes

### Affine
Two dimensional affine transform for 2D linear mapping.

    Parameters
    ----------
    a, b, c, d, e, f : float
        Coefficients of an augmented affine transformation matrix

        | x' |   | a  b  c | | x |
        | y' | = | d  e  f | | y |
        | 1  |   | 0  0  1 | | 1 |

        `a`, `b`, and `c` are the elements of the first row of the
        matrix. `d`, `e`, and `f` are the elements of the second row.

    Attributes
    ----------
    a, b, c, d, e, f, g, h, i : float
        The coefficients of the 3x3 augmented affine transformation
        matrix

        | x' |   | a  b  c | | x |
        | y' | = | d  e  f | | y |
        | 1  |   | g  h  i | | 1 |

        `g`, `h`, and `i` are always 0, 0, and 1.

    The Affine package is derived from Casey Duncan's Planar package.
    See the copyright statement below.  Parallel lines are preserved by
    these transforms. Affine transforms can perform any combination of
    translations, scales/flips, shears, and rotations.  Class methods
    are provided to conveniently compose transforms from these
    operations.

    Internally the transform is stored as a 3x3 transformation matrix.
    The transform may be constructed directly by specifying the first
    two rows of matrix values as 6 floats. Since the matrix is an affine
    transform, the last row is always ``(0, 0, 1)``.

    N.B.: multiplication of a transform and an (x, y) vector *always*
    returns the column vector that is the matrix multiplication product
    of the transform and (x, y) as a column vector, no matter which is
    on the left or right side. This is obviously not the case for
    matrices and vectors in general, but provides a convenience for
    users of this class.

    
### Bounds
Bounds(xmin: float = 0.0, ymin: float = 0.0, xmax: float = 0.0, ymax: float = 0.0)
### DTCCModel
Base class for all DTCC models. Must implement to_proto and from_proto
    methods that converts to and from the protobuf representation.
    
### Raster
A georeferenced n-dimensional raster of values.
    data is a numpy array of shape (height, width, channels) or (height, width)
    if channels is 1.
    

## Functions:

### dataclass()
Add dunder methods based on the fields defined in the class.

    Examines PEP 526 __annotations__ to determine fields.

    If init is true, an __init__() method is added to the class. If repr
    is true, a __repr__() method is added. If order is true, rich
    comparison dunder methods are added. If unsafe_hash is true, a
    __hash__() method is added. If frozen is true, fields may not be
    assigned to after instance creation. If match_args is true, the
    __match_args__ tuple is added. If kw_only is true, then by default
    all fields are keyword-only. If slots is true, a new class with a
    __slots__ attribute is returned.
    
### field()
Return an object to identify dataclass fields.

    default is the default value of the field.  default_factory is a
    0-argument function called to initialize a field's value.  If init
    is true, the field will be a parameter to the class's __init__()
    function.  If repr is true, the field will be included in the
    object's repr().  If hash is true, the field will be included in the
    object's hash().  If compare is true, the field will be used in
    comparison functions.  metadata, if specified, must be a mapping
    which is stored but not otherwise examined by dataclass.  If kw_only
    is true, the field will become a keyword-only parameter to
    __init__().

    It is an error to specify both default and default_factory.
    
### getmembers()
Return all members of an object as (name, value) pairs sorted by name.
    Optionally, only return members that satisfy a given predicate.
### isfunction()
Return true if the object is a user-defined function.

    Function objects provide these attributes:
        __doc__         documentation string
        __name__        name with which this function was defined
        __code__        code object containing compiled function bytecode
        __defaults__    tuple of any default values for arguments
        __globals__     global namespace in which this function was defined
        __annotations__ dict of parameter annotations
        __kwdefaults__  dict of keyword only parameters with defaults
### ismethod()
Return true if the object is an instance method.

    Instance method objects provide these attributes:
        __doc__         documentation string
        __name__        name with which this method was defined
        __func__        function object containing implementation of method
        __self__        instance to which this method is bound

# Summary of API for dtcc.roadnetwork

## Modules

* `np`
* `proto`

## Classes

### Any
Special type indicating an unconstrained type.

    - Any is compatible with every type.
    - Any assumed to have all methods.
    - All values assumed to be instances of Any.

    Note that all the above statements are true from the point of view of
    static type checkers. At runtime, Any should not be used with instance
    checks.
    
### DTCCModel
Base class for all DTCC models. Must implement to_proto and from_proto
    methods that converts to and from the protobuf representation.
    
### Enum

    Create a collection of name/value pairs.

    Example enumeration:

    >>> class Color(Enum):
    ...     RED = 1
    ...     BLUE = 2
    ...     GREEN = 3

    Access them by:

    - attribute access::

    >>> Color.RED
    <Color.RED: 1>

    - value lookup:

    >>> Color(1)
    <Color.RED: 1>

    - name lookup:

    >>> Color['RED']
    <Color.RED: 1>

    Enumerations can be iterated over, and know how many members they have:

    >>> len(Color)
    3

    >>> list(Color)
    [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]

    Methods can be added to enumerations, and members can have their own
    attributes -- see the documentation for details.
    
### Georef
Georef(crs: str = '', epsg: int = 0, x0: float = 0.0, y0: float = 0.0)
### LineString

    A geometry type composed of one or more line segments.

    A LineString is a one-dimensional feature and has a non-zero length but
    zero area. It may approximate a curve and need not be straight. Unlike a
    LinearRing, a LineString is not closed.

    Parameters
    ----------
    coordinates : sequence
        A sequence of (x, y, [,z]) numeric coordinate pairs or triples, or
        an array-like with shape (N, 2) or (N, 3).
        Also can be a sequence of Point objects.

    Examples
    --------
    Create a LineString with two segments

    >>> a = LineString([[0, 0], [1, 0], [1, 1]])
    >>> a.length
    2.0
    
### Road
Road(road_geometry: shapely.geometry.linestring.LineString = <factory>, road_vertices: List[int] = <factory>, road_type: dtcc_model.roadnetwork.RoadType = <RoadType.PRIMARY: 2>, road_width: float = 0, tunnel: bool = False, bridge: bool = False, lanes: int = 1, speed_limit: float = 0, road_name: str = '', road_id: str = '')
### RoadNetwork
RoadNetwork(roads: List[dtcc_model.roadnetwork.Road] = <factory>, vertices: numpy.ndarray = <factory>, georef: dtcc_model.geometry.Georef = <factory>)
### RoadType
None
### auto

    Instances are replaced with an appropriate value in Enum class suites.
    

## Functions:

### dataclass()
Add dunder methods based on the fields defined in the class.

    Examines PEP 526 __annotations__ to determine fields.

    If init is true, an __init__() method is added to the class. If repr
    is true, a __repr__() method is added. If order is true, rich
    comparison dunder methods are added. If unsafe_hash is true, a
    __hash__() method is added. If frozen is true, fields may not be
    assigned to after instance creation. If match_args is true, the
    __match_args__ tuple is added. If kw_only is true, then by default
    all fields are keyword-only. If slots is true, a new class with a
    __slots__ attribute is returned.
    
### field()
Return an object to identify dataclass fields.

    default is the default value of the field.  default_factory is a
    0-argument function called to initialize a field's value.  If init
    is true, the field will be a parameter to the class's __init__()
    function.  If repr is true, the field will be included in the
    object's repr().  If hash is true, the field will be included in the
    object's hash().  If compare is true, the field will be used in
    comparison functions.  metadata, if specified, must be a mapping
    which is stored but not otherwise examined by dataclass.  If kw_only
    is true, the field will become a keyword-only parameter to
    __init__().

    It is an error to specify both default and default_factory.
    

# Summary of API for dtcc.utils

## Modules

* `dtcc_pb2`
* `shapely`

## Classes


## Functions:

### coords_to_pb_linear_ring()
None
### pb_polygon_from_shapely()
None
### pb_polygon_to_shapely()
None

