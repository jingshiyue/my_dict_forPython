#include <stdio.h>
#include <stdlib.h>
//#include "../../include/myfun.h"

int m = 1;
#define MON m
#define MO (2)

#define ORAVERNUM(major, minor, update, patch, port_update) \
    (((major) >= 18) ? (((major) << 24) | ((minor) << 16) | ((update) << 12) | ((patch) << 4) | (port_update)) \
                     : (((major) << 24) | ((minor) << 20) | ((update) << 12) | ((patch) << 8) | (port_update)))


int f;


#define Add_H


int main()
{

	printf("%d", f);
	printf("%d", MO);
	return 0;
}