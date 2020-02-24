Last login: Sun Feb 23 00:19:55 on ttys002
stc-mbpro16:assn03 labuser$ #! /bash/bin
stc-mbpro16:assn03 labuser$ #assn03-1
stc-mbpro16:assn03 labuser$ #for i in TR-{808..8008}; do echo $i;done
stc-mbpro16:assn03 labuser$ #assn03-2
stc-mbpro16:assn03 labuser$ #alias l="less"
stc-mbpro16:assn03 labuser$ #assn03-3
stc-mbpro16:assn03 labuser$ #for i in *.fasta; do echo $i;done | wc -l
stc-mbpro16:assn03 labuser$ #assn03-4
stc-mbpro16:assn03 labuser$ #for i in *.tre; do echo $i;done | wc -l
stc-mbpro16:assn03 labuser$ #assn03-5
stc-mbpro16:assn03 labuser$ #for i in *.sched; do echo $i;done | wc -l
stc-mbpro16:assn03 labuser$ #assn03-6
stc-mbpro16:assn03 labuser$ #for i in *.tre; do echo $i;done >tree_fasta.txt
stc-mbpro16:assn03 labuser$ #for i in *.fasta; do echo $i;done >>tree_fasta.txt
stc-mbpro16:assn03 labuser$ #cut -c -9 tree_fasta.txt > tree_fasta_num.txt|sort -n tree_fasta_num.txt| uniq -u| wc -l
stc-mbpro16:assn03 labuser$ #assn03-7
stc-mbpro16:assn03 labuser$ 




































