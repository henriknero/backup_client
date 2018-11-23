#ifndef INCLUDE_features_h__
#define INCLUDE_features_h__

/* #undef GIT_DEBUG_POOL */
/* #undef GIT_TRACE */
#define GIT_THREADS 1
/* #undef GIT_MSVC_CRTDBG */

#define GIT_ARCH_64 1
/* #undef GIT_ARCH_32 */

/* #undef GIT_USE_ICONV */
#define GIT_USE_NSEC 1
#define GIT_USE_STAT_MTIM 1
/* #undef GIT_USE_STAT_MTIMESPEC */
/* #undef GIT_USE_STAT_MTIME_NSEC */
#define GIT_USE_FUTIMENS 1
/* #undef GIT_USE_REGCOMP_L */

#define GIT_SSH 1
#define GIT_SSH_MEMORY_CREDENTIALS 1

/* #undef GIT_GSSAPI */
/* #undef GIT_WINHTTP */
#define GIT_CURL 1

#define GIT_HTTPS 1
#define GIT_OPENSSL 1
/* #undef GIT_SECURE_TRANSPORT */

#define GIT_SHA1_COLLISIONDETECT 1
/* #undef GIT_SHA1_WIN32 */
/* #undef GIT_SHA1_COMMON_CRYPTO */
/* #undef GIT_SHA1_OPENSSL */

#endif
