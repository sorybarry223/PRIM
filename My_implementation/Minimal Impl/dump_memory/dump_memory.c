#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/mm.h>

#define START_ADDRESS 0xfee00000
#define END_ADDRESS 0xfee0ffff

static int __init dump_memory_init(void)
{
    unsigned long address;
    unsigned char *ptr;

    for (address = START_ADDRESS; address <= END_ADDRESS; address++) {
        ptr = (unsigned char *)address;
        printk("0x%lx: 0x%x\n", address, *ptr);
    }

    return 0;
}

static void __exit dump_memory_exit(void)
{
    printk("Exiting dump_memory module\n");
}

module_init(dump_memory_init);
module_exit(dump_memory_exit);

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Sory BARRY");
MODULE_DESCRIPTION("A simple example Linux module to retrieve the APIC base.");
MODULE_VERSION("0.01");