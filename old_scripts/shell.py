import os
from os import path
import time 

def shellpath():

    path = os.getcwd()
    path1 = os.path.join(path,"weather_forecast")
    path2 = os.path.join(path1,"weather_forecast")
    
    print(f'path2: {path2}')
    chdir = os.chdir(path2)
    path_file = os.path.join(path2,"weather.json")
    print(path_file)
    for root, dirs, files in os.walk(".", topdown=False):
        for file_name in files:
            #print(os.path.join(root, file_name))
            if "weather.json" == file_name:
                print(True)
                os.remove(path_file)
                print("Arquivo Removido")
            else:
                print("Criando weather.json")
    os.system("scrapy crawl weather -o weather.json")
    
    #os.system("cls")


shellpath()
'''
dir = dir(os)
#print(dir)

['DirEntry', 'F_OK', 'MutableMapping', 'O_APPEND', 'O_BINARY', 'O_CREAT', 
'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL', 
'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC', 'O_WRONLY', 'P_DETACH', 
'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 
'P_WAIT', 'PathLike', 'R_OK', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'TMP_MAX', 
'W_OK', 'X_OK', '_AddedDllDirectory', '_Environ', '__all__', '__builtins__', 
'__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', 
'__spec__', '_check_methods', '_execvpe', '_exists', '_exit', '_fspath', 
'_get_exports_list', '_putenv', '_unsetenv', '_wrap_close', 'abc', 'abort', 
'access', 'add_dll_directory', 'altsep', 'chdir', 'chmod', 'close', 'closerange', 
'cpu_count', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 
'environ', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 
'execvp', 'execvpe', 'extsep', 'fdopen', 'fsdecode', 'fsencode', 'fspath', 
'fstat', 'fsync', 'ftruncate', 'get_exec_path', 'get_handle_inheritable', 
'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getenv', 
'getlogin', 'getpid', 'getppid', 'isatty', 'kill', 'linesep', 'link', 
'listdir', 'lseek', 'lstat', 'makedirs', 'mkdir', 'name', 'open', 
'pardir', 'path', 'pathsep', 'pipe', 'popen', 'putenv', 'read', 
'readlink', 'remove', 'removedirs', 'rename', 'renames', 'replace', 
'rmdir', 'scandir', 'sep', 'set_handle_inheritable', 'set_inheritable', 
'spawnl', 'spawnle', 'spawnv', 'spawnve', 'st', 'startfile', 'stat', 
'stat_result', 'statvfs_result', 'strerror', 'supports_bytes_environ', 
'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 
'supports_follow_symlinks', 'symlink', 'sys', 'system', 'terminal_size', 
'times', 'times_result', 'truncate', 'umask', 'uname_result', 
'unlink', 'urandom', 'utime', 'waitpid', 'walk', 'write']
'''