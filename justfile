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
    # cp {{ OUTDIR }}/core/orbital-engine .
    cp {{ OUTDIR }}/compile_commands.json .

clean:
    rm -rf {{ OUTDIR }}
    rm -rf {{ DEBUG_DIR }}
    rm -f orbital
    rm -f orbital_server

purge: clean
    rm -rf .cpm_cache

re: clean release
