#nombre del ejecutable
TARGET1 = client
#todos los objetos de los que dependa el ejecutable
OBJS1 = socket_comm.o
#flags del compilador
CFLAGS = -Wall

.PHONY: all
all: $(TARGET1) $(TARGET2)

#link del target con todos los objetos
#$@ hace referencia a TARGET1
$(TARGET1) : $(OBJS1)
	gcc $(OBJS1) -o $@ $(CFLAGS)


#regla para compilar cada objeto
#ejemplo: gcc -c -Wall main.c -o main.o
#$< hace referencia a %.c
#$@ hace referencia a %.o
%.o : %.c
	gcc -c $< -o $@ $(CFLAGS)