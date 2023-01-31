CC=gcc
CFLAGS=-Wall

all: apic_base_address

apic_base_address: apic_base_address.c
	$(CC) $(CFLAGS) -o apic_base_address apic_base_address.c

run: apic_base_address
	./apic_base_address

clean:
	rm -f apic_base_address
