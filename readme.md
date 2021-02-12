
# `can_call`

[![HitCount](http://hits.dwyl.com/mc-sdn/can_call.svg)](http://hits.dwyl.com/mc-sdn/can_call)



## About the `can_call`

`can_call` is a toy script to check if there exists a path between two vertices in the execution path of functions that a C program goes through.
`can_call` parses and analyses C code in Python with Clang which enables such usage through `libclang` (with Python bindings).


## Requirements

* LLVM/Clang -- check out the [getting
  started](http://clang.llvm.org/get_started.html) guide to find out how to obtain Clang from source. `libclang` is
  built and installed along with the Clang compiler.

----

**Please note**: Unfortunately, the state of documentation for `libclang` and its Python bindings is very lacking. 

----


## Usage

If you are running `can_call` from the terminal, just pass the arguments after the script name as follows:

```console
python3 can_call <filename> <caller> <callee>
```
where

- `<some_file.c>` is a C file
- `<caller>` is the name of a function declared in `<some_file.c>`
- `<callee>` is the name of a function declared in `<some_file.c>`

### Example


Suppose we invoke `can_call` on the C-code `some_file.c` below: 

```c
void baz(); // prototype

void foo() { }

void bar() {
    foo();
    baz();
}

void baz() {
    if (0)
        bar();
}

void bizz() { }

void buzz() {
    bizz();
}

int main() {
    foo();
    baz();
    buzz();
}
```

Executing `can_call` to find whether exists a path in the call graph for `some_file.c` from `caller`-function to `callee`-one, given in the table, we get:

| `caller`    | `callee` | Expected Output   |
| ----------- | ---------|----------|
| main        | baz      | True      |
| baz         | bar      | True      |
| buzz        | foo      | None      |
| baz         | baz      | True      |


```console
$ python3 can_call.py some_file.c main baz
True
$ python3 can_call.py some_file.c baz bar
True
$ python3 can_call.py some_file.c buzz foo
None
$ python3 can_call.py some_file.c baz baz
True
```

Clang converts the C-files into an abstract syntax tree (AST) and manipulates the AST. 
Clang has also a builtin AST-dump mode; below, the `some_file.c` converted into an AST.

![Alt text here](AST_example.svg)





