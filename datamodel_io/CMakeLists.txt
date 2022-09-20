set(LIBRARY generate_protobuf)

link_libraries(dtccproto ${PROTOBUF_LIBRARY} Threads::Threads)
pybind11_add_module(${LIBRARY} cpp/${LIBRARY}.cpp)
set_target_properties(${LIBRARY} PROPERTIES LIBRARY_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/datamodel_io/pblib)
