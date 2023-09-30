# C / C++ Custom Auto-grader for Coursera(c) Labs.

![Static Badge](https://img.shields.io/badge/License-BSD--2--Clause-blue)

## Features:

* Automatic grading of C / C++ Programming Assignments.

* Multiple parts are supported.

* Test cases based fractional grading.

* Maximum control over building (Can use `make` if needed).

* It can test console output, file output, functions and classes. 

* Token-based text matching (Details are given below) and feedback.

* Adequate auto-grading feedback to the learners.

* Detailed logs for the administrator.

* Supports multi-file submission grading via automatic archive decompression.

* Supports grading programs with input via command line, standard input or files.

* Supports checking program output to standard output and files.

* Supports removing main() function from user submissions.

## How it works:

1. The auto-grader runs on a custom docker container instance including `python3`, `gcc`, `g++` and `make`.

2. It copies the submission file to the build directory and decompresses it if it is in a known archive format (zip, tar, etc.), The submission file is, by default, saved in the `/shared/submission` folder by Coursera.

3. It then builds the code as per user-supplied commands.

4. Then, it runs the code in a working directory containing input files while using input and output redirection for handling standard input, error and output.

5. Any program-generated files are also compared to user-specified files.

6. If the first test case (generally the test case open to the learners in the assignment as a specification) fails, then it provides detailed token-based matching feedback to the learners, And the fractional score is brought down to zero.

7. A fractional score is provided based on a configurable PENALTY variable, which limits the maximum number of failed test cases to 1/PENALTY before awarding a zero score if the number of test cases exceeds 1/PENALTY.

## Token-based text matching:

* Common punctuation marks are removed from the text, and the text is converted to lowercase. Special consideration is given to removing full stops while retaining decimal points.

* Tokens are generated by splitting the transformed string at blank spaces, tabs, newline and linefeed characters. Empty tokens are removed.

* The sequence of tokens thus generated should match with the test.

## How to use

1. Copy the contents `partTemplate` folder into a `part_N` folder (`N` is any text, generally integer).
2. Inside the `part_N` folderCoursera's programming assignment creation web interface
   1. Fill up the details as per **Table 1**.
   2. For each test case, copy the contents of `testcaseTemplate` into a `testcase_N` folder (`N` is any text, generally an integer)
   3. Inside the `testcase_N` folder, fill up the details as per **Table 2**
3. Create a docker zip file by compressing the topmost directory contents (contains file `Docker` and a folder named `files`)
4. Upload and select it as a custom auto-grader for each part in the programming assignment creation web interface of Coursera.

### Table 1: Contents of *part_N* folder

| File / Folder             | Description                                                                                                                                                                                                   |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Coursera_PartID.txt`     | Put PartId as per the Coursera programming assignment part in the web interface.                                                                                                                              |
| `Submission_Filename.txt` | Put submission filename with extension (case-sensitive)                                                                                                                                                       |
| `Build_Command.txt`       | Specify the full build command as a single line such that it produces a program named `testApp`. Can run `Remove_Main.py` using python3 to remove the `main()` function from user submissions (see snippets). |
| `build_directory` folder  | Put additional files if needed for compilation here. (eg. makefile, header files, custom `main.c` or `main.cpp` for function and class testing)                                                               |
| `testcaseTemplate` folder | Do not change contents. Use as a template for `testcase_N` folders.                                                                                                                                           |
| `testcase_N` folder       | Contains details for each test case                                                                                                                                                                           |

### Table 2: Contents of *testcase_N* folder

| File / Folder                  | Description                                                                                         |
| ------------------------------ | --------------------------------------------------------------------------------------------------- |
| `input_commandline.txt`        | Single Line. Specify the command line arguments to be sent while invoking the program.              |
| `input_console.txt`            | Specify the input to be provided to the standard input (stdin)                                      |
| `expected_output_console.txt`  | Expected output from the program for grading                                                        |
| `working_directory` folder     | Save additional files available to the program for reading                                          |
| `expected_output_files` folder | Expected output files supposed to be generated by the program in the working directory for grading. |

## Common snippets for Build_Command.txt :

* Building with user submitted `main()` function: `gcc -o testApp ./*.c`
* Building after removing user submitted `main()` function: `python3 Remove_Main.py && gcc -o testApp ./*.c`
  * The `Remove_Main.py` script does not remove the `main()` function from files ending with `_.c`. 
* Can use any shell command. Even make.

## Acknowledgements:

Initial programming tips: [@ShawnHymel](https://www.github.com/ShawnHymel)
