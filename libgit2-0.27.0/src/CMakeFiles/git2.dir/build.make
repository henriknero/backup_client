# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/henrik/Programming/backup_client/libgit2-0.27.0

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/henrik/Programming/backup_client/libgit2-0.27.0

# Include any dependencies generated for this target.
include src/CMakeFiles/git2.dir/depend.make

# Include the progress variables for this target.
include src/CMakeFiles/git2.dir/progress.make

# Include the compile flags for this target's objects.
include src/CMakeFiles/git2.dir/flags.make

# Object files for target git2
git2_OBJECTS =

# External object files for target git2
git2_EXTERNAL_OBJECTS = \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/annotated_commit.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/apply.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/attr.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/attr_file.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/attrcache.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/blame.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/blame_git.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/blob.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/branch.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/buf_text.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/buffer.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/cache.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/checkout.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/cherrypick.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/clone.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/commit.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/commit_list.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/config.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/config_cache.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/config_file.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/config_parse.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/crlf.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/date.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/delta.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/describe.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/diff.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/diff_driver.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/diff_file.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/diff_generate.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/diff_parse.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/diff_print.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/diff_stats.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/diff_tform.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/diff_xdiff.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/errors.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/fetch.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/fetchhead.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/filebuf.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/fileops.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/filter.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/fnmatch.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/global.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/graph.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/hash.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/hashsig.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/ident.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/idxmap.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/ignore.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/index.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/indexer.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/iterator.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/merge.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/merge_driver.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/merge_file.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/message.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/mwindow.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/netops.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/notes.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/object.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/object_api.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/odb.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/odb_loose.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/odb_mempack.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/odb_pack.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/offmap.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/oid.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/oidarray.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/oidmap.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/pack-objects.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/pack.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/parse.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/patch.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/patch_generate.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/patch_parse.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/path.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/pathspec.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/pool.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/posix.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/pqueue.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/proxy.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/push.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/rebase.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/refdb.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/refdb_fs.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/reflog.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/refs.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/refspec.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/remote.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/repository.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/reset.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/revert.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/revparse.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/revwalk.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/settings.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/sha1_lookup.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/signature.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/sortedcache.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/stash.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/status.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/strmap.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/submodule.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/sysdir.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/tag.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/thread-utils.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/trace.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/trailer.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/transaction.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/transport.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/tree-cache.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/tree.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/tsort.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/util.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/varint.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/vector.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/worktree.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/zstream.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/streams/curl.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/streams/openssl.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/streams/socket.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/streams/stransport.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/streams/tls.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/transports/auth.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/transports/auth_negotiate.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/transports/cred.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/transports/cred_helpers.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/transports/git.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/transports/http.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/transports/local.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/transports/smart.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/transports/smart_pkt.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/transports/smart_protocol.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/transports/ssh.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/transports/winhttp.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/xdiff/xdiffi.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/xdiff/xemit.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/xdiff/xhistogram.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/xdiff/xmerge.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/xdiff/xpatience.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/xdiff/xprepare.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/xdiff/xutils.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/unix/map.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/unix/realpath.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/hash/sha1dc/sha1.c.o" \
"/home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2internal.dir/hash/sha1dc/ubc_check.c.o"

libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/annotated_commit.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/apply.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/attr.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/attr_file.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/attrcache.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/blame.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/blame_git.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/blob.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/branch.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/buf_text.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/buffer.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/cache.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/checkout.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/cherrypick.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/clone.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/commit.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/commit_list.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/config.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/config_cache.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/config_file.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/config_parse.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/crlf.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/date.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/delta.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/describe.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/diff.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/diff_driver.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/diff_file.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/diff_generate.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/diff_parse.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/diff_print.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/diff_stats.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/diff_tform.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/diff_xdiff.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/errors.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/fetch.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/fetchhead.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/filebuf.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/fileops.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/filter.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/fnmatch.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/global.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/graph.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/hash.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/hashsig.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/ident.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/idxmap.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/ignore.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/index.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/indexer.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/iterator.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/merge.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/merge_driver.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/merge_file.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/message.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/mwindow.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/netops.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/notes.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/object.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/object_api.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/odb.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/odb_loose.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/odb_mempack.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/odb_pack.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/offmap.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/oid.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/oidarray.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/oidmap.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/pack-objects.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/pack.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/parse.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/patch.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/patch_generate.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/patch_parse.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/path.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/pathspec.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/pool.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/posix.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/pqueue.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/proxy.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/push.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/rebase.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/refdb.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/refdb_fs.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/reflog.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/refs.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/refspec.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/remote.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/repository.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/reset.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/revert.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/revparse.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/revwalk.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/settings.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/sha1_lookup.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/signature.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/sortedcache.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/stash.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/status.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/strmap.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/submodule.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/sysdir.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/tag.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/thread-utils.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/trace.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/trailer.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/transaction.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/transport.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/tree-cache.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/tree.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/tsort.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/util.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/varint.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/vector.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/worktree.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/zstream.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/streams/curl.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/streams/openssl.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/streams/socket.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/streams/stransport.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/streams/tls.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/transports/auth.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/transports/auth_negotiate.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/transports/cred.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/transports/cred_helpers.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/transports/git.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/transports/http.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/transports/local.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/transports/smart.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/transports/smart_pkt.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/transports/smart_protocol.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/transports/ssh.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/transports/winhttp.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/xdiff/xdiffi.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/xdiff/xemit.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/xdiff/xhistogram.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/xdiff/xmerge.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/xdiff/xpatience.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/xdiff/xprepare.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/xdiff/xutils.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/unix/map.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/unix/realpath.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/hash/sha1dc/sha1.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2internal.dir/hash/sha1dc/ubc_check.c.o
libgit2.so.0.27.0: src/CMakeFiles/git2.dir/build.make
libgit2.so.0.27.0: /usr/lib/x86_64-linux-gnu/libssl.so
libgit2.so.0.27.0: /usr/lib/x86_64-linux-gnu/libcrypto.so
libgit2.so.0.27.0: /usr/lib/x86_64-linux-gnu/libhttp_parser.so
libgit2.so.0.27.0: /usr/lib/x86_64-linux-gnu/libz.so
libgit2.so.0.27.0: src/CMakeFiles/git2.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/henrik/Programming/backup_client/libgit2-0.27.0/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Linking C shared library ../libgit2.so"
	cd /home/henrik/Programming/backup_client/libgit2-0.27.0/src && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/git2.dir/link.txt --verbose=$(VERBOSE)
	cd /home/henrik/Programming/backup_client/libgit2-0.27.0/src && $(CMAKE_COMMAND) -E cmake_symlink_library ../libgit2.so.0.27.0 ../libgit2.so.27 ../libgit2.so

libgit2.so.27: libgit2.so.0.27.0
	@$(CMAKE_COMMAND) -E touch_nocreate libgit2.so.27

libgit2.so: libgit2.so.0.27.0
	@$(CMAKE_COMMAND) -E touch_nocreate libgit2.so

# Rule to build all files generated by this target.
src/CMakeFiles/git2.dir/build: libgit2.so

.PHONY : src/CMakeFiles/git2.dir/build

src/CMakeFiles/git2.dir/requires:

.PHONY : src/CMakeFiles/git2.dir/requires

src/CMakeFiles/git2.dir/clean:
	cd /home/henrik/Programming/backup_client/libgit2-0.27.0/src && $(CMAKE_COMMAND) -P CMakeFiles/git2.dir/cmake_clean.cmake
.PHONY : src/CMakeFiles/git2.dir/clean

src/CMakeFiles/git2.dir/depend:
	cd /home/henrik/Programming/backup_client/libgit2-0.27.0 && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/henrik/Programming/backup_client/libgit2-0.27.0 /home/henrik/Programming/backup_client/libgit2-0.27.0/src /home/henrik/Programming/backup_client/libgit2-0.27.0 /home/henrik/Programming/backup_client/libgit2-0.27.0/src /home/henrik/Programming/backup_client/libgit2-0.27.0/src/CMakeFiles/git2.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/CMakeFiles/git2.dir/depend
