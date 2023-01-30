#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>
#include <asm/msr.h>
#include <asm/msr-index.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Sory BARRY");
MODULE_DESCRIPTION("A simple example Linux module to retrieve the APIC base.");
MODULE_VERSION("0.01");

static unsigned long long apic_base;

static int __init lkm_base_init(void) {

    rdmsrl(MSR_IA32_APIC_BASE, apic_base);
    printk(KERN_INFO "APIC base address: 0x%llx\n", apic_base & 0xFFFFFFFFFFFFF000ull);

    return 0;
}

static void __exit lkm_base_exit(void) {
    printk(KERN_INFO "Goodbye, World!\n");
}

module_init(lkm_base_init);
module_exit(lkm_base_exit);