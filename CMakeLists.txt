cmake_minimum_required(VERSION 3.14)

project(Orbital-Engine
        VERSION 0.0.0
        DESCRIPTION "Astrophysics Simulator"
        LANGUAGES CXX
)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_INTERPROCEDURAL_OPTIMIZATION ON)
set(CMAKE_CXX_STANDARD 20 CACHE STRING "C++ standard")
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CPM_USE_LOCAL_PACKAGES ON)

include(cmake/CPM.cmake)
CPMUsePackageLock(package-lock.cmake)
CPMGetPackage("Eigen")
CPMGetPackage("ImGui")

add_library(imgui_core STATIC
    ${CPM_PACKAGE_imgui_SOURCE_DIR}/imgui.cpp
    ${CPM_PACKAGE_imgui_SOURCE_DIR}/imgui_draw.cpp
    ${CPM_PACKAGE_imgui_SOURCE_DIR}/imgui_tables.cpp
    ${CPM_PACKAGE_imgui_SOURCE_DIR}/imgui_widgets.cpp
)

target_include_directories(imgui_core PUBLIC ${CPM_PACKAGE_imgui_SOURCE_DIR})

set_target_properties(imgui_core PROPERTIES POSITION_INDEPENDENT_CODE ON)

if (NOT CMAKE_BUILD_TYPE)
    if (MSVC)
    	add_compile_definitions(RAYLIB_CPP_NO_MATH)
    endif()
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

add_subdirectory(Physics)
add_subdirectory(Core)
add_subdirectory(Renderer)
add_subdirectory(UI)
