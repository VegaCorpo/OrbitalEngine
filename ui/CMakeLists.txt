cmake_minimum_required(VERSION 3.14)

include(FetchContent)
FetchContent_GetProperties(imgui)

file(GLOB_RECURSE src CONFIGURE_DEPENDS "*.cpp")
file(GLOB_RECURSE common_src CONFIGURE_DEPENDS "${CMAKE_SOURCE_DIR}/common/src/*.cpp")

set(IMGUI_SOURCES
    ${imgui_SOURCE_DIR}/imgui.cpp
    ${imgui_SOURCE_DIR}/imgui_draw.cpp
    ${imgui_SOURCE_DIR}/imgui_tables.cpp
    ${imgui_SOURCE_DIR}/imgui_widgets.cpp
)

add_library(orbital_ui SHARED ${src} ${common_src} ${IMGUI_SOURCES})

# target_link_libraries(orbital_ui PRIVATE)

target_include_directories(orbital_ui PRIVATE
    ${imgui_SOURCE_DIR}
    ${CMAKE_SOURCE_DIR}/common/include
    ${CMAKE_CURRENT_SOURCE_DIR}
)

if(WIN32)
    target_compile_definitions(orbital_ui PRIVATE NOGDI NOUSER WIN32_LEAN_AND_MEAN)

    set(PROJECT_DIR ${CMAKE_SOURCE_DIR})
    set(BUILD_DIR ${CMAKE_BINARY_DIR})
    set(UI_DIR "${BUILD_DIR}/ui/${CMAKE_BUILD_TYPE}")

    set(TARGET_DIR "${PROJECT_DIR}")
endif()
