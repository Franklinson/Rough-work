#include <stdio.h>
#include <stdarg.h>

int sum_them_all(const unsigned int n, ...){

    va_list do;

    unsigned int i = 0;
    int sum = 0;

    if (n == 0)
        return (0);


    va_start (do, n);

    for (; i < n; i++)
        sum += va_arg(do, int)

    va_end(do);
    return (d0);


}