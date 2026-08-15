cmake_minimum_required(VERSION 3.14)

project(Orbital-Engine
        VERSION 0.0.0
        DESCRIPTION "Astrophysics Simulator"
        LANGUAGES CXX
)

# This file only orchestrates: every component is configured as its own CMake
# project (see orbital_component below), so each one resolves its own
# package-lock.cmake independently. Nothing is declared or linked here.
set(CMAKE_CXX_STANDARD 26 CACHE STRING "C++ standard")
set(CMAKE_CXX_STANDARD_REQUIRED ON)

if (NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE "Release")
endif()

if (CMAKE_BUILD_TYPE STREQUAL "Debug")
    if (MSVC)
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /Zi /Od")
        set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} /DEBUG")
    else()
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g3 -O0")
        set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -g3 -O0")
    endif()
endif()

if (CMAKE_BUILD_TYPE STREQUAL "Asan")
    if (MSVC)
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /Zi /Od")
        set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} /DEBUG")
    else()
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g3 -O0 -fsanitize=address")
        set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -g3 -O0 -fsanitize=address")
    endif()
endif()

include(ExternalProject)

# Shared so every component reuses the same downloads instead of one cache per
# sub-build. Must be absolute: the sub-cmake runs from its own binary dir, so a
# relative path would resolve under build/<Component>/.
set(ORBITAL_CPM_CACHE "${CMAKE_CURRENT_SOURCE_DIR}/.cpm_cache")

# Toolchain and build settings are forwarded; dependencies are not. Drop
# CMAKE_CXX_STANDARD here to let each component fall back to the standard
# declared in its own CMakeLists (Physics 23, Inputs 20).
set(ORBITAL_FORWARDED_ARGS
    -DCMAKE_BUILD_TYPE=${CMAKE_BUILD_TYPE}
    -DCMAKE_CXX_COMPILER=${CMAKE_CXX_COMPILER}
    -DCMAKE_CXX_STANDARD=${CMAKE_CXX_STANDARD}
    -DCMAKE_CXX_STANDARD_REQUIRED=${CMAKE_CXX_STANDARD_REQUIRED}
    -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
    -DCPM_SOURCE_CACHE=${ORBITAL_CPM_CACHE}
    "-DCMAKE_CXX_FLAGS=${CMAKE_CXX_FLAGS}"
    "-DCMAKE_EXE_LINKER_FLAGS=${CMAKE_EXE_LINKER_FLAGS}"
)

# BINARY_DIR is kept at build/<Component> so the artifact paths used by the
# justfile are unchanged.
function(orbital_component name)
    ExternalProject_Add(${name}
        SOURCE_DIR      ${CMAKE_CURRENT_SOURCE_DIR}/${name}
        BINARY_DIR      ${CMAKE_BINARY_DIR}/${name}
        PREFIX          ${CMAKE_BINARY_DIR}/external/${name}
        CMAKE_ARGS      ${ORBITAL_FORWARDED_ARGS}
        BUILD_ALWAYS    TRUE
        INSTALL_COMMAND ""
        USES_TERMINAL_CONFIGURE TRUE
        USES_TERMINAL_BUILD     TRUE
    )
endfunction()

set(ORBITAL_COMPONENTS Core Physics Loader Inputs)
# set(ORBITAL_COMPONENTS ${ORBITAL_COMPONENTS} Renderer UI)

foreach(component IN LISTS ORBITAL_COMPONENTS)
    orbital_component(${component})
    list(APPEND ORBITAL_COMPILE_COMMANDS "${CMAKE_BINARY_DIR}/${component}/compile_commands.json")
endforeach()

# Each component now emits its own compile_commands.json, so the top-level one
# has to be stitched back together for clangd to see the whole tree.
add_custom_target(compile_commands ALL
    COMMAND ${CMAKE_COMMAND}
            -DOUT=${CMAKE_BINARY_DIR}/compile_commands.json
            "-DINPUTS=${ORBITAL_COMPILE_COMMANDS}"
            -P ${CMAKE_CURRENT_SOURCE_DIR}/cmake/merge_compile_commands.cmake
    COMMENT "Merging compile_commands.json from all components"
    VERBATIM
)
add_dependencies(compile_commands ${ORBITAL_COMPONENTS})
