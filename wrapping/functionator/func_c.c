//Just a demo program to test wrapping of C code using Cython
#include "func.h"
#include <stdio.h>
#include <string.h>

int circle(int rad){
	if(rad < 0){
    return -1;
  }
  else{
    return 3.14*rad*rad;
  }
}

int square(int side){
  if(side < 0){
    return -1;
  }
  else{
    return side*side;
  }
}