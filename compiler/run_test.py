import subprocess
import sys
import filecmp


def run_single_test(test, dir):
    print "Running " + test
    if dir == 1:
        test = "tests/" + test

    f1 = open("out/python.txt", "w")
    f2 = open("out/compiler.txt", "w")

    # execute normal python
    exit_st_python = subprocess.call(["python", test], stdout=f1, stderr=f1)

    # execute our compiler
    exit_st_compiler = subprocess.call(["python", "compile.py", test], stderr=f2)

    output = 1

    # compare output when both files output ok
    if exit_st_compiler == 0 & exit_st_python == 0:
        subprocess.call(["gcc", "build/asmbl.s", "-m32", "runtim.c", "-o", "test"])
        subprocess.call(["./test"], stdout=f2)
        compare = filecmp.cmp('out/python.txt', 'out/compiler.txt')

        if compare:
            print test + " passed"
            output = 0
        else:
            print test + " failed"

    # if both compilers throw error, test is passed
    elif exit_st_compiler == 1 & exit_st_python == 1:
        print test + " passed"
        output = 0

    # if the compilers status exit are different, test is failed
    else:
        print test + " failed"

    return output


if __name__ == '__main__':
    test = sys.argv[1]
    run_single_test(test,0)