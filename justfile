set export

OUTDIR := env("BUILD_OUT", "build")
DEBUG_DIR := env("DEBUG_DIR", "cmake-build-cache")
CPM_SOURCE_CACHE := env("CPM_SOURCE_CACHE", ".cpm_cache")

release: (_build "Release")

debug: (_build "Debug")

asan: (_build "Asan")

_build type extra='':
    cmake -S . -B {{ OUTDIR }} -DCMAKE_BUILD_TYPE={{ type }} {{extra}}
    cmake --build {{ OUTDIR }} -j {{ num_cpus() }}

    mkdir -p plugins/physics
    mkdir -p plugins/ui
    mkdir -p plugins/render

    cp {{ OUTDIR }}/compile_commands.json .
    cp {{ OUTDIR }}/core/orbital-engine .
    cp {{ OUTDIR }}/physics/liborbital_physics.* plugins/physics
    cp {{ OUTDIR }}/render/liborbital_render.* plugins/render
    cp {{ OUTDIR }}/ui/liborbital_ui.* plugins/ui

clean:
    rm -rf {{ OUTDIR }}
    rm -rf {{ DEBUG_DIR }}
    rm -f orbital-engine
    find . -name "*.so" -type f -delete
    find . -name "*.dll" -type f -delete

purge: clean
    rm -rf .cpm_cache

re: clean release
