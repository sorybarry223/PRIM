#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    FILE *fp;
    char output[1000];
    char *line;

    fp = popen("sudo dmesg | grep -i \"APIC\"", "r");
    if (fp == NULL) {
        printf("Failed to run command\n");
        exit(1);
    }

    while (fgets(output, sizeof(output) - 1, fp) != NULL) {
        line = strstr(output, "APIC");
        if (line != NULL) {
            printf("%s", output);
        }
    }

    pclose(fp);
    return 0;
}