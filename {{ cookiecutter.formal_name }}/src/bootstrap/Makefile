
CFLAGS=$(shell /app/bin/python3-config --cflags)
LDFLAGS=$(shell /app/bin/python3-config --ldflags)

all: helloworld

helloworld: main.c
	gcc -o helloworld $^ $(CFLAGS) $(LDFLAGS) -lpython{{ '.'.join(cookiecutter.python_version.split('.')[:2]) }}

clean:
	rm -f helloworld

install:
	cp helloworld /app/bin/helloworld

.PHONY: all clean install

