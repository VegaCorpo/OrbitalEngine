# Concatenates the compile_commands.json arrays of every component into a
# single database. Run in script mode:
#   cmake -DOUT=<file> "-DINPUTS=<a.json;b.json>" -P merge_compile_commands.cmake
#
# Missing inputs are skipped, so a partially built tree still yields a valid
# database rather than failing the build.

set(entries "")

foreach(input IN LISTS INPUTS)
    if(NOT EXISTS "${input}")
        continue()
    endif()

    file(READ "${input}" content)
    string(STRIP "${content}" content)
    string(REGEX REPLACE "^\\[" "" content "${content}")
    string(REGEX REPLACE "\\]$" "" content "${content}")
    string(STRIP "${content}" content)

    if(content STREQUAL "")
        continue()
    endif()

    if(NOT entries STREQUAL "")
        string(APPEND entries ",\n")
    endif()
    string(APPEND entries "${content}")
endforeach()

file(WRITE "${OUT}" "[\n${entries}\n]\n")
