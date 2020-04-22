Last login: Tue Feb  4 21:36:00 on ttys000
stc-mbpro01:watermelon_files labuser$ #! /bin/bash
stc-mbpro01:watermelon_files labuser$ #assn01-1
stc-mbpro01:watermelon_files labuser$ cd ~/Desktop/watermelon_files/watermelon_nt; find nad*; cd ~/Desktop/watermelon_files/watermelon_aa;find nad*
nad1.fasta
nad2.fasta
nad3.fasta
nad4.fasta
nad4L.fasta
nad5.fasta
nad6.fasta
nad7.fasta
nad9.fasta
nad1.fasta
nad2.fasta
nad3.fasta
nad4.fasta
nad4L.fasta
nad5.fasta
nad6.fasta
nad7.fasta
nad9.fasta
stc-mbpro01:watermelon_aa labuser$ cd ..
stc-mbpro01:watermelon_files labuser$ #assn01-2
stc-mbpro01:watermelon_files labuser$ top
stc-mbpro01:watermelon_files labuser$ #I used the 'top' command.
stc-mbpro01:watermelon_files labuser$ #The command uses between 0.24% and 2.39% of the CPU.
stc-mbpro01:watermelon_files labuser$ #MemRegions: 82443 total, 1546M resident, 88M private, 470M shared. PhysMem: 5706M used (1520M wired), 2485M unused.
stc-mbpro01:watermelon_files labuser$ #I got those numbers in the summary of the 'top' command.
stc-mbpro01:watermelon_files labuser$ #assn01-3
stc-mbpro01:watermelon_files labuser$ grep misc_feature watermelon.gff> IR_prep; sort -k5gr IR_prep> IR_regions.gff
stc-mbpro01:watermelon_files labuser$ #assn01-4
stc-mbpro01:watermelon_files labuser$ wc nonIR_regions.gff; wc IR_regions.gff
     107    1975   10624 nonIR_regions.gff
      37     811    5347 IR_regions.gff
stc-mbpro01:watermelon_files labuser$ #More chloroplast fragments seem to come from outside of the IR region.
stc-mbpro01:watermelon_files labuser$ #assn01-5
stc-mbpro01:watermelon_files labuser$ for CAT in genes.fsa; do grep GGATCC $CAT>>BamHi; done
stc-mbpro01:watermelon_files labuser$ for CAT in BamHi; do grep -v GAATTC $CAT>>BamHi_sans; done
stc-mbpro01:watermelon_files labuser$ less BamHi_sans 
stc-mbpro01:watermelon_files labuser$ for CAT in genes.fsa; do grep GGATCC $CAT>>BamHi; done
stc-mbpro01:watermelon_files labuser$ for CAT in genes.fsa; do grep GGATCC $CAT>BamHi; done
stc-mbpro01:watermelon_files labuser$ for CAT in BamHi; do grep -v GAATTC $CAT>BamHi_sans; done
stc-mbpro01:watermelon_files labuser$ less BamHi_sans 
stc-mbpro01:watermelon_files labuser$ #assn01-6
stc-mbpro01:watermelon_files labuser$ cd ~/Desktop/example_files
stc-mbpro01:example_files labuser$ sed -n -e '500,1000p' shaver_etal.csv>shaver_cut
stc-mbpro01:example_files labuser$ #assn01-7
stc-mbpro01:example_files labuser$ sort -k2,2r -k3,3 fruit.txt
5 pear FL
3 pear IL
2 pear OH
4 apple FL
6 apple MI
1 apple OH
stc-mbpro01:example_files labuser$ 
