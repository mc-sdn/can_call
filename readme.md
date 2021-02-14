
# `can_call`
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/vili-1/can_call)

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fvili-1%2Fcan_call&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://github.com/vili-1/can_call)
[![GitHub forks](https://img.shields.io/github/forks/vili-1/can_call)](https://github.com/vili-1/can_call/network)
[![GitHub stars](https://img.shields.io/github/stars/vili-1/can_call?color=yellowgreen)](https://github.com/vili-1/can_call/stargazers)
<img src="https://img.shields.io/badge/made%20with-python-blueviolet.svg" alt="made with python">
[![Open Source Love](https://badges.frapsoft.com/os/v3/open-source.svg?v=103)](https://github.com/vili-1/can_call)



<img src="https://img.shields.io/badge/keywords-Clang,%20AST,%20Python bindings to libclang-cyan.svg" alt="keywords">


<!---[![Github All Releases](https://img.shields.io/github/downloads/vili-1/can_call/total.svg)](https://github.com/vili-1/can_call)--->
<!---[![Github Releases (by Release)](https://img.shields.io/github/downloads/vili-1/can_call/v1.1/total.svg)](https://github.com/vili-1/can_call/releases/)--->


## About the `can_call`

`can_call` is a toy script to check if there exists a path between two vertices in the execution path of functions that a C program goes through.
`can_call` parses and analyses C code in Python with Clang which enables such usage through `libclang` (with [Python bindings](https://github.com/llvm-mirror/clang/tree/master/bindings/python)).
Clang converts the C-files into an abstract syntax tree (AST) and manipulates the AST by considering nodes (or certain [properties of nodes](https://coggle.it/diagram/VSk7_32dyC9M7Wtk/t/python-clang)).


## Requirements

* LLVM/Clang -- check out the [getting
  started](http://clang.llvm.org/get_started.html) guide to find out how to obtain Clang from source. `libclang` is
  built and installed along with the Clang compiler.

----

**Please note**: Unfortunately, the state of documentation for Python bindings to `libclang` is very lacking. Expect to have to look through the `libclang` API.

----


## Usage

If you are running `can_call` from the terminal, just pass the arguments after the script name as follows:

```console
python3 can_call.py <filename> <caller> <callee>
```
where

- `<filename>` is a C file
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


Clang has a builtin AST-dump mode; below, the `some_file.c` converted into an AST.

![Alt text here](AST_example.svg)



## References
`libclang`

> *  <a href="https://eli.thegreenplace.net/2011/07/03/parsing-c-in-python-with-clang"><button type="button" 
style="
            cursor: pointer;
">Eli Bendersky's website
</button></a>
> *  <a href="http://llvm.org/devmtg/2010-11/Gregor-libclang.pdf"><button type="button" 
style="
            cursor: pointer;
">libclang: Thinking Beyond the Compiler
</button></a>
> *  <a href="http://clang.llvm.org/doxygen/group__CINDEX.html"><button type="button" 
style="
            cursor: pointer;
">libclang: C Interface to Clang
</button></a>
> *  <a href="https://github.com/llvm-mirror/clang/blob/master/bindings/python/clang/cindex.py"><button type="button" 
style="
            cursor: pointer;
">clang/bindings/python/clang/cindex.py
</button></a>
