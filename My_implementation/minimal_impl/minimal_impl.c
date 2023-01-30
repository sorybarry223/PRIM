#include <linux/module.h>
#include <linux/kernel.h> 
#include <linux/init.h>
#include <linux/io.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Sory BARRY");
MODULE_DESCRIPTION("A simple example Linux module to retrieve the APIC base.");
MODULE_VERSION("0.01");


static int __init lkm_base_init(void) {

    volatile unsigned char* local_apic = ioremap_cache(0xfee00000, 0x1000);
    //pr_info("APIC MMIO region: 0x%lx\n", (unsigned long)local_apic);
    
    printk(KERN_INFO "APIC MMIO region: 0x%lx\n", (unsigned long)local_apic);
    iounmap((void *)((unsigned long)local_apic));
    

    return 0;
}

static void __exit lkm_base_exit(void) {
    printk(KERN_INFO "Adieu monde cruel..\n");
}

module_init(lkm_base_init);
module_exit(lkm_base_exit);