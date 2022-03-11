#
# This spec file is read by gcj when linking.
# It is only used by the testing harnesses (in libjava and gdb).
#
%rename lib liborig2
*lib: -L/c/Users/bp1user.SYDGRAM/Downloads/PortableGit/gcj/.libs -rpath /c/Users/bp1user.SYDGRAM/Downloads/PortableGit/gcj/.libs -L/c/Users/bp1user.SYDGRAM/Downloads/PortableGit/gcj/boehm-gc/.libs -rpath /c/Users/bp1user.SYDGRAM/Downloads/PortableGit/gcj/boehm-gc/.libs  %(liborig2)

