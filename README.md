# cython_tutorial
Tutorial codes for Cython

## Common cdef Declarations

| CDEF DECLARATION          	| MEANING                        	|
|---------------------------	|--------------------------------	|
| cdef int i, j, k          	| declare multiple C integers    	|
| cdef char *s              	| declare a C-type string        	|
| cdef float x = 1.0        	| declare and init a C float     	|
| cdef list names           	| statically typed Python list   	|
| cdef dict name_to_id = {} 	| declare and init a Python dict 	|
| cdef object a             	| a reference counted object     	|
| ctypedef long time_t        | typdef long as time_t         	|

