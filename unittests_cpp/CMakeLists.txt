
set(PROGRAM run-unittests)
add_executable(${PROGRAM} ${PROGRAM}.cpp)
target_link_libraries(${PROGRAM} dtccproto ${PROTOBUF_LIBRARY} Threads::Threads)
install(TARGETS ${PROGRAM} DESTINATION ${CMAKE_SOURCE_DIR}/unittests_cpp/bin)

