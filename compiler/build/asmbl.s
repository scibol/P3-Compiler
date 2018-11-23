.section	__TEXT,__text,regular,pure_instructions
                 .macosx_version_min 10, 13
                 .globl	_main
                 .p2align	4, 0x90
                 _main:                                  ## @main
                 ## BB#0:
                 pushl	%ebp
                 movl	%esp, %ebp
                 subl	$24, %esp
                 xorl	%eax, %eax
                 movl	$0, -4(%ebp)
    movl    $False, %eax
    movl    $True, %ecx
    movl    %ecx, %eax
    movl    $True, %eax
xorl %eax, %eax 
                addl     $24, %esp
                popl     %ebp
                retl


.subsections_via_symbols