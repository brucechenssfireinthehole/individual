cmake_minimum_required(VERSION 2.8)  
#project name
PROJECT(test_math)
#head file path
INCLUDE_DIRECTORIES(
include
)
#source directory
AUX_SOURCE_DIRECTORY(src DIR_SRCS)
#set environment variable
SET(TEST_MATH
${DIR_SRCS}
)
#set extern libraries
SET(LIBRARIES
libm.so
)
#add executable file
ADD_EXECUTABLE(main ${TEST_MATH})
#add link library
TARGET_LINK_LIBRARIES(main ${LIBRARIES})
 

