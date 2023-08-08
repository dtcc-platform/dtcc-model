# Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`namespace `[`dtcc_model::building`](#namespacedtcc__model_1_1building) | 
`namespace `[`dtcc_model::city`](#namespacedtcc__model_1_1city) | 
`namespace `[`dtcc_model::geometry`](#namespacedtcc__model_1_1geometry) | 
`namespace `[`dtcc_model::grid`](#namespacedtcc__model_1_1grid) | 
`namespace `[`dtcc_model::gridfields`](#namespacedtcc__model_1_1gridfields) | 
`namespace `[`dtcc_model::landuse`](#namespacedtcc__model_1_1landuse) | 
`namespace `[`dtcc_model::logging`](#namespacedtcc__model_1_1logging) | 
`namespace `[`dtcc_model::meshes`](#namespacedtcc__model_1_1meshes) | 
`namespace `[`dtcc_model::meshfields`](#namespacedtcc__model_1_1meshfields) | 
`namespace `[`dtcc_model::model`](#namespacedtcc__model_1_1model) | 
`namespace `[`dtcc_model::pointcloud`](#namespacedtcc__model_1_1pointcloud) | 
`namespace `[`dtcc_model::raster`](#namespacedtcc__model_1_1raster) | 
`namespace `[`dtcc_model::roadnetwork`](#namespacedtcc__model_1_1roadnetwork) | 
`namespace `[`dtcc_model::utils`](#namespacedtcc__model_1_1utils) | 

# namespace `dtcc_model::building` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`class `[`dtcc_model::building::Building`](#classdtcc__model_1_1building_1_1_building) | A base representation of a singele building.

# class `dtcc_model::building::Building` 

```
class dtcc_model::building::Building
  : public dtcc_model.model.DTCCModel
```  

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

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`footprint`](#classdtcc__model_1_1building_1_1_building_1a87b678e340512ede9570457a2961ef0f) | 
`public  `[`uuid`](#classdtcc__model_1_1building_1_1_building_1abd0f702fb3554fdf2051237f40b33e2f) | 
`public  `[`height`](#classdtcc__model_1_1building_1_1_building_1af726d35966084abf27c5978cef7cf0ce) | 
`public  `[`ground_level`](#classdtcc__model_1_1building_1_1_building_1a7753667f27d7c8330d866b81f08d2b46) | 
`public  `[`error`](#classdtcc__model_1_1building_1_1_building_1aa113cf48d7563c5a7513383a2b9acc8a) | 
`public  `[`roofpoints`](#classdtcc__model_1_1building_1_1_building_1a0cf1bf7aacda910a008225020305b135) | 
`public  `[`__str__`](#classdtcc__model_1_1building_1_1_building_1ae166ff6eec1339bf4bf81888c17773bc)`(self)` | 
`public  `[`area`](#classdtcc__model_1_1building_1_1_building_1a0dda135e8fd90b6eb3619cc014123afa)`(self)` | 
`public  `[`from_proto`](#classdtcc__model_1_1building_1_1_building_1aaf036d9928b7ac93d6c806d852f44a6e)`(self,Union pb)` | 
`public proto.Building `[`to_proto`](#classdtcc__model_1_1building_1_1_building_1a0944f04f57fa0b663a67e8028e23f197)`(self)` | 
`public Any `[`__getitem__`](#classdtcc__model_1_1building_1_1_building_1aba3b2674661429ce98a615112366d1cb)`(self,str key)` | 
`public  `[`__setitem__`](#classdtcc__model_1_1building_1_1_building_1a287f0be5b1d02db91ed986b3edd0018e)`(self,str key,Any value)` | 

## Members

#### `public  `[`footprint`](#classdtcc__model_1_1building_1_1_building_1a87b678e340512ede9570457a2961ef0f) 

#### `public  `[`uuid`](#classdtcc__model_1_1building_1_1_building_1abd0f702fb3554fdf2051237f40b33e2f) 

#### `public  `[`height`](#classdtcc__model_1_1building_1_1_building_1af726d35966084abf27c5978cef7cf0ce) 

#### `public  `[`ground_level`](#classdtcc__model_1_1building_1_1_building_1a7753667f27d7c8330d866b81f08d2b46) 

#### `public  `[`error`](#classdtcc__model_1_1building_1_1_building_1aa113cf48d7563c5a7513383a2b9acc8a) 

#### `public  `[`roofpoints`](#classdtcc__model_1_1building_1_1_building_1a0cf1bf7aacda910a008225020305b135) 

#### `public  `[`__str__`](#classdtcc__model_1_1building_1_1_building_1ae166ff6eec1339bf4bf81888c17773bc)`(self)` 

#### `public  `[`area`](#classdtcc__model_1_1building_1_1_building_1a0dda135e8fd90b6eb3619cc014123afa)`(self)` 

#### `public  `[`from_proto`](#classdtcc__model_1_1building_1_1_building_1aaf036d9928b7ac93d6c806d852f44a6e)`(self,Union pb)` 

#### `public proto.Building `[`to_proto`](#classdtcc__model_1_1building_1_1_building_1a0944f04f57fa0b663a67e8028e23f197)`(self)` 

#### `public Any `[`__getitem__`](#classdtcc__model_1_1building_1_1_building_1aba3b2674661429ce98a615112366d1cb)`(self,str key)` 

#### `public  `[`__setitem__`](#classdtcc__model_1_1building_1_1_building_1a287f0be5b1d02db91ed986b3edd0018e)`(self,str key,Any value)` 

# namespace `dtcc_model::city` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`class `[`dtcc_model::city::City`](#classdtcc__model_1_1city_1_1_city) | A City is the top-level container class for city models

# class `dtcc_model::city::City` 

```
class dtcc_model::city::City
  : public dtcc_model.model.DTCCModel
```  

A City is the top-level container class for city models

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`name`](#classdtcc__model_1_1city_1_1_city_1a374f2d78485e7357c15450c0a59d0f78) | 
`public  `[`buildings`](#classdtcc__model_1_1city_1_1_city_1abcb74494dea1b4ad140f706f627864de) | 
`public  `[`landuse`](#classdtcc__model_1_1city_1_1_city_1a8c3152f7e58fb8c953ddf787f64e1e8d) | 
`public  `[`__str__`](#classdtcc__model_1_1city_1_1_city_1a5bd35711723b8fe772c20be63198ecd0)`(self)` | 
`public  `[`origin`](#classdtcc__model_1_1city_1_1_city_1a988e7f9291df901cd871f0b2dd346fe0)`(self)` | 
`public  `[`add_building`](#classdtcc__model_1_1city_1_1_city_1aae502714002c101dcfa8f09eed33dfeb)`(self,`[`Building`](#classdtcc__model_1_1building_1_1_building)` building)` | 
`public  `[`from_proto`](#classdtcc__model_1_1city_1_1_city_1afdcac30000984a3dd6f2bd24e507105d)`(self,Union pb)` | 
`public proto.City `[`to_proto`](#classdtcc__model_1_1city_1_1_city_1aa6a0ab536ae347d66a1e2a5143c3a656)`(self)` | 

## Members

#### `public  `[`name`](#classdtcc__model_1_1city_1_1_city_1a374f2d78485e7357c15450c0a59d0f78) 

#### `public  `[`buildings`](#classdtcc__model_1_1city_1_1_city_1abcb74494dea1b4ad140f706f627864de) 

#### `public  `[`landuse`](#classdtcc__model_1_1city_1_1_city_1a8c3152f7e58fb8c953ddf787f64e1e8d) 

#### `public  `[`__str__`](#classdtcc__model_1_1city_1_1_city_1a5bd35711723b8fe772c20be63198ecd0)`(self)` 

#### `public  `[`origin`](#classdtcc__model_1_1city_1_1_city_1a988e7f9291df901cd871f0b2dd346fe0)`(self)` 

#### `public  `[`add_building`](#classdtcc__model_1_1city_1_1_city_1aae502714002c101dcfa8f09eed33dfeb)`(self,`[`Building`](#classdtcc__model_1_1building_1_1_building)` building)` 

#### `public  `[`from_proto`](#classdtcc__model_1_1city_1_1_city_1afdcac30000984a3dd6f2bd24e507105d)`(self,Union pb)` 

#### `public proto.City `[`to_proto`](#classdtcc__model_1_1city_1_1_city_1aa6a0ab536ae347d66a1e2a5143c3a656)`(self)` 

# namespace `dtcc_model::geometry` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`class `[`dtcc_model::geometry::Bounds`](#classdtcc__model_1_1geometry_1_1_bounds) | 
`class `[`dtcc_model::geometry::Georef`](#classdtcc__model_1_1geometry_1_1_georef) | 

# class `dtcc_model::geometry::Bounds` 

```
class dtcc_model::geometry::Bounds
  : public dtcc_model.model.DTCCModel
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`xmin`](#classdtcc__model_1_1geometry_1_1_bounds_1ab86cf5eb2a93b3b791017f109c5f7b43) | 
`public  `[`ymin`](#classdtcc__model_1_1geometry_1_1_bounds_1a24c65d6fec6e7a8aeedec5bd5b2d970b) | 
`public  `[`xmax`](#classdtcc__model_1_1geometry_1_1_bounds_1a380c80ffc95555c7ed34ba76d151374d) | 
`public  `[`ymax`](#classdtcc__model_1_1geometry_1_1_bounds_1a849b48ec00ec8836d32ecb9cfd8ab6e6) | 
`public  `[`__str__`](#classdtcc__model_1_1geometry_1_1_bounds_1a73b53ee9b3d34157cbf72094ec3e4c4d)`(self)` | 
`public str `[`bndstr`](#classdtcc__model_1_1geometry_1_1_bounds_1ac9d3468a24dc6cd4b8ae20b151582490)`(self)` | 
`public float `[`width`](#classdtcc__model_1_1geometry_1_1_bounds_1acadbc1366aeb7b479a4d16705c0cfd6b)`(self)` | 
`public float `[`height`](#classdtcc__model_1_1geometry_1_1_bounds_1a7faf4b01043540becfdb5f1a28392ea6)`(self)` | 
`public float `[`north`](#classdtcc__model_1_1geometry_1_1_bounds_1a2c44861f6261943988488c9c2ec93682)`(self)` | 
`public float `[`south`](#classdtcc__model_1_1geometry_1_1_bounds_1aa1cf9279aede774ace2ec0ed349f96b9)`(self)` | 
`public float `[`east`](#classdtcc__model_1_1geometry_1_1_bounds_1a1e7f05765eeb4f681b7568618eb70a55)`(self)` | 
`public float `[`west`](#classdtcc__model_1_1geometry_1_1_bounds_1a707d42134e7f916b842e9b85deddd8c0)`(self)` | 
`public tuple `[`tuple`](#classdtcc__model_1_1geometry_1_1_bounds_1ada134b16111f7d28be7549763cf9ed44)`(self)` | 
`public float `[`area`](#classdtcc__model_1_1geometry_1_1_bounds_1a29189b6f54e3327c589c02d422a48baa)`(self)` | 
`public tuple `[`center`](#classdtcc__model_1_1geometry_1_1_bounds_1a6f2eefec9ed4a2ddb5ade70a324fbfd6)`(self)` | 
`public  `[`buffer`](#classdtcc__model_1_1geometry_1_1_bounds_1aadc176a9ea1d4ebb886a05e3ea225c99)`(self,float distance)` | 
`public  `[`union`](#classdtcc__model_1_1geometry_1_1_bounds_1a048d6a7ea29d567d7903ef606582798e)`(self,other)` | 
`public  `[`intersect`](#classdtcc__model_1_1geometry_1_1_bounds_1a13f0affc59deb7c0cbeff5158a5c4435)`(self,other)` | 
`public  `[`from_proto`](#classdtcc__model_1_1geometry_1_1_bounds_1a2accadfd2b4158f0993b4a18099ba95b)`(self,Union pb)` | 
`public proto.Bounds `[`to_proto`](#classdtcc__model_1_1geometry_1_1_bounds_1a97c39117da28f186f3479eb4560aa828)`(self)` | 

## Members

#### `public  `[`xmin`](#classdtcc__model_1_1geometry_1_1_bounds_1ab86cf5eb2a93b3b791017f109c5f7b43) 

#### `public  `[`ymin`](#classdtcc__model_1_1geometry_1_1_bounds_1a24c65d6fec6e7a8aeedec5bd5b2d970b) 

#### `public  `[`xmax`](#classdtcc__model_1_1geometry_1_1_bounds_1a380c80ffc95555c7ed34ba76d151374d) 

#### `public  `[`ymax`](#classdtcc__model_1_1geometry_1_1_bounds_1a849b48ec00ec8836d32ecb9cfd8ab6e6) 

#### `public  `[`__str__`](#classdtcc__model_1_1geometry_1_1_bounds_1a73b53ee9b3d34157cbf72094ec3e4c4d)`(self)` 

#### `public str `[`bndstr`](#classdtcc__model_1_1geometry_1_1_bounds_1ac9d3468a24dc6cd4b8ae20b151582490)`(self)` 

#### `public float `[`width`](#classdtcc__model_1_1geometry_1_1_bounds_1acadbc1366aeb7b479a4d16705c0cfd6b)`(self)` 

#### `public float `[`height`](#classdtcc__model_1_1geometry_1_1_bounds_1a7faf4b01043540becfdb5f1a28392ea6)`(self)` 

#### `public float `[`north`](#classdtcc__model_1_1geometry_1_1_bounds_1a2c44861f6261943988488c9c2ec93682)`(self)` 

#### `public float `[`south`](#classdtcc__model_1_1geometry_1_1_bounds_1aa1cf9279aede774ace2ec0ed349f96b9)`(self)` 

#### `public float `[`east`](#classdtcc__model_1_1geometry_1_1_bounds_1a1e7f05765eeb4f681b7568618eb70a55)`(self)` 

#### `public float `[`west`](#classdtcc__model_1_1geometry_1_1_bounds_1a707d42134e7f916b842e9b85deddd8c0)`(self)` 

#### `public tuple `[`tuple`](#classdtcc__model_1_1geometry_1_1_bounds_1ada134b16111f7d28be7549763cf9ed44)`(self)` 

#### `public float `[`area`](#classdtcc__model_1_1geometry_1_1_bounds_1a29189b6f54e3327c589c02d422a48baa)`(self)` 

#### `public tuple `[`center`](#classdtcc__model_1_1geometry_1_1_bounds_1a6f2eefec9ed4a2ddb5ade70a324fbfd6)`(self)` 

#### `public  `[`buffer`](#classdtcc__model_1_1geometry_1_1_bounds_1aadc176a9ea1d4ebb886a05e3ea225c99)`(self,float distance)` 

#### `public  `[`union`](#classdtcc__model_1_1geometry_1_1_bounds_1a048d6a7ea29d567d7903ef606582798e)`(self,other)` 

#### `public  `[`intersect`](#classdtcc__model_1_1geometry_1_1_bounds_1a13f0affc59deb7c0cbeff5158a5c4435)`(self,other)` 

#### `public  `[`from_proto`](#classdtcc__model_1_1geometry_1_1_bounds_1a2accadfd2b4158f0993b4a18099ba95b)`(self,Union pb)` 

#### `public proto.Bounds `[`to_proto`](#classdtcc__model_1_1geometry_1_1_bounds_1a97c39117da28f186f3479eb4560aa828)`(self)` 

# class `dtcc_model::geometry::Georef` 

```
class dtcc_model::geometry::Georef
  : public dtcc_model.model.DTCCModel
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`crs`](#classdtcc__model_1_1geometry_1_1_georef_1a01cc05353a41065f42a228c9760aba5a) | 
`public  `[`epsg`](#classdtcc__model_1_1geometry_1_1_georef_1afc9595e7c0cffecb5e6b403e5ad2c7d3) | 
`public  `[`x0`](#classdtcc__model_1_1geometry_1_1_georef_1a0266abf76ddc7781b829dac8e2f5f9c8) | 
`public  `[`y0`](#classdtcc__model_1_1geometry_1_1_georef_1aaba65e6fe5bc8da0c373592053ea3a05) | 
`public  `[`__str__`](#classdtcc__model_1_1geometry_1_1_georef_1a785a3314f3512559bcfe948045720b4c)`(self)` | 
`public  `[`from_proto`](#classdtcc__model_1_1geometry_1_1_georef_1abdd9e1ee574963e2d543731a4faf34e6)`(self,Union pb)` | 
`public proto.Georef `[`to_proto`](#classdtcc__model_1_1geometry_1_1_georef_1a07e6d1ad3391bd0dfd309bca5c7b8810)`(self)` | 

## Members

#### `public  `[`crs`](#classdtcc__model_1_1geometry_1_1_georef_1a01cc05353a41065f42a228c9760aba5a) 

#### `public  `[`epsg`](#classdtcc__model_1_1geometry_1_1_georef_1afc9595e7c0cffecb5e6b403e5ad2c7d3) 

#### `public  `[`x0`](#classdtcc__model_1_1geometry_1_1_georef_1a0266abf76ddc7781b829dac8e2f5f9c8) 

#### `public  `[`y0`](#classdtcc__model_1_1geometry_1_1_georef_1aaba65e6fe5bc8da0c373592053ea3a05) 

#### `public  `[`__str__`](#classdtcc__model_1_1geometry_1_1_georef_1a785a3314f3512559bcfe948045720b4c)`(self)` 

#### `public  `[`from_proto`](#classdtcc__model_1_1geometry_1_1_georef_1abdd9e1ee574963e2d543731a4faf34e6)`(self,Union pb)` 

#### `public proto.Georef `[`to_proto`](#classdtcc__model_1_1geometry_1_1_georef_1a07e6d1ad3391bd0dfd309bca5c7b8810)`(self)` 

# namespace `dtcc_model::grid` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`class `[`dtcc_model::grid::Grid`](#classdtcc__model_1_1grid_1_1_grid) | 

# class `dtcc_model::grid::Grid` 

```
class dtcc_model::grid::Grid
  : public dtcc_model.model.DTCCModel
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`width`](#classdtcc__model_1_1grid_1_1_grid_1a13234f013264ee08681601a093837289) | 
`public  `[`height`](#classdtcc__model_1_1grid_1_1_grid_1a15bf1d4fc51f766379e468d19f01f79c) | 
`public  `[`xstep`](#classdtcc__model_1_1grid_1_1_grid_1a319d1e60af356bf2a86446e05f0d9293) | 
`public  `[`ystep`](#classdtcc__model_1_1grid_1_1_grid_1a79f5e3edd43a2dbaacc3d6ef8f882a8c) | 
`public  `[`__str__`](#classdtcc__model_1_1grid_1_1_grid_1aa448e292267017e0969fb60d67127793)`(self)` | 
`public int `[`num_vertices`](#classdtcc__model_1_1grid_1_1_grid_1a3ebefb68c3e25543cfb4a3fbc880db02)`(self)` | 
`public int `[`num_cells`](#classdtcc__model_1_1grid_1_1_grid_1aa5e6db9f05095deb5085a5014c4207cc)`(self)` | 
`public  `[`from_proto`](#classdtcc__model_1_1grid_1_1_grid_1a8e9b78c8dede7a9c48f7f39912aa9816)`(self,Union pb)` | 
`public proto.Mesh `[`to_proto`](#classdtcc__model_1_1grid_1_1_grid_1a72b2a5f6ce0ac87725afd1b4444fd37d)`(self)` | 

## Members

#### `public  `[`width`](#classdtcc__model_1_1grid_1_1_grid_1a13234f013264ee08681601a093837289) 

#### `public  `[`height`](#classdtcc__model_1_1grid_1_1_grid_1a15bf1d4fc51f766379e468d19f01f79c) 

#### `public  `[`xstep`](#classdtcc__model_1_1grid_1_1_grid_1a319d1e60af356bf2a86446e05f0d9293) 

#### `public  `[`ystep`](#classdtcc__model_1_1grid_1_1_grid_1a79f5e3edd43a2dbaacc3d6ef8f882a8c) 

#### `public  `[`__str__`](#classdtcc__model_1_1grid_1_1_grid_1aa448e292267017e0969fb60d67127793)`(self)` 

#### `public int `[`num_vertices`](#classdtcc__model_1_1grid_1_1_grid_1a3ebefb68c3e25543cfb4a3fbc880db02)`(self)` 

#### `public int `[`num_cells`](#classdtcc__model_1_1grid_1_1_grid_1aa5e6db9f05095deb5085a5014c4207cc)`(self)` 

#### `public  `[`from_proto`](#classdtcc__model_1_1grid_1_1_grid_1a8e9b78c8dede7a9c48f7f39912aa9816)`(self,Union pb)` 

#### `public proto.Mesh `[`to_proto`](#classdtcc__model_1_1grid_1_1_grid_1a72b2a5f6ce0ac87725afd1b4444fd37d)`(self)` 

# namespace `dtcc_model::gridfields` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`class `[`dtcc_model::gridfields::GridField`](#classdtcc__model_1_1gridfields_1_1_grid_field) | 
`class `[`dtcc_model::gridfields::GridVectorField`](#classdtcc__model_1_1gridfields_1_1_grid_vector_field) | 

# class `dtcc_model::gridfields::GridField` 

```
class dtcc_model::gridfields::GridField
  : public dtcc_model.model.DTCCModel
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`values`](#classdtcc__model_1_1gridfields_1_1_grid_field_1a29b1b81ccdeb8a7f5b61daeca4211e57) | 
`public  `[`__str__`](#classdtcc__model_1_1gridfields_1_1_grid_field_1a2c2412f4e794809a5613e56c79e2e62e)`(self)` | 
`public  `[`from_proto`](#classdtcc__model_1_1gridfields_1_1_grid_field_1a1659c981be691595b8d0a82516c6905d)`(self,Union pb)` | 
`public proto.GridField `[`to_proto`](#classdtcc__model_1_1gridfields_1_1_grid_field_1ad061cae1eace9f0c90d4d4271916b4ec)`(self)` | 

## Members

#### `public  `[`values`](#classdtcc__model_1_1gridfields_1_1_grid_field_1a29b1b81ccdeb8a7f5b61daeca4211e57) 

#### `public  `[`__str__`](#classdtcc__model_1_1gridfields_1_1_grid_field_1a2c2412f4e794809a5613e56c79e2e62e)`(self)` 

#### `public  `[`from_proto`](#classdtcc__model_1_1gridfields_1_1_grid_field_1a1659c981be691595b8d0a82516c6905d)`(self,Union pb)` 

#### `public proto.GridField `[`to_proto`](#classdtcc__model_1_1gridfields_1_1_grid_field_1ad061cae1eace9f0c90d4d4271916b4ec)`(self)` 

# class `dtcc_model::gridfields::GridVectorField` 

```
class dtcc_model::gridfields::GridVectorField
  : public dtcc_model.model.DTCCModel
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`values`](#classdtcc__model_1_1gridfields_1_1_grid_vector_field_1ad80e98ca28445e954718a2106f36883d) | 
`public  `[`__str__`](#classdtcc__model_1_1gridfields_1_1_grid_vector_field_1ac56ac3c09c64e19960a7fa9aaf7de9f4)`(self)` | 
`public  `[`from_proto`](#classdtcc__model_1_1gridfields_1_1_grid_vector_field_1a0135e9f41f36544cd8f3bc493a42217a)`(self,Union pb)` | 
`public proto.GridField `[`to_proto`](#classdtcc__model_1_1gridfields_1_1_grid_vector_field_1a442b822dfda3fbc7e0943418ad93b18f)`(self)` | 

## Members

#### `public  `[`values`](#classdtcc__model_1_1gridfields_1_1_grid_vector_field_1ad80e98ca28445e954718a2106f36883d) 

#### `public  `[`__str__`](#classdtcc__model_1_1gridfields_1_1_grid_vector_field_1ac56ac3c09c64e19960a7fa9aaf7de9f4)`(self)` 

#### `public  `[`from_proto`](#classdtcc__model_1_1gridfields_1_1_grid_vector_field_1a0135e9f41f36544cd8f3bc493a42217a)`(self,Union pb)` 

#### `public proto.GridField `[`to_proto`](#classdtcc__model_1_1gridfields_1_1_grid_vector_field_1a442b822dfda3fbc7e0943418ad93b18f)`(self)` 

# namespace `dtcc_model::landuse` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`class `[`dtcc_model::landuse::Landuse`](#classdtcc__model_1_1landuse_1_1_landuse) | A polygon of a singele landuse area.:
`class `[`dtcc_model::landuse::LanduseClasses`](#classdtcc__model_1_1landuse_1_1_landuse_classes) | 

# class `dtcc_model::landuse::Landuse` 

```
class dtcc_model::landuse::Landuse
  : public dtcc_model.model.DTCCModel
```  

A polygon of a singele landuse area.:
available landuse types are:
WATER, GRASS, FOREST, FARMLAND, URBAN, INDUSTRIAL, MILITARY, ROAD, RAIL

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`footprint`](#classdtcc__model_1_1landuse_1_1_landuse_1afcf942133a7b3705736643a78d8bad5a) | 
`public  `[`landuse`](#classdtcc__model_1_1landuse_1_1_landuse_1a14703ea51d95344865bde04b813395d2) | 
`public str `[`__str__`](#classdtcc__model_1_1landuse_1_1_landuse_1ac19eb918edb8db644b3abb7f6239ac1b)`(self)` | 
`public float `[`area`](#classdtcc__model_1_1landuse_1_1_landuse_1ab82c45ce89202fb1fca74dabf779f00c)`(self)` | 
`public proto.LandUse `[`to_proto`](#classdtcc__model_1_1landuse_1_1_landuse_1a0826df5a0b469aeb6c342a4e59ffc1cf)`(self)` | 
`public  `[`from_proto`](#classdtcc__model_1_1landuse_1_1_landuse_1a96850621ba8ab5622f9fd281dae1c35f)`(self,Union pb)` | 

## Members

#### `public  `[`footprint`](#classdtcc__model_1_1landuse_1_1_landuse_1afcf942133a7b3705736643a78d8bad5a) 

#### `public  `[`landuse`](#classdtcc__model_1_1landuse_1_1_landuse_1a14703ea51d95344865bde04b813395d2) 

#### `public str `[`__str__`](#classdtcc__model_1_1landuse_1_1_landuse_1ac19eb918edb8db644b3abb7f6239ac1b)`(self)` 

#### `public float `[`area`](#classdtcc__model_1_1landuse_1_1_landuse_1ab82c45ce89202fb1fca74dabf779f00c)`(self)` 

#### `public proto.LandUse `[`to_proto`](#classdtcc__model_1_1landuse_1_1_landuse_1a0826df5a0b469aeb6c342a4e59ffc1cf)`(self)` 

#### `public  `[`from_proto`](#classdtcc__model_1_1landuse_1_1_landuse_1a96850621ba8ab5622f9fd281dae1c35f)`(self,Union pb)` 

# class `dtcc_model::landuse::LanduseClasses` 

```
class dtcc_model::landuse::LanduseClasses
  : public Enum
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# namespace `dtcc_model::logging` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`set_log_level`](#logging_8py_1ab0bd74b1f6e323151ab966db98f49e25)`(level)`            | 

## Members

#### `public  `[`set_log_level`](#logging_8py_1ab0bd74b1f6e323151ab966db98f49e25)`(level)` 

# namespace `dtcc_model::meshes` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`class `[`dtcc_model::meshes::Mesh`](#classdtcc__model_1_1meshes_1_1_mesh) | 
`class `[`dtcc_model::meshes::VolumeMesh`](#classdtcc__model_1_1meshes_1_1_volume_mesh) | 

# class `dtcc_model::meshes::Mesh` 

```
class dtcc_model::meshes::Mesh
  : public dtcc_model.model.DTCCModel
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`vertices`](#classdtcc__model_1_1meshes_1_1_mesh_1ad1c4f0a10c44f18e7990dc944a9529e0) | 
`public  `[`normals`](#classdtcc__model_1_1meshes_1_1_mesh_1a7c5af47d282fd2c4c9bae420739c2239) | 
`public  `[`faces`](#classdtcc__model_1_1meshes_1_1_mesh_1a08bf54b2d3adeb7991ecaf8598634ea9) | 
`public  `[`__str__`](#classdtcc__model_1_1meshes_1_1_mesh_1a1c745918ad300f47e46608d24b68edc6)`(self)` | 
`public int `[`num_vertices`](#classdtcc__model_1_1meshes_1_1_mesh_1a96d92463f37410bdf15eedb54166bb42)`(self)` | 
`public int `[`num_normals`](#classdtcc__model_1_1meshes_1_1_mesh_1a91cb37e9f73def0264943226d21fd530)`(self)` | 
`public int `[`num_faces`](#classdtcc__model_1_1meshes_1_1_mesh_1ac4aff828b2c05488e3a5e09196392cf7)`(self)` | 
`public  `[`from_proto`](#classdtcc__model_1_1meshes_1_1_mesh_1a253fd48c155682ea0b83f075118c8b43)`(self,Union pb)` | 
`public proto.Mesh `[`to_proto`](#classdtcc__model_1_1meshes_1_1_mesh_1ad51d6e4bd9ab34f58f8c27f142f0af6b)`(self)` | 

## Members

#### `public  `[`vertices`](#classdtcc__model_1_1meshes_1_1_mesh_1ad1c4f0a10c44f18e7990dc944a9529e0) 

#### `public  `[`normals`](#classdtcc__model_1_1meshes_1_1_mesh_1a7c5af47d282fd2c4c9bae420739c2239) 

#### `public  `[`faces`](#classdtcc__model_1_1meshes_1_1_mesh_1a08bf54b2d3adeb7991ecaf8598634ea9) 

#### `public  `[`__str__`](#classdtcc__model_1_1meshes_1_1_mesh_1a1c745918ad300f47e46608d24b68edc6)`(self)` 

#### `public int `[`num_vertices`](#classdtcc__model_1_1meshes_1_1_mesh_1a96d92463f37410bdf15eedb54166bb42)`(self)` 

#### `public int `[`num_normals`](#classdtcc__model_1_1meshes_1_1_mesh_1a91cb37e9f73def0264943226d21fd530)`(self)` 

#### `public int `[`num_faces`](#classdtcc__model_1_1meshes_1_1_mesh_1ac4aff828b2c05488e3a5e09196392cf7)`(self)` 

#### `public  `[`from_proto`](#classdtcc__model_1_1meshes_1_1_mesh_1a253fd48c155682ea0b83f075118c8b43)`(self,Union pb)` 

#### `public proto.Mesh `[`to_proto`](#classdtcc__model_1_1meshes_1_1_mesh_1ad51d6e4bd9ab34f58f8c27f142f0af6b)`(self)` 

# class `dtcc_model::meshes::VolumeMesh` 

```
class dtcc_model::meshes::VolumeMesh
  : public dtcc_model.model.DTCCModel
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`vertices`](#classdtcc__model_1_1meshes_1_1_volume_mesh_1a1aaa1757ffaccad49a8e96fe05502438) | 
`public  `[`cells`](#classdtcc__model_1_1meshes_1_1_volume_mesh_1ac0f9ba5e3e9678b7914fceb1246674d8) | 
`public  `[`__str__`](#classdtcc__model_1_1meshes_1_1_volume_mesh_1a25934c410956801349db44aec44526e9)`(self)` | 
`public int `[`num_vertices`](#classdtcc__model_1_1meshes_1_1_volume_mesh_1a56a9a128dc560e9ad9621cba8a699948)`(self)` | 
`public int `[`num_cells`](#classdtcc__model_1_1meshes_1_1_volume_mesh_1a2af384614da466955d37b1d4a797f7ea)`(self)` | 
`public  `[`from_proto`](#classdtcc__model_1_1meshes_1_1_volume_mesh_1a962d96767360aab9f31d37d58cc267da)`(self,Union pb)` | 
`public proto.Mesh `[`to_proto`](#classdtcc__model_1_1meshes_1_1_volume_mesh_1a08e02fd09122525553d1854d984e51a3)`(self)` | 

## Members

#### `public  `[`vertices`](#classdtcc__model_1_1meshes_1_1_volume_mesh_1a1aaa1757ffaccad49a8e96fe05502438) 

#### `public  `[`cells`](#classdtcc__model_1_1meshes_1_1_volume_mesh_1ac0f9ba5e3e9678b7914fceb1246674d8) 

#### `public  `[`__str__`](#classdtcc__model_1_1meshes_1_1_volume_mesh_1a25934c410956801349db44aec44526e9)`(self)` 

#### `public int `[`num_vertices`](#classdtcc__model_1_1meshes_1_1_volume_mesh_1a56a9a128dc560e9ad9621cba8a699948)`(self)` 

#### `public int `[`num_cells`](#classdtcc__model_1_1meshes_1_1_volume_mesh_1a2af384614da466955d37b1d4a797f7ea)`(self)` 

#### `public  `[`from_proto`](#classdtcc__model_1_1meshes_1_1_volume_mesh_1a962d96767360aab9f31d37d58cc267da)`(self,Union pb)` 

#### `public proto.Mesh `[`to_proto`](#classdtcc__model_1_1meshes_1_1_volume_mesh_1a08e02fd09122525553d1854d984e51a3)`(self)` 

# namespace `dtcc_model::meshfields` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`class `[`dtcc_model::meshfields::MeshField`](#classdtcc__model_1_1meshfields_1_1_mesh_field) | 
`class `[`dtcc_model::meshfields::MeshVectorField`](#classdtcc__model_1_1meshfields_1_1_mesh_vector_field) | 
`class `[`dtcc_model::meshfields::VolumeMeshField`](#classdtcc__model_1_1meshfields_1_1_volume_mesh_field) | 
`class `[`dtcc_model::meshfields::VolumeMeshVectorField`](#classdtcc__model_1_1meshfields_1_1_volume_mesh_vector_field) | 

# class `dtcc_model::meshfields::MeshField` 

```
class dtcc_model::meshfields::MeshField
  : public dtcc_model.model.DTCCModel
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`values`](#classdtcc__model_1_1meshfields_1_1_mesh_field_1ade3a12b2f154156b2b44e99ed96752df) | 
`public  `[`__str__`](#classdtcc__model_1_1meshfields_1_1_mesh_field_1a551db9893539505e5e4fba3e4a7fe974)`(self)` | 
`public  `[`from_proto`](#classdtcc__model_1_1meshfields_1_1_mesh_field_1a157d8f1887396dfd89ea20a0f9db6082)`(self,Union pb)` | 
`public proto.MeshField `[`to_proto`](#classdtcc__model_1_1meshfields_1_1_mesh_field_1a1136e18e14813869c401fc922e0abf9e)`(self)` | 

## Members

#### `public  `[`values`](#classdtcc__model_1_1meshfields_1_1_mesh_field_1ade3a12b2f154156b2b44e99ed96752df) 

#### `public  `[`__str__`](#classdtcc__model_1_1meshfields_1_1_mesh_field_1a551db9893539505e5e4fba3e4a7fe974)`(self)` 

#### `public  `[`from_proto`](#classdtcc__model_1_1meshfields_1_1_mesh_field_1a157d8f1887396dfd89ea20a0f9db6082)`(self,Union pb)` 

#### `public proto.MeshField `[`to_proto`](#classdtcc__model_1_1meshfields_1_1_mesh_field_1a1136e18e14813869c401fc922e0abf9e)`(self)` 

# class `dtcc_model::meshfields::MeshVectorField` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`values`](#classdtcc__model_1_1meshfields_1_1_mesh_vector_field_1afbe3488c0a1156ee49cf32a6b2d2b7a0) | 
`public  `[`__str__`](#classdtcc__model_1_1meshfields_1_1_mesh_vector_field_1adce6190f0d879f6b0f51df40e7164b0a)`(self)` | 
`public  `[`from_proto`](#classdtcc__model_1_1meshfields_1_1_mesh_vector_field_1acf727fc518e5265879fc95145cf5eeb7)`(self,Union pb)` | 
`public proto.MeshVectorField `[`to_proto`](#classdtcc__model_1_1meshfields_1_1_mesh_vector_field_1af344ae0bd2499bc6181f8a32e68e735f)`(self)` | 

## Members

#### `public  `[`values`](#classdtcc__model_1_1meshfields_1_1_mesh_vector_field_1afbe3488c0a1156ee49cf32a6b2d2b7a0) 

#### `public  `[`__str__`](#classdtcc__model_1_1meshfields_1_1_mesh_vector_field_1adce6190f0d879f6b0f51df40e7164b0a)`(self)` 

#### `public  `[`from_proto`](#classdtcc__model_1_1meshfields_1_1_mesh_vector_field_1acf727fc518e5265879fc95145cf5eeb7)`(self,Union pb)` 

#### `public proto.MeshVectorField `[`to_proto`](#classdtcc__model_1_1meshfields_1_1_mesh_vector_field_1af344ae0bd2499bc6181f8a32e68e735f)`(self)` 

# class `dtcc_model::meshfields::VolumeMeshField` 

```
class dtcc_model::meshfields::VolumeMeshField
  : public dtcc_model.model.DTCCModel
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`values`](#classdtcc__model_1_1meshfields_1_1_volume_mesh_field_1a6788fccc2adc834ff536146b2133b8aa) | 
`public  `[`__str__`](#classdtcc__model_1_1meshfields_1_1_volume_mesh_field_1ab33b1ff1e1e14f289125a6211707fe70)`(self)` | 
`public  `[`from_proto`](#classdtcc__model_1_1meshfields_1_1_volume_mesh_field_1a5637b322f47be3b15ec66aed71912cc9)`(self,Union pb)` | 
`public proto.VolumeMeshField `[`to_proto`](#classdtcc__model_1_1meshfields_1_1_volume_mesh_field_1a99897dfb074f70bd93b231700ffc2632)`(self)` | 

## Members

#### `public  `[`values`](#classdtcc__model_1_1meshfields_1_1_volume_mesh_field_1a6788fccc2adc834ff536146b2133b8aa) 

#### `public  `[`__str__`](#classdtcc__model_1_1meshfields_1_1_volume_mesh_field_1ab33b1ff1e1e14f289125a6211707fe70)`(self)` 

#### `public  `[`from_proto`](#classdtcc__model_1_1meshfields_1_1_volume_mesh_field_1a5637b322f47be3b15ec66aed71912cc9)`(self,Union pb)` 

#### `public proto.VolumeMeshField `[`to_proto`](#classdtcc__model_1_1meshfields_1_1_volume_mesh_field_1a99897dfb074f70bd93b231700ffc2632)`(self)` 

# class `dtcc_model::meshfields::VolumeMeshVectorField` 

```
class dtcc_model::meshfields::VolumeMeshVectorField
  : public dtcc_model.model.DTCCModel
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`values`](#classdtcc__model_1_1meshfields_1_1_volume_mesh_vector_field_1ab010a8726da6f589e5d2560becc1cb8b) | 
`public  `[`__str__`](#classdtcc__model_1_1meshfields_1_1_volume_mesh_vector_field_1a8f8b7573dbad758c1b8c1518c05c09ad)`(self)` | 
`public  `[`from_proto`](#classdtcc__model_1_1meshfields_1_1_volume_mesh_vector_field_1a1650cfb2886869580530993d8919674f)`(self,Union pb)` | 
`public proto.VolumeMeshVectorField `[`to_proto`](#classdtcc__model_1_1meshfields_1_1_volume_mesh_vector_field_1a065274a498818ba5db2bffaa1ca5a9b1)`(self)` | 

## Members

#### `public  `[`values`](#classdtcc__model_1_1meshfields_1_1_volume_mesh_vector_field_1ab010a8726da6f589e5d2560becc1cb8b) 

#### `public  `[`__str__`](#classdtcc__model_1_1meshfields_1_1_volume_mesh_vector_field_1a8f8b7573dbad758c1b8c1518c05c09ad)`(self)` 

#### `public  `[`from_proto`](#classdtcc__model_1_1meshfields_1_1_volume_mesh_vector_field_1a1650cfb2886869580530993d8919674f)`(self,Union pb)` 

#### `public proto.VolumeMeshVectorField `[`to_proto`](#classdtcc__model_1_1meshfields_1_1_volume_mesh_vector_field_1a065274a498818ba5db2bffaa1ca5a9b1)`(self)` 

# namespace `dtcc_model::model` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`protected  `[`_add_method`](#model_8py_1a00e28aa52118a2046c16f29bf7bcf7bd)`(cls,function,name)`            | 
`class `[`dtcc_model::model::DTCCModel`](#classdtcc__model_1_1model_1_1_d_t_c_c_model) | Base class for all DTCC models. Must implement to_proto and from_proto

## Members

#### `protected  `[`_add_method`](#model_8py_1a00e28aa52118a2046c16f29bf7bcf7bd)`(cls,function,name)` 

# class `dtcc_model::model::DTCCModel` 

```
class dtcc_model::model::DTCCModel
  : public ABC
```  

Base class for all DTCC models. Must implement to_proto and from_proto
methods that converts to and from the protobuf representation.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`to_proto`](#classdtcc__model_1_1model_1_1_d_t_c_c_model_1a93241d2da190399d8909ff8830e12886)`(self)` | 
`public  `[`from_proto`](#classdtcc__model_1_1model_1_1_d_t_c_c_model_1a80cc52cad31274db7fa25ed8f02fa8c8)`(self,pb)` | 
`public  `[`to_json`](#classdtcc__model_1_1model_1_1_d_t_c_c_model_1a44658e6efba48b1dea068a1e4637bafb)`(self)` | 
`public  `[`add_methods`](#classdtcc__model_1_1model_1_1_d_t_c_c_model_1a6e24e9af398d0822dcdcff35d85ba1dc)`(cls,module,name)` | 
`public  `[`print_methods`](#classdtcc__model_1_1model_1_1_d_t_c_c_model_1ab3d342cc905cdbbd2148d194a974ce9a)`(cls,verbose)` | 
`protected  `[`_methods`](#classdtcc__model_1_1model_1_1_d_t_c_c_model_1a72c3f38e862f599b42fe4d39a0c16450) | 

## Members

#### `public  `[`to_proto`](#classdtcc__model_1_1model_1_1_d_t_c_c_model_1a93241d2da190399d8909ff8830e12886)`(self)` 

#### `public  `[`from_proto`](#classdtcc__model_1_1model_1_1_d_t_c_c_model_1a80cc52cad31274db7fa25ed8f02fa8c8)`(self,pb)` 

#### `public  `[`to_json`](#classdtcc__model_1_1model_1_1_d_t_c_c_model_1a44658e6efba48b1dea068a1e4637bafb)`(self)` 

#### `public  `[`add_methods`](#classdtcc__model_1_1model_1_1_d_t_c_c_model_1a6e24e9af398d0822dcdcff35d85ba1dc)`(cls,module,name)` 

#### `public  `[`print_methods`](#classdtcc__model_1_1model_1_1_d_t_c_c_model_1ab3d342cc905cdbbd2148d194a974ce9a)`(cls,verbose)` 

#### `protected  `[`_methods`](#classdtcc__model_1_1model_1_1_d_t_c_c_model_1a72c3f38e862f599b42fe4d39a0c16450) 

# namespace `dtcc_model::pointcloud` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`class `[`dtcc_model::pointcloud::PointCloud`](#classdtcc__model_1_1pointcloud_1_1_point_cloud) | A point cloud is a set of points with associated attributes.

# class `dtcc_model::pointcloud::PointCloud` 

```
class dtcc_model::pointcloud::PointCloud
  : public dtcc_model.model.DTCCModel
```  

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

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`classification`](#classdtcc__model_1_1pointcloud_1_1_point_cloud_1a2ab366516cf75061dabd18561b4d0354) | 
`public  `[`points`](#classdtcc__model_1_1pointcloud_1_1_point_cloud_1a18e205e17b1373056341d7bac76e4370) | 
`public  `[`bounds`](#classdtcc__model_1_1pointcloud_1_1_point_cloud_1afaf17a76a1b06f930916b0fade059ffa) | 
`public  `[`intensity`](#classdtcc__model_1_1pointcloud_1_1_point_cloud_1ac5a6d2fac81ad6c4ea17dc8d9e332a53) | 
`public  `[`return_number`](#classdtcc__model_1_1pointcloud_1_1_point_cloud_1a788990249db00505d61a2d1ac7778ab7) | 
`public  `[`num_returns`](#classdtcc__model_1_1pointcloud_1_1_point_cloud_1a1ae1b78dc7446250b531f924b00e7207) | 
`public  `[`__str__`](#classdtcc__model_1_1pointcloud_1_1_point_cloud_1a485cffa3907e95cc69542f851a1901da)`(self)` | 
`public  `[`__len__`](#classdtcc__model_1_1pointcloud_1_1_point_cloud_1a489e3654b0170e1b3c84cf687481a1c1)`(self)` | 
`public set `[`used_classifications`](#classdtcc__model_1_1pointcloud_1_1_point_cloud_1a714cf3d76ac0d43331f69af37c0f1e6c)`(self)` | 
`public  `[`calculate_bounds`](#classdtcc__model_1_1pointcloud_1_1_point_cloud_1af2d6c887675af0a675f8929f2d1c8462)`(self)` | Calculate the bounds of the point cloud and update the bounds attribute.
`public  `[`remove_points`](#classdtcc__model_1_1pointcloud_1_1_point_cloud_1ac0f8caa4707e0d4606ed2d0e6c333165)`(self,np.ndarray indices)` | Remove points from the point cloud using the given indices.
`public  `[`from_proto`](#classdtcc__model_1_1pointcloud_1_1_point_cloud_1ae2334dcc7dab3023639ee06cfc6f868f)`(self,Union pb)` | 
`public proto.PointCloud `[`to_proto`](#classdtcc__model_1_1pointcloud_1_1_point_cloud_1a7231000237bc527bd9fe810d06fe3ba7)`(self)` | 
`public  `[`merge`](#classdtcc__model_1_1pointcloud_1_1_point_cloud_1ae524b6b879621b3b3f7668cd347a6148)`(self,other)` | Merge another point cloud into this point cloud.

## Members

#### `public  `[`classification`](#classdtcc__model_1_1pointcloud_1_1_point_cloud_1a2ab366516cf75061dabd18561b4d0354) 

#### `public  `[`points`](#classdtcc__model_1_1pointcloud_1_1_point_cloud_1a18e205e17b1373056341d7bac76e4370) 

#### `public  `[`bounds`](#classdtcc__model_1_1pointcloud_1_1_point_cloud_1afaf17a76a1b06f930916b0fade059ffa) 

#### `public  `[`intensity`](#classdtcc__model_1_1pointcloud_1_1_point_cloud_1ac5a6d2fac81ad6c4ea17dc8d9e332a53) 

#### `public  `[`return_number`](#classdtcc__model_1_1pointcloud_1_1_point_cloud_1a788990249db00505d61a2d1ac7778ab7) 

#### `public  `[`num_returns`](#classdtcc__model_1_1pointcloud_1_1_point_cloud_1a1ae1b78dc7446250b531f924b00e7207) 

#### `public  `[`__str__`](#classdtcc__model_1_1pointcloud_1_1_point_cloud_1a485cffa3907e95cc69542f851a1901da)`(self)` 

#### `public  `[`__len__`](#classdtcc__model_1_1pointcloud_1_1_point_cloud_1a489e3654b0170e1b3c84cf687481a1c1)`(self)` 

#### `public set `[`used_classifications`](#classdtcc__model_1_1pointcloud_1_1_point_cloud_1a714cf3d76ac0d43331f69af37c0f1e6c)`(self)` 

#### `public  `[`calculate_bounds`](#classdtcc__model_1_1pointcloud_1_1_point_cloud_1af2d6c887675af0a675f8929f2d1c8462)`(self)` 

Calculate the bounds of the point cloud and update the bounds attribute.

#### `public  `[`remove_points`](#classdtcc__model_1_1pointcloud_1_1_point_cloud_1ac0f8caa4707e0d4606ed2d0e6c333165)`(self,np.ndarray indices)` 

Remove points from the point cloud using the given indices.

#### `public  `[`from_proto`](#classdtcc__model_1_1pointcloud_1_1_point_cloud_1ae2334dcc7dab3023639ee06cfc6f868f)`(self,Union pb)` 

#### `public proto.PointCloud `[`to_proto`](#classdtcc__model_1_1pointcloud_1_1_point_cloud_1a7231000237bc527bd9fe810d06fe3ba7)`(self)` 

#### `public  `[`merge`](#classdtcc__model_1_1pointcloud_1_1_point_cloud_1ae524b6b879621b3b3f7668cd347a6148)`(self,other)` 

Merge another point cloud into this point cloud.

# namespace `dtcc_model::raster` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`class `[`dtcc_model::raster::Raster`](#classdtcc__model_1_1raster_1_1_raster) | A georeferenced n-dimensional raster of values.

# class `dtcc_model::raster::Raster` 

```
class dtcc_model::raster::Raster
  : public dtcc_model.model.DTCCModel
```  

A georeferenced n-dimensional raster of values.
data is a numpy array of shape (height, width, channels) or (height, width)
if channels is 1.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`data`](#classdtcc__model_1_1raster_1_1_raster_1a7d1cdda99853cd7fe36e799f7828e023) | 
`public  `[`nodata`](#classdtcc__model_1_1raster_1_1_raster_1a065bbf0b1002e1bffbec60e0cc9d08d4) | 
`public  `[`georef`](#classdtcc__model_1_1raster_1_1_raster_1a8c0c298feb3189a772655477545485bb) | 
`public  `[`__str__`](#classdtcc__model_1_1raster_1_1_raster_1a518c8e9b00f8f623051e2200e1a24943)`(self)` | 
`public  `[`shape`](#classdtcc__model_1_1raster_1_1_raster_1a468438aa4267b6c6bd506f296bf71425)`(self)` | 
`public  `[`height`](#classdtcc__model_1_1raster_1_1_raster_1a0f848dc10ccaa88cef991741f24202f1)`(self)` | 
`public  `[`width`](#classdtcc__model_1_1raster_1_1_raster_1a398c8b4ac5567fe381b9776a1532daf8)`(self)` | 
`public  `[`channels`](#classdtcc__model_1_1raster_1_1_raster_1a61cbed28cefc74d363d068a529f96b8f)`(self)` | 
`public  `[`bounds`](#classdtcc__model_1_1raster_1_1_raster_1a0bdefb2cc07b6d2200aa23b23893164c)`(self)` | 
`public  `[`cell_size`](#classdtcc__model_1_1raster_1_1_raster_1ac5901c08153085e6d363518eac889f0b)`(self)` | 
`public  `[`get_value`](#classdtcc__model_1_1raster_1_1_raster_1a167539d67f383f88f2390afd45f1dd64)`(self,float x,float y)` | Get the value at the given coordinate
`public proto.Raster `[`to_proto`](#classdtcc__model_1_1raster_1_1_raster_1a34a2afd5afe08ea05737a95965f1ed3f)`(self)` | 
`public  `[`from_proto`](#classdtcc__model_1_1raster_1_1_raster_1a595392b1b85304f6237ea6fc9713c712)`(self,Union pb)` | 

## Members

#### `public  `[`data`](#classdtcc__model_1_1raster_1_1_raster_1a7d1cdda99853cd7fe36e799f7828e023) 

#### `public  `[`nodata`](#classdtcc__model_1_1raster_1_1_raster_1a065bbf0b1002e1bffbec60e0cc9d08d4) 

#### `public  `[`georef`](#classdtcc__model_1_1raster_1_1_raster_1a8c0c298feb3189a772655477545485bb) 

#### `public  `[`__str__`](#classdtcc__model_1_1raster_1_1_raster_1a518c8e9b00f8f623051e2200e1a24943)`(self)` 

#### `public  `[`shape`](#classdtcc__model_1_1raster_1_1_raster_1a468438aa4267b6c6bd506f296bf71425)`(self)` 

#### `public  `[`height`](#classdtcc__model_1_1raster_1_1_raster_1a0f848dc10ccaa88cef991741f24202f1)`(self)` 

#### `public  `[`width`](#classdtcc__model_1_1raster_1_1_raster_1a398c8b4ac5567fe381b9776a1532daf8)`(self)` 

#### `public  `[`channels`](#classdtcc__model_1_1raster_1_1_raster_1a61cbed28cefc74d363d068a529f96b8f)`(self)` 

#### `public  `[`bounds`](#classdtcc__model_1_1raster_1_1_raster_1a0bdefb2cc07b6d2200aa23b23893164c)`(self)` 

#### `public  `[`cell_size`](#classdtcc__model_1_1raster_1_1_raster_1ac5901c08153085e6d363518eac889f0b)`(self)` 

#### `public  `[`get_value`](#classdtcc__model_1_1raster_1_1_raster_1a167539d67f383f88f2390afd45f1dd64)`(self,float x,float y)` 

Get the value at the given coordinate

#### `public proto.Raster `[`to_proto`](#classdtcc__model_1_1raster_1_1_raster_1a34a2afd5afe08ea05737a95965f1ed3f)`(self)` 

#### `public  `[`from_proto`](#classdtcc__model_1_1raster_1_1_raster_1a595392b1b85304f6237ea6fc9713c712)`(self,Union pb)` 

# namespace `dtcc_model::roadnetwork` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`class `[`dtcc_model::roadnetwork::Road`](#classdtcc__model_1_1roadnetwork_1_1_road) | 
`class `[`dtcc_model::roadnetwork::RoadNetwork`](#classdtcc__model_1_1roadnetwork_1_1_road_network) | 
`class `[`dtcc_model::roadnetwork::RoadType`](#classdtcc__model_1_1roadnetwork_1_1_road_type) | 

# class `dtcc_model::roadnetwork::Road` 

```
class dtcc_model::roadnetwork::Road
  : public dtcc_model.model.DTCCModel
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`road_vertices`](#classdtcc__model_1_1roadnetwork_1_1_road_1a59e5f91a3a240049964a099c3311cec7) | 
`public  `[`road_type`](#classdtcc__model_1_1roadnetwork_1_1_road_1a55a4f88252dfdeebd4c261bd362e4513) | 
`public  `[`road_width`](#classdtcc__model_1_1roadnetwork_1_1_road_1a0d9cf97bd057b6ba64c0c7efc2eaf227) | 
`public  `[`lanes`](#classdtcc__model_1_1roadnetwork_1_1_road_1a6f0ff5db1c265a88f1d4f507f9a66d08) | 
`public  `[`speed_limit`](#classdtcc__model_1_1roadnetwork_1_1_road_1ac27044399185975a3409bef4ff5381d6) | 
`public  `[`road_name`](#classdtcc__model_1_1roadnetwork_1_1_road_1abd99c928e899d66fb0c86316380cad5b) | 
`public  `[`road_id`](#classdtcc__model_1_1roadnetwork_1_1_road_1a7f59b2cdf8b912f4c1d8ad3b271fbc18) | 
`public  `[`__str__`](#classdtcc__model_1_1roadnetwork_1_1_road_1aa528c02afa877bb7c2e6b888c48cec3d)`(self)` | 
`public  `[`length`](#classdtcc__model_1_1roadnetwork_1_1_road_1a3613eba716460b5b335f81651080f5da)`(self)` | 
`public proto.Road `[`to_proto`](#classdtcc__model_1_1roadnetwork_1_1_road_1a5b6675fff254bd10d13c7eb440a6524f)`(self)` | 
`public  `[`from_proto`](#classdtcc__model_1_1roadnetwork_1_1_road_1a72c651b0b330058ed036110d90442b79)`(self,Union pb)` | 

## Members

#### `public  `[`road_vertices`](#classdtcc__model_1_1roadnetwork_1_1_road_1a59e5f91a3a240049964a099c3311cec7) 

#### `public  `[`road_type`](#classdtcc__model_1_1roadnetwork_1_1_road_1a55a4f88252dfdeebd4c261bd362e4513) 

#### `public  `[`road_width`](#classdtcc__model_1_1roadnetwork_1_1_road_1a0d9cf97bd057b6ba64c0c7efc2eaf227) 

#### `public  `[`lanes`](#classdtcc__model_1_1roadnetwork_1_1_road_1a6f0ff5db1c265a88f1d4f507f9a66d08) 

#### `public  `[`speed_limit`](#classdtcc__model_1_1roadnetwork_1_1_road_1ac27044399185975a3409bef4ff5381d6) 

#### `public  `[`road_name`](#classdtcc__model_1_1roadnetwork_1_1_road_1abd99c928e899d66fb0c86316380cad5b) 

#### `public  `[`road_id`](#classdtcc__model_1_1roadnetwork_1_1_road_1a7f59b2cdf8b912f4c1d8ad3b271fbc18) 

#### `public  `[`__str__`](#classdtcc__model_1_1roadnetwork_1_1_road_1aa528c02afa877bb7c2e6b888c48cec3d)`(self)` 

#### `public  `[`length`](#classdtcc__model_1_1roadnetwork_1_1_road_1a3613eba716460b5b335f81651080f5da)`(self)` 

#### `public proto.Road `[`to_proto`](#classdtcc__model_1_1roadnetwork_1_1_road_1a5b6675fff254bd10d13c7eb440a6524f)`(self)` 

#### `public  `[`from_proto`](#classdtcc__model_1_1roadnetwork_1_1_road_1a72c651b0b330058ed036110d90442b79)`(self,Union pb)` 

# class `dtcc_model::roadnetwork::RoadNetwork` 

```
class dtcc_model::roadnetwork::RoadNetwork
  : public dtcc_model.model.DTCCModel
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`vertices`](#classdtcc__model_1_1roadnetwork_1_1_road_network_1ac3f04117a62095c987596c6789aca771) | 
`public  `[`roads`](#classdtcc__model_1_1roadnetwork_1_1_road_network_1aa646c3e77d0e5b38c48d5d20bfd4e363) | 
`public  `[`__str__`](#classdtcc__model_1_1roadnetwork_1_1_road_network_1af405499da01daa7ecb5847671fd31f3b)`(self)` | 
`public proto.RoadNetwork `[`to_proto`](#classdtcc__model_1_1roadnetwork_1_1_road_network_1a536d1d7ee5d18291c010df412e71a056)`(self)` | 
`public  `[`from_proto`](#classdtcc__model_1_1roadnetwork_1_1_road_network_1ac7ff18cbb05087b3b957b9b65eb0ff35)`(self,Union pb)` | 

## Members

#### `public  `[`vertices`](#classdtcc__model_1_1roadnetwork_1_1_road_network_1ac3f04117a62095c987596c6789aca771) 

#### `public  `[`roads`](#classdtcc__model_1_1roadnetwork_1_1_road_network_1aa646c3e77d0e5b38c48d5d20bfd4e363) 

#### `public  `[`__str__`](#classdtcc__model_1_1roadnetwork_1_1_road_network_1af405499da01daa7ecb5847671fd31f3b)`(self)` 

#### `public proto.RoadNetwork `[`to_proto`](#classdtcc__model_1_1roadnetwork_1_1_road_network_1a536d1d7ee5d18291c010df412e71a056)`(self)` 

#### `public  `[`from_proto`](#classdtcc__model_1_1roadnetwork_1_1_road_network_1ac7ff18cbb05087b3b957b9b65eb0ff35)`(self,Union pb)` 

# class `dtcc_model::roadnetwork::RoadType` 

```
class dtcc_model::roadnetwork::RoadType
  : public Enum
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# namespace `dtcc_model::utils` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`coords_to_pb_linear_ring`](#utils_8py_1a1e24de2dc70716efcf6c9df60bd3c1a1)`(coords)`            | 
`public shapely.geometry.Polygon `[`pb_polygon_to_shapely`](#utils_8py_1ae3cac5f1ff0a61419071e30c796b35e2)`(dtcc_pb2.Polygon pb_polygon)`            | 
`public  `[`pb_polygon_from_shapely`](#utils_8py_1a4dd9c96fc6c224a4aad8d11b33ac38bb)`(polygon)`            | 

## Members

#### `public  `[`coords_to_pb_linear_ring`](#utils_8py_1a1e24de2dc70716efcf6c9df60bd3c1a1)`(coords)` 

#### `public shapely.geometry.Polygon `[`pb_polygon_to_shapely`](#utils_8py_1ae3cac5f1ff0a61419071e30c796b35e2)`(dtcc_pb2.Polygon pb_polygon)` 

#### `public  `[`pb_polygon_from_shapely`](#utils_8py_1a4dd9c96fc6c224a4aad8d11b33ac38bb)`(polygon)` 

Generated by [Moxygen](https://sourcey.com/moxygen)